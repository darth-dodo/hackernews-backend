import graphene
import graphql_jwt

from hn_users import schema as hn_users_schema
from links import schema as links_schema
from links import schema_relay as links_schema_relay


class Query(
    hn_users_schema.Query,
    links_schema.Query,
    links_schema_relay.RelayQuery,
    graphene.ObjectType,
):
    pass


class Mutation(hn_users_schema.Mutation, links_schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
