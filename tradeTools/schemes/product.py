import graphene
from graphene_django import DjangoObjectType
from graphene import relay
from tradeTools.libs.common_db import *


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        interface = (relay.Node, )


class ProductConnection(relay.Connection):
    class Meta:
        node = ProductType


class CreateProduct(graphene.Mutation):
    class Arguments:
        categoryid = graphene.Int(required=True)
        title = graphene.String(required=True)
        description = graphene.String()

    product = graphene.Field(ProductType)

    @staticmethod
    def mutate(self, info, **kwargs):
        product = create_product(info, kwargs)
        return CreateProduct(product=product)


class UpdateProduct(graphene.Mutation):
    class Arguments:
        productid = graphene.Int(required=True)
        categoryid = graphene.Int(required=True)
        title = graphene.String(required=True)
        description = graphene.String()

    product = graphene.Field(ProductType)

    def mutate(self, info, **kwargs):
        product = update_product(kwargs)
        return UpdateProduct(product=product)


class ProductMutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()


class ProductQuery(graphene.ObjectType):
    products_byuser = relay.ConnectionField(ProductConnection)
    products = relay.ConnectionField(ProductConnection)
    product = graphene.List(ProductType,
                            productid=graphene.Int(),
                            title=graphene.String(),
                            userid=graphene.Int(),
                            page=graphene.Int())

    def resolve_products(root, info, **kwargs):
        return Product.objects.all().order_by('productid')

    def resolve_products_byuser(self, info, **kwargs):
        return Product.objects.filter(userid=info.context.user.id)

    def resolve_product(self, info, **kwargs):
        productid = kwargs.get('productid')
        title = kwargs.get('title')
        userid = kwargs.get('userid')
        page = kwargs.get('page')

        if productid is not None:
            return Product.objects.filter(productid=productid)

        if title is not None:
            return Product.objects.filter(title=title)

        if userid is not None:
            return Product.objects.filter(userid=userid)

        if page is not None:
            products_per_page = 5
            products_to = products_per_page * page
            products_from = products_to - products_per_page
            return Product.objects.all()[products_from:products_to]

        return None

