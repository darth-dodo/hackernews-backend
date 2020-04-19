import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

from hn_users.models import HNUser


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class HNUserType(DjangoObjectType):
    username = graphene.String()
    email = graphene.String()
    full_name = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    is_active = graphene.String()
    superuser_access = graphene.Boolean()

    class Meta:
        model = HNUser


class Query(graphene.ObjectType):
    hn_users = graphene.List(HNUserType)
    me = graphene.Field(HNUserType)

    def resolve_hn_users(self, info, **kwargs):
        return HNUser.objects.all()

    def resolve_me(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Not Logged in!")

        return user.hn_user


class CreateHNUser(graphene.Mutation):
    hn_user = graphene.Field(HNUserType)

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        bio = graphene.String()

    def mutate(self, info, username, password, email, bio):
        user = get_user_model()(username=username, email=email)
        user.set_password(password)
        user.save()

        hn_user_obj = HNUser()
        hn_user_obj.django_user = user
        hn_user_obj.bio = bio
        hn_user_obj.save()

        return CreateHNUser(hn_user=hn_user_obj)


class Mutation(graphene.ObjectType):
    create_hn_user = CreateHNUser.Field()
