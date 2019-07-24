import graphene
from graphene_django.types import DjangoObjectType
from django.utils import timezone
from tradeTools.models import *


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
        productdetails = Productdetails(productid=Product.objects.get(pk=kwargs.get("productid")),
                                        model=kwargs.get("model", None),
                                        url=kwargs.get("url", None),
                                        serialno=kwargs.get("serialno", None),
                                        weight=kwargs.get("weight", 0.0),
                                        height=kwargs.get("height", 0.0),
                                        width=kwargs.get("width", 0.0),
                                        length=kwargs.get("length", 0.0),
                                        userid=AuthUser.objects.get(pk=info.context.user.id),
                                        created=timezone.now())
        productdetails.save()
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
        productdetails = Productdetails.objects.get(pk=kwargs.get("productdetailsid"))
        productdetails.productid = Product.objects.get(pk=kwargs.get("productid"))
        productdetails.model = kwargs.get("model", None)
        productdetails.url = kwargs.get("url", None)
        productdetails.serialno = kwargs.get("serialno", None)
        productdetails.weight = kwargs.get("weight", 0.0)
        productdetails.height = kwargs.get("height", 0.0)
        productdetails.width = kwargs.get("width", 0.0)
        productdetails.length = kwargs.get("length", 0.0)

        productdetails.save()
        return UpdateProductDetails(productdetails=productdetails)


class ProductDetailsMutation(graphene.ObjectType):
    create_productdetails = CreateProductDetails.Field()
    update_productdetails = UpdateProductDetails.Field()


