# import graphene
# from graphene_django import DjangoObjectType
#
# from hn_users.models import HNUser
#
# class HNUserType(DjangoObjectType):
#     class Meta:
#         model = HNUser
#
# class Query(graphene.ObjectType):
#     users = graphene.List(HNUserType)
#
#     def resolve_links(self, info, **kwargs):
#         return HNUser.objects.all()
#
#
# class CreateHNUser(graphene.Mutation):
