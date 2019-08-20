import graphene
from graphene_django import DjangoObjectType
from tradeTools.libs.common_db import *


class LosstypeType(DjangoObjectType):
    class Meta:
        model = Losstype


class CreateLossType(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)

    losstype = graphene.Field(LosstypeType)

    def mutate(self, info, **kwargs):
        losstype = create_losstype(info, kwargs)
        return CreateLossType(losstype=losstype)


class UpdateLossType(graphene.Mutation):
    class Arguments:
        losstypeid = graphene.Int(required=True)
        title = graphene.String(required=True)

    losstype = graphene.Field(LosstypeType)

    def mutate(self, info, **kwargs):
        losstype = update_losstype(kwargs)
        losstype.save()
        return UpdateLossType(losstype=losstype)


class LossTypeMutation(graphene.ObjectType):
    create_losstype = CreateLossType.Field()
    update_losstype = UpdateLossType.Field()


class LossTypeQuery(graphene.ObjectType):
    losstypes = graphene.List(LosstypeType)
    losstype = graphene.Field(LosstypeType, losstypeid=graphene.Int())

    def resolve_losstypes(self, info, **kwargs):
            return Losstype.objects.all()

    def resolve_losstype(self, info, **kwargs):
        losstypeid = kwargs.get('losstypeid')

        if losstypeid is not None:
            return Losstype.objects.get(pk=losstypeid)

        return None
