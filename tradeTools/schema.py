import graphene
import testTool.schema


class Query(testTool.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)