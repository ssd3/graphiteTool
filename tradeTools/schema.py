import graphene
from django.utils import timezone
from graphene_django import DjangoObjectType
from graphene import relay
# from graphql_extensions.auth.decorators import login_required
from graphql_jwt.decorators import login_required
from .models import Category, AuthUser, Status, Pricetype, Discount
from tradeTools.schemes.jwtAuth import JwtAuth
from tradeTools.schemes.product import ProductMutation, ProductQuery
from tradeTools.schemes.debit import DebitMutation, DebitQuery
from tradeTools.schemes.productDetails import ProductDetailsMutation, ProductDetailsQuery
from tradeTools.schemes.warehouse import WarehouseQuery, WarehouseMutation
from tradeTools.schemes.productComment import ProductCommentMutation, ProductCommentQuery
from tradeTools.schemes.debitComplex import DebitComplexMutation


class UserType(DjangoObjectType):
    class Meta:
        model = AuthUser


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class StatusType(DjangoObjectType):
    class Meta:
        model = Status


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


class CreateStatus(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        value = graphene.String(required=True)

    status = graphene.Field(StatusType)

    @login_required
    def mutate(self, info, title, value):
        user_instance = AuthUser.objects.get(pk=info.context.user.id)
        current_time = timezone.now()
        status = Status(title=title,
                        value=value,
                        userid=user_instance,
                        created=current_time)
        status.save()
        return CreateStatus(status=status)


class UpdateStatus(graphene.Mutation):
    class Arguments:
        statusid = graphene.Int(required=True)
        title = graphene.String(required=True)
        value = graphene.String(required=True)

    status = graphene.Field(StatusType)

    @login_required
    def mutate(self, info, statusid, title, value):
        status = Status.objects.get(pk=statusid)
        status.title = title
        status.value = value
        status.save()
        return UpdateStatus(status=status)


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
    create_status = CreateStatus.Field()
    update_status = UpdateStatus.Field()
    create_pricetype = CreatePriceType.Field()


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType,
                          userid=graphene.Int(),
                          username=graphene.String(),
                          email=graphene.String(),
                          description=graphene.String())

    categories = graphene.List(CategoryType)

    statuses = graphene.List(StatusType)
    status = graphene.Field(StatusType,
                            title=graphene.String(),
                            statusid=graphene.Int())

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

    @login_required
    def resolve_statuses(self, info, **kwargs):
        return Status.objects.all()

    @login_required
    def resolve_status(self, info, **kwargs):
        title = kwargs.get('title')
        statusid = kwargs.get('statusid')

        if title is not None:
            return Status.objects.get(title=title)

        if statusid is not None:
            return Status.objects.get(statusid=statusid)

        return None

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
                   graphene.ObjectType):
    pass


schema = graphene.Schema(query=RootQuery, mutation=RootMutation)
