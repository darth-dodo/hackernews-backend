import graphene
from graphene_django import DjangoObjectType

from hn_users.schema import HNUserType
from links.models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    def resolve_links(self, info, **kwargs):
        return Link.objects.all()


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


class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
