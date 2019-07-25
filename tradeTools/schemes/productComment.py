import graphene
from graphene_django.types import DjangoObjectType
from tradeTools.libs.common_db import *


class ProductCommentType(DjangoObjectType):
    class Meta:
        model = Productcomment


class ProductCommentQuery(graphene.ObjectType):
    productcomments = graphene.List(ProductCommentType, productid=graphene.Int())
    productcomment = graphene.Field(ProductCommentType, productcommentid=graphene.Int())

    @staticmethod
    def resolve_productcomments(self, info, **kwargs):
        productid = kwargs.get('productid')

        if productid is not None:
            return Productcomment.objects.filter(productid=productid)

        return None

    @staticmethod
    def resolve_productcomment(self, info, **kwargs):
        productcommentid = kwargs.get('productcommentid')

        if productcommentid is not None:
            return Productcomment.objects.get(pk=productcommentid)

        return None


class CreateProductComment(graphene.Mutation):
    class Arguments:
        productid = graphene.Int(required=True)
        comment = graphene.String()

    productcomment = graphene.Field(ProductCommentType)

    def mutate(self, info, **kwargs):
        productcomment = create_productcomment(info, kwargs)
        return CreateProductComment(productcomment=productcomment)


class UpdateProductComment(graphene.Mutation):
    class Arguments:
        productcommentid = graphene.Int(required=True)
        comment = graphene.String()

    productcomment = graphene.Field(ProductCommentType)

    def mutate(self, info, **kwargs):
        productcomment = update_productcomment(kwargs)
        return UpdateProductComment(productcomment=productcomment)


class ProductCommentMutation(graphene.ObjectType):
    create_productcomment = CreateProductComment.Field()
    update_productcomment = UpdateProductComment.Field()
