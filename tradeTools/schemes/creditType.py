import graphene
from graphene_django import DjangoObjectType
from tradeTools.libs.common_db import *


class CredittypeType(DjangoObjectType):
    class Meta:
        model = Credittype


class CreateCreditType(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String()

    credittype = graphene.Field(CredittypeType)

    def mutate(self, info, **kwargs):
        credittype = create_credittype(info, kwargs)
        return CreateCreditType(credittype=credittype)


class UpdateCreditType(graphene.Mutation):
    class Arguments:
        credittypeid = graphene.Int(required=True)
        title = graphene.String()
        description = graphene.String()

    credittype = graphene.Field(CredittypeType)

    def mutate(self, info, **kwargs):
        credittype = update_credittype(kwargs)
        credittype.save()
        return UpdateCreditType(credittype=credittype)


class CreditTypeMutation(graphene.ObjectType):
    create_credittype = CreateCreditType.Field()
    update_credittype = UpdateCreditType.Field()


class CreditTypeQuery(graphene.ObjectType):
    credittypes = graphene.List(CredittypeType)
    credittype = graphene.Field(CredittypeType, credittypeid=graphene.Int())

    def resolve_credittypes(self, info, **kwargs):
        return Credittype.objects.all()

    def resolve_credittype(self, info, **kwargs):
        credittypeid = kwargs.get('credittypeid')

        if credittypeid is not None:
            return Credittype.objects.get(pk=credittypeid)

        return None
