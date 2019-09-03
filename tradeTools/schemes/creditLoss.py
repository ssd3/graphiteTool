import graphene
from graphene_django import DjangoObjectType
from tradeTools.libs.common_db import *


class CreditLossType(DjangoObjectType):
    class Meta:
        model = Creditloss


class CreateCreditLoss(graphene.Mutation):
    class Arguments:
        creditid = graphene.Int(required=True)
        losstypeid = graphene.Int(required=True)
        rate = graphene.Decimal(required=True)
        notes = graphene.String()

    creditloss = graphene.Field(CreditLossType)

    def mutate(self, info, **kwargs):
        creditloss = create_creditloss(info, kwargs)
        return CreateCreditLoss(creditloss=creditloss)


class UpdateCreditLoss(graphene.Mutation):
    class Arguments:
        creditlossid = graphene.Int(required=True)
        creditid = graphene.Int()
        losstypeid = graphene.Int()
        rate = graphene.Decimal()
        notes = graphene.String()

    creditloss = graphene.Field(CreditLossType)

    def mutate(self, info, **kwargs):
        creditloss = update_creditloss(kwargs)
        creditloss.save()
        return UpdateCreditLoss(creditloss=creditloss)


class CreditLossMutation(graphene.ObjectType):
    create_creditloss = CreateCreditLoss.Field()
    update_creditloss = UpdateCreditLoss.Field()


class CreditLossQuery(graphene.ObjectType):
    creditlosses = graphene.List(CreditLossType, creditid=graphene.Int())
    creditloss = graphene.Field(CreditLossType, creditlossid=graphene.Int())

    def resolve_creditlosses(self, info, **kwargs):
        creditid = kwargs.get('creditid')

        if creditid is not None:
            return Creditloss.objects.filter(creditid=creditid)

        return None

    def resolve_creditloss(self, info, **kwargs):
        creditlossid = kwargs.get('creditlossid')

        if creditlossid is not None:
            return Creditloss.objects.get(pk=creditlossid)

        return None
