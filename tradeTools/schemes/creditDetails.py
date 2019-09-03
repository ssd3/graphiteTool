import graphene
from graphene_django import DjangoObjectType
from tradeTools.libs.common_db import *


class CreditDetailsType(DjangoObjectType):
    class Meta:
        model = Creditdetails


class CreateCreditDetail(graphene.Mutation):
    class Arguments:
        creditid = graphene.Int(required=True)
        productid = graphene.Int(required=True)
        price = graphene.Decimal(required=True)
        qty = graphene.Decimal(required=True)
        pricetypeid = graphene.Int(required=True)

    creditdetail = graphene.Field(CreditDetailsType)

    def mutate(self, info, **kwargs):
        creditdetail = create_creditdetail(info, kwargs)
        return CreateCreditDetail(creditdetail=creditdetail)


class UpdateCreditDetail(graphene.Mutation):
    class Arguments:
        creditdetailid = graphene.Int(required=True)
        creditid = graphene.Int()
        productid = graphene.Int()
        price = graphene.Decimal()
        qty = graphene.Decimal()
        pricetypeid = graphene.Int()

    creditdetail = graphene.Field(CreditDetailsType)

    def mutate(self, info, **kwargs):
        creditdetail = update_creditdetail(kwargs)
        creditdetail.save()
        return UpdateCreditDetail(creditdetail=creditdetail)


class CreditDetailMutation(graphene.ObjectType):
    create_creditdetail = CreateCreditDetail.Field()
    update_creditdetail = UpdateCreditDetail.Field()


class CreditDetailsQuery(graphene.ObjectType):
    creditdetails = graphene.List(CreditDetailsType, creditid=graphene.Int())
    creditdetail = graphene.Field(CreditDetailsType, creditdetailid=graphene.Int())

    def resolve_creditdetails(self, info, **kwargs):
        creditid = kwargs.get('creditid')

        if creditid is not None:
            return Creditdetails.objects.filter(creditid=creditid)

        return None

    def resolve_creditdetail(self, info, **kwargs):
        creditdetailid = kwargs.get('creditdetailid')

        if creditdetailid is not None:
            return Creditdetails.objects.get(pk=creditdetailid)

        return None
