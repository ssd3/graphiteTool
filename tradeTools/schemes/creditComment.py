import graphene
from graphene_django import DjangoObjectType
from tradeTools.libs.common_db import *


class CreditCommentType(DjangoObjectType):
    class Meta:
        model = Creditcomment


class CreateCreditComment(graphene.Mutation):
    class Arguments:
        creditid = graphene.Int(required=True)
        comment = graphene.String(required=True)

    creditcomment = graphene.Field(CreditCommentType)

    def mutate(self, info, **kwargs):
        creditcomment = create_creditcomment(info, kwargs)
        return CreateCreditComment(creditcomment=creditcomment)


class UpdateCreditComment(graphene.Mutation):
    class Arguments:
        creditcommentid = graphene.Int(required=True)
        creditid = graphene.Int(required=True)
        comment = graphene.String()

    creditcomment = graphene.Field(CreditCommentType)

    def mutate(self, info, **kwargs):
        creditcomment = update_creditcomment(kwargs)
        creditcomment.save()
        return UpdateCreditComment(creditcomment=creditcomment)


class CreditCommentMutation(graphene.ObjectType):
    create_creditcomment = CreateCreditComment.Field()
    update_creditcomment = UpdateCreditComment.Field()


class CreditCommentQuery(graphene.ObjectType):
    creditcomments = graphene.List(CreditCommentType)
    creditcomment = graphene.Field(CreditCommentType, creditcommentid=graphene.Int())
    creditcomments_bycredit = graphene.List(CreditCommentType, creditid=graphene.Int())

    def resolve_creditcomments(self, info, **kwargs):
        return Creditcomment.objects.all()

    def resolve_creditcomments_bycredit(self, info, **kwargs):
        creditid = kwargs.get('creditid')

        if creditid is not None:
            return Creditcomment.objects.filter(creditid=creditid)

        return None

    def resolve_creditcomment(self, info, **kwargs):
        creditcommentid = kwargs.get('creditcommentid')

        if creditcommentid is not None:
            return Creditcomment.objects.get(pk=creditcommentid)

        return None
