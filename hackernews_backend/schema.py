import graphene

from hn_users import schema as hn_users_schema
from links import schema as links_schema


class Query(hn_users_schema.Query, links_schema.Query, graphene.ObjectType):
    pass


class Mutation(hn_users_schema.Mutation, links_schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
