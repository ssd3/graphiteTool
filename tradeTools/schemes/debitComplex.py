import graphene
from tradeTools.libs.common_db import *
from tradeTools.libs.common import *
from tradeTools.schemes.product import ProductType, CreateProduct
from tradeTools.schemes.productDetails import ProductDetailsType
from tradeTools.schemes.productComment import ProductCommentType
from tradeTools.schemes.debit import DebitType


class ProductInput(graphene.InputObjectType):
    categoryid = graphene.Int(required=True)
    title = graphene.String(required=True)
    description = graphene.String()


class ProductDetailsInput(graphene.InputObjectType):
    model = graphene.String()
    url = graphene.String()
    serialno = graphene.String()
    weight = graphene.Decimal(default=0.0)
    height = graphene.Decimal(default=0.0)
    width = graphene.Decimal(default=0.0)
    length = graphene.Decimal(default=0.0)


class ProductCommentInput(graphene.InputObjectType):
    comment = graphene.String()


class DebitInput(graphene.InputObjectType):
    warehouseid = graphene.Int(required=True)
    qty = graphene.Decimal()
    price = graphene.Decimal()
    pricetypeid = graphene.Int()
    discountid = graphene.Int()
    tracknumber = graphene.String(required=True)
    statusid = graphene.Int()
    notes = graphene.String()


class CreateDebitComplex(graphene.Mutation):
    class Arguments:
        product_data = ProductInput(required=True)
        productdetails_data = ProductDetailsInput()
        productcomment_data = ProductCommentInput()
        debit_data = DebitInput(required=True)

    product = graphene.Field(ProductType)
    productdetails = graphene.Field(ProductDetailsType)
    productcomment = graphene.Field(ProductCommentType)
    debit = graphene.Field(DebitType)

    @staticmethod
    def mutate(self, info, **kwargs):
        product_data = delete_none_keys(kwargs.get("product_data"))
        productdetails_data = delete_none_keys(kwargs.get("productdetails_data"))
        productcomment_data = delete_none_keys(kwargs.get("productcomment_data"))
        debit_data = delete_none_keys(kwargs.get("debit_data"))

        # tracknumber unique check before
        try:
            if Debit.objects.get(tracknumber=debit_data.get("tracknumber")) is not None:
                raise ValueError('TrackNumber must be unique.')
        except Debit.DoesNotExist:
            pass

        product = create_product(info, product_data)
        debit_data.update({'productid': product.productid})
        debit = create_debit(info, debit_data)

        productdetails = None
        productcomment = None

        if len(productdetails_data) > 0:
            productdetails_data.update({'productid': product.productid})
            productdetails = create_productdetails(info, productdetails_data)

        if len(productcomment_data) > 0:
            productcomment_data.update({'productid': product.productid})
            productcomment = create_productcomment(info, productcomment_data)

        return CreateDebitComplex(product=product,
                                  productdetails=productdetails,
                                  productcomment=productcomment,
                                  debit=debit)


class DebitComplexMutation(graphene.ObjectType):
    create_debitcomplex = CreateDebitComplex.Field()
