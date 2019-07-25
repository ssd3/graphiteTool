import graphene
from graphene_django.types import DjangoObjectType
from tradeTools.libs.common_db import *


class ProductDetailsType(DjangoObjectType):
    class Meta:
        model = Productdetails


class ProductDetailsQuery(graphene.ObjectType):
    productdetails = graphene.List(ProductDetailsType, productid=graphene.Int())
    productdetail = graphene.Field(ProductDetailsType, productdetailsid=graphene.Int())

    @staticmethod
    def resolve_productdetails(self, info, **kwargs):
        productid = kwargs.get('productid')

        if productid is not None:
            return Productdetails.objects.filter(productid=productid)

        return None

    @staticmethod
    def resolve_productdetail(self, info, **kwargs):
        productdetailsid = kwargs.get('productdetailsid')

        if productdetailsid is not None:
            return Productdetails.objects.get(pk=productdetailsid)

        return None


class CreateProductDetails(graphene.Mutation):
    class Arguments:
        productid = graphene.Int(required=True)
        model = graphene.String()
        url = graphene.String()
        serialno = graphene.String()
        weight = graphene.Decimal()
        height = graphene.Decimal()
        width = graphene.Decimal()
        length = graphene.Decimal()

    productdetails = graphene.Field(ProductDetailsType)

    def mutate(self, info, **kwargs):
        productdetails = create_productdetails(info, kwargs)
        return CreateProductDetails(productdetails=productdetails)


class UpdateProductDetails(graphene.Mutation):
    class Arguments:
        productdetailsid = graphene.Int(required=True)
        productid = graphene.Int(required=True)
        model = graphene.String()
        url = graphene.String()
        serialno = graphene.String()
        weight = graphene.Decimal()
        height = graphene.Decimal()
        width = graphene.Decimal()
        length = graphene.Decimal()

    productdetails = graphene.Field(ProductDetailsType)

    def mutate(self, info, **kwargs):
        productdetails = update_productdetails(kwargs)
        return UpdateProductDetails(productdetails=productdetails)


class ProductDetailsMutation(graphene.ObjectType):
    create_productdetails = CreateProductDetails.Field()
    update_productdetails = UpdateProductDetails.Field()


