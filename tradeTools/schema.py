import graphene
from graphene_django import DjangoObjectType
import testTool.schema
from .models import Product, Category


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class Query(graphene.ObjectType):
    products = graphene.List(ProductType)
    categories = graphene.List(CategoryType)

    def resolve_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()


schema = graphene.Schema(query=Query)