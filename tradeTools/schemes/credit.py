import graphene
from graphene_django import DjangoObjectType
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from tradeTools.libs.common_db import *
from tradeTools.libs.total_count import ExtendedConnection


class CreditType(DjangoObjectType):
    class Meta:
        model = Credit
        filter_fields = {
            'credittypeid': ['exact', 'in']
        }
        interfaces = (relay.Node,)
        connection_class = ExtendedConnection


class CreditConnection(relay.Connection):
    class Meta:
        node = CreditType


class CreateCredit(graphene.Mutation):
    class Arguments:
        credittypeid = graphene.Int(required=True)
        buyerid = graphene.Int(required=True)
        fromwarehouseid = graphene.Int()
        towarehouseid = graphene.Int()
        sent = graphene.DateTime()
        received = graphene.DateTime()

    credit = graphene.Field(CreditType)

    def mutate(self, info, **kwargs):
        credit = create_credit(info, kwargs)
        return CreateCredit(credit=credit)


class UpdateCredit(graphene.Mutation):
    class Arguments:
        creditid = graphene.Int(required=True)
        credittypeid = graphene.Int(required=True)
        buyerid = graphene.Int(required=True)
        fromwarehouseid = graphene.Int()
        towarehouseid = graphene.Int()
        sent = graphene.DateTime()
        received = graphene.DateTime()

    credit = graphene.Field(CreditType)

    def mutate(self, info, **kwargs):
        credit = update_credit(kwargs)
        credit.save()
        return UpdateCredit(credit=credit)


class CreditMutation(graphene.ObjectType):
    create_credit = CreateCredit.Field()
    update_credit = UpdateCredit.Field()


class CreditQuery(graphene.ObjectType):
    credits = DjangoFilterConnectionField(CreditType)
    credit = graphene.Field(CreditType, creditid=graphene.Int())

    def resolve_credits(self, info, **kwargs):
        return Credit.objects.all()

    def resolve_credit(self, info, **kwargs):
        creditid = kwargs.get('creditid')

        if creditid is not None:
            return Credit.objects.get(pk=creditid)

        return None