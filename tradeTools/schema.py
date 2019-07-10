import graphene
from graphene_django import DjangoObjectType
from .models import Product, Category, User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    user = graphene.Field(UserType,
                          userid=graphene.Int(),
                          username=graphene.String(),
                          email=graphene.String(),
                          description=graphene.String())

    products = graphene.List(ProductType)
    categories = graphene.List(CategoryType)

    def resolve_user(self, info, **kwargs):
        userid = kwargs.get('userid')
        username = kwargs.get('username')
        email = kwargs.get('email')
        description = kwargs.get('description')

        if userid is not None:
            return User.objects.get(pk=userid)

        if username is not None:
            return User.objects.get(username=username)

        if email is not None:
            return User.objects.get(email=email)

        if description is not None:
            return User.objects.get(description=description)

        return None

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_products(self, info, **kwargs):
        return Product.objects.all().order_by('-productid')

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()


schema = graphene.Schema(query=Query)