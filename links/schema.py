import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from hn_users.schema import HNUserType
from links.models import Link, Vote


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class VoteType(DjangoObjectType):
    class Meta:
        model = Vote


class Query(graphene.ObjectType):
    links = graphene.List(LinkType)
    votes = graphene.List(VoteType)

    def resolve_links(self, info, **kwargs):
        return Link.objects.all()

    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()


class CreateLink(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()
    posted_by = graphene.Field(HNUserType)

    class Arguments:
        url = graphene.String()
        description = graphene.String()

    def mutate(self, info, url, description):

        hn_user = info.context.user.hn_user or None

        link = Link()
        link.url = url
        link.description = description
        link.posted_by = hn_user

        link.save()

        return CreateLink(
            id=link.id, url=link.url, posted_by=hn_user, description=link.description
        )


class CreateVote(graphene.Mutation):
    vote = graphene.Field(VoteType)

    class Arguments:
        link_id = graphene.Int()

    def mutate(self, info, link_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Please login to vote!")

        try:
            hn_user = user.hn_user
        except AttributeError:
            raise GraphQLError("Invalid User!")

        try:
            link = Link.objects.get(id=link_id)
        except Link.DoesNotExist:
            raise GraphQLError("Invalid Link!")

        new_vote = Vote()
        new_vote.user = hn_user
        new_vote.link = link
        new_vote.save()

        return CreateVote(vote=new_vote)


class RegisterUnvote(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        link_id = graphene.Int()

    def mutate(self, info, link_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Please login to unvote!")

        try:
            hn_user = user.hn_user
        except AttributeError:
            raise GraphQLError("Invalid User!")

        try:
            vote = hn_user.hn_user_votes.get(link_id=link_id)
            vote.delete()
            return RegisterUnvote(success=True)
        except Vote.DoesNotExist:
            return RegisterUnvote(success=None)


class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
    create_vote = CreateVote.Field()
    register_unvote = RegisterUnvote.Field()
