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
    losstypeid = graphene.Int(required=True)
    rate = graphene.Decimal(required=True)
    notes = graphene.String()


class CreditLossesInput(graphene.InputObjectType):
    creditlosses = graphene.List(CreditLossInput)


class CreditDetailInput(graphene.InputObjectType):
    productid = graphene.Int(required=True)
    price = graphene.Decimal(required=True)
    qty = graphene.Decimal(required=True)
    pricetypeid = graphene.Int(required=True)


class CreditDetailsInput(graphene.InputObjectType):
    creditdetails = graphene.List(CreditDetailInput)


class CreditCommentInput(graphene.InputObjectType):
    comment = graphene.String(required=True)


class CreateCreditComplex(graphene.Mutation):
    class Arguments:
        credit_data = CreditInput(required=True)
        creditloss_data = CreditLossesInput(required=True)
        creditdetails_data = CreditDetailsInput(required=True)
        creditcomment_data = CreditCommentInput()

    credit = graphene.Field(CreditType)
    creditloss = graphene.List(CreditLossType)
    creditdetails = graphene.List(CreditDetailsType)
    creditcomment = graphene.Field(CreditCommentType)

    @staticmethod
    def mutate(self, info, **kwargs):
        credit_data = delete_none_keys(kwargs.get("credit_data"))
        creditloss_data = kwargs.get("creditloss_data")
        creditdetails_data = kwargs.get("creditdetails_data")
        creditcomment_data = delete_none_keys(kwargs.get("creditcomment_data"))

        credit = create_credit(info, credit_data)
        creditlosses = create_creditlosses(info, creditloss_data)
        creditdetails = create_productdetails(info, creditdetails_data)
        creditcomment = create_creditcomment(info, creditcomment_data)

        return CreateCreditComplex(credit=credit,
                                   creditloss=creditlosses,
                                   creditdetails=creditdetails,
                                   creditcomment=creditcomment)


class CreditComplexMutation(graphene.ObjectType):
    create_creditcomplex = CreateCreditComplex.Field()
