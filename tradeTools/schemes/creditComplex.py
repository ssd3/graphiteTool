import graphene

from tradeTools.libs.common_db import *
from tradeTools.libs.common import delete_none_keys
from tradeTools.schemes.credit import CreditType
from tradeTools.schemes.creditComment import CreditCommentType
from tradeTools.schemes.creditDetails import CreditDetailsType
from tradeTools.schemes.creditLoss import CreditLossType


class CreditInput(graphene.InputObjectType):
    credittypeid = graphene.Int(required=True)
    buyerid = graphene.Int(required=True)
    fromwarehouseid = graphene.Int()
    towarehouseid = graphene.Int()
    sent = graphene.DateTime()
    received = graphene.DateTime()
    tracknumber = graphene.String()


class CreditLossInput(graphene.InputObjectType):
    creditid = graphene.Int(required=True)
    losstypeid = graphene.Int(required=True)
    rate = graphene.Decimal(required=True)
    notes = graphene.String()


class CreditDetailsInput(graphene.InputObjectType):
    creditid = graphene.Int(required=True)
    productid = graphene.Int(required=True)
    price = graphene.Decimal(required=True)
    qty = graphene.Decimal(required=True)
    pricetypeid = graphene.Int(required=True)


class CreditCommentInput(graphene.InputObjectType):
    creditid = graphene.Int(required=True)
    comment = graphene.String(required=True)


class CreateCreditComplex(graphene.Mutation):
    class Arguments:
        credit_data = CreditInput(required=True)
        creditloss_data = graphene.List(CreditLossInput(required=True))
        creditdetails_data = graphene.List(CreditDetailsInput(required=True))
        creditcomment_data = CreditCommentInput()

    credit = graphene.Field(CreditType)
    creditloss = graphene.List(CreditLossType)
    creditdetails = graphene.List(CreditDetailsType)
    creditcomment = graphene.Field(CreditCommentType)

    @staticmethod
    def mutate(self, info, **kwargs):
        credit_data = delete_none_keys(kwargs.get("credit_data"))
        creditdetails_data = kwargs.get("creditdetails_data")
        creditcomment_data = delete_none_keys(kwargs.get("creditcomment_data"))
        creditloss_data = kwargs.get("debit_data")

        credit = create_credit(info, credit_data)

        return CreateCreditComplex(credit=credit,
                                   creditloss=None,
                                   creditdetails=None,
                                   creditcomment=None)


class CreditComplexMutation(graphene.ObjectType):
    create_creditcomplex = CreateCreditComplex.Field()
