import graphene
from django.http import QueryDict
from django.utils import timezone
import datetime
from graphene_django import DjangoObjectType
from graphene import relay
# from graphql_extensions.auth.decorators import login_required
from graphql_jwt.decorators import login_required
from .models import Category, AuthUser, Pricetype, Discount
from tradeTools.schemes.jwtAuth import JwtAuth
from tradeTools.schemes.product import ProductMutation, ProductQuery
from tradeTools.schemes.debit import DebitMutation, DebitQuery
from tradeTools.schemes.credit import CreditMutation, CreditQuery
from tradeTools.schemes.creditDetails import CreditDetailsQuery, CreditDetailMutation
from tradeTools.schemes.productDetails import ProductDetailsMutation, ProductDetailsQuery
from tradeTools.schemes.warehouse import WarehouseQuery, WarehouseMutation
from tradeTools.schemes.productComment import ProductCommentMutation, ProductCommentQuery
from tradeTools.schemes.debitComplex import DebitComplexMutation
from tradeTools.schemes.status import StatusQuery, StatusMutation
from tradeTools.schemes.creditType import CreditTypeQuery, CreditTypeMutation
from tradeTools.schemes.creditComment import CreditCommentQuery, CreditCommentMutation
from tradeTools.schemes.lossType import LossTypeQuery, LossTypeMutation


# Assertion errors from promise when using graphene-django
# https://github.com/syrusakbary/promise/issues/57
from promise import promise
promise.async_instance.disable_trampoline()


class UserType(DjangoObjectType):
    class Meta:
        model = AuthUser


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class PricetypeType(DjangoObjectType):
    class Meta:
        model = Pricetype


class DiscountType(DjangoObjectType):
    class Meta:
        model = Discount


class UpdateCategory(graphene.Mutation):
    class Arguments:
        categoryid = graphene.Int(required=True)
        title = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    def mutate(self, info, categoryid, title):
        category = Category.objects.get(pk=categoryid)
        category.title = title
        category.save()
        return UpdateCategory(category=category)


class CreateCategory(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    def mutate(self, info, title):
        user_instance = AuthUser.objects.get(pk=info.context.user.id)
        current_time = timezone.now()
        category = Category(title=title,
                            userid=user_instance,
                            created=current_time)
        category.save()
        return CreateCategory(category=category)


class CreatePriceType(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String()
        ratio = graphene.Int(required=True)

    pricetype = graphene.Field(PricetypeType)

    def mutate(self, info, title, description, ratio):
        user_instance = AuthUser.objects.get(pk=info.context.user.id)
        current_time = timezone.now()
        pricetype = Pricetype(title=title,
                              description=description,
                              ratio=ratio,
                              userid=user_instance,
                              created=current_time)
        pricetype.save()
        return CreatePriceType(pricetype=pricetype)


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    create_pricetype = CreatePriceType.Field()


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType,
                          userid=graphene.Int(),
                          username=graphene.String(),
                          email=graphene.String(),
                          description=graphene.String())

    categories = graphene.List(CategoryType)

    pricetypes = graphene.List(PricetypeType)
    pricetype = graphene.Field(PricetypeType,
                               pricetypeid=graphene.Int(),
                               title=graphene.String())

    discounts = graphene.List(DiscountType)
    discount = graphene.Field(DiscountType,
                              discountid=graphene.Int(),
                              title=graphene.String(),
                              value=graphene.Decimal(),
                              units=graphene.String())

    def resolve_user(self, info, **kwargs):
        userid = kwargs.get('userid')
        username = kwargs.get('username')
        email = kwargs.get('email')
        description = kwargs.get('description')

        if userid is not None:
            return AuthUser.objects.get(pk=userid)

        if username is not None:
            return AuthUser.objects.get(username=username)

        if email is not None:
            return AuthUser.objects.get(email=email)

        if description is not None:
            return AuthUser.objects.get(description=description)

        return None

    def resolve_users(self, info, **kwargs):
        return AuthUser.objects.all()

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_pricetypes(self, info, **kwargs):
        return Pricetype.objects.all()

    def resolve_pricetype(self, info, **kwargs):
        pricetypeid = kwargs.get('pricetypeid')
        title = kwargs.get('title')

        if pricetypeid is not None:
            return Pricetype.objects.get(pricetypeid=pricetypeid)

        if title is not None:
            return Pricetype.objects.get(title=title)

    def resolve_discounts(self, info, **kwargs):
        return Discount.objects.all()

    def resolve_discount(self, info, **kwargs):
        discountid = kwargs.get('discountid')

        if discountid is not None:
            return Discount.objects.filter(pk=discountid)

        return None


class RootQuery(Query,
                ProductQuery,
                ProductDetailsQuery,
                ProductCommentQuery,
                DebitQuery,
                WarehouseQuery,
                CreditQuery,
                CreditDetailsQuery,
                StatusQuery,
                CreditTypeQuery,
                CreditCommentQuery,
                LossTypeQuery,
                graphene.ObjectType):
    pass


class RootMutation(Mutation,
                   JwtAuth,
                   ProductMutation,
                   ProductDetailsMutation,
                   ProductCommentMutation,
                   DebitMutation,
                   WarehouseMutation,
                   DebitComplexMutation,
                   CreditMutation,
                   CreditDetailMutation,
                   StatusMutation,
                   CreditTypeMutation,
                   CreditCommentMutation,
                   LossTypeMutation,
                   graphene.ObjectType):
    pass


schema = graphene.Schema(query=RootQuery, mutation=RootMutation)
