import json

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
    fromwarehouseid = graphene.Int(required=True)
    towarehouseid = graphene.Int(required=True)
    sent = graphene.DateTime()
    received = graphene.DateTime()
    tracknumber = graphene.String()


class CreditUpdateInput(graphene.InputObjectType):
    creditid = graphene.Int(required=True)
    credittypeid = graphene.Int(required=True)
    buyerid = graphene.Int(required=True)
    fromwarehouseid = graphene.Int(required=True)
    towarehouseid = graphene.Int(required=True)
    sent = graphene.DateTime()
    received = graphene.DateTime()
    tracknumber = graphene.String()


class CreditLossInput(graphene.InputObjectType):
    losstypeid = graphene.Int(required=True)
    rate = graphene.Decimal(required=True)
    notes = graphene.String()


class CreditLossUpdateInput(graphene.InputObjectType):
    creditid = graphene.Int(required=True)
    creditlossid = graphene.Int()
    losstypeid = graphene.Int(required=True)
    rate = graphene.Decimal(required=True)
    notes = graphene.String()


class CreditLossesInput(graphene.InputObjectType):
    creditlosses = graphene.List(CreditLossInput)


class CreditLossesUpdateInput(graphene.InputObjectType):
    creditlosses = graphene.List(CreditLossUpdateInput)


class CreditDetailInput(graphene.InputObjectType):
    debitid = graphene.Int(required=True)
    productid = graphene.Int(required=True)
    price = graphene.Decimal(required=True)
    qty = graphene.Decimal(required=True)
    pricetypeid = graphene.Int(required=True)


class CreditDetailUpdateInput(graphene.InputObjectType):
    creditid = graphene.Int(required=True)
    creditdetailsid = graphene.Int()
    debitid = graphene.Int(required=True)
    productid = graphene.Int(required=True)
    price = graphene.Decimal(required=True)
    qty = graphene.Decimal(required=True)
    pricetypeid = graphene.Int(required=True)


class CreditDetailsInput(graphene.InputObjectType):
    creditdetails = graphene.List(CreditDetailInput)


class CreditDetailsUpdateInput(graphene.InputObjectType):
    creditdetails = graphene.List(CreditDetailUpdateInput)


class CreditCommentInput(graphene.InputObjectType):
    comment = graphene.String()


class CreditCommentUpdateInput(graphene.InputObjectType):
    creditcommentid = graphene.Int(required=True)
    comment = graphene.String()


class CreateCreditComplex(graphene.Mutation):
    class Arguments:
        credit_data = CreditInput(required=True)
        creditdetails_data = CreditDetailsInput(required=True)
        creditloss_data = CreditLossesInput()
        creditcomment_data = CreditCommentInput()

    credit = graphene.Field(CreditType)
    creditlosses = graphene.List(CreditLossType)
    creditdetails = graphene.List(CreditDetailsType)
    creditcomment = graphene.Field(CreditCommentType)

    @staticmethod
    def mutate(self, info, **kwargs):
        credit_data = delete_none_keys(kwargs.get("credit_data"))
        creditloss_data = kwargs.get("creditloss_data")
        creditdetails_data = kwargs.get("creditdetails_data")
        creditcomment_data = delete_none_keys(kwargs.get("creditcomment_data"))

        credit = create_credit(info, credit_data)
        creditlosses = create_creditlosses(info, creditloss_data.creditlosses, credit)
        creditdetails = create_creditdetails(info, creditdetails_data.creditdetails, credit)

        creditcomment = None
        if len(creditcomment_data) > 0:
            creditcomment = create_creditcomment(info, creditcomment_data, credit)

        return CreateCreditComplex(credit=credit,
                                   creditlosses=creditlosses,
                                   creditdetails=creditdetails,
                                   creditcomment=creditcomment)


class UpdateCreditComplex(graphene.Mutation):
    class Arguments:
        credit_data = CreditUpdateInput(required=True)
        creditdetails_data = CreditDetailsUpdateInput(required=True)
        creditloss_data = CreditLossesUpdateInput()
        creditcomment_data = CreditCommentUpdateInput()

    credit = graphene.Field(CreditType)
    creditlosses = graphene.List(CreditLossType)
    creditdetails = graphene.List(CreditDetailsType)
    creditcomment = graphene.Field(CreditCommentType)

    @staticmethod
    def mutate(self, info, **kwargs):
        credit_data = delete_none_keys(kwargs.get("credit_data"))
        creditloss_data = kwargs.get("creditloss_data")
        creditdetails_data = kwargs.get("creditdetails_data")
        creditcomment_data = delete_none_keys(kwargs.get("creditcomment_data"))

        credit = update_credit(info, credit_data)
        creditlosses = update_creditlosses(info, creditloss_data.creditlosses, credit)
        creditdetails = update_creditdetails(info, creditdetails_data.creditdetails, credit)

        creditcomment = None
        if len(creditcomment_data) > 0:
            creditcomment_data.creditid = credit
            creditcomment = update_creditcomment(creditcomment_data)

        return UpdateCreditComplex(credit=credit,
                                   creditlosses=creditlosses,
                                   creditdetails=creditdetails,
                                   creditcomment=creditcomment)


class CreditComplexMutation(graphene.ObjectType):
    create_creditcomplex = CreateCreditComplex.Field()
    update_creditcomplex = UpdateCreditComplex.Field()
