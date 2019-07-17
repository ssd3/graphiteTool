import graphene
from django.utils import timezone
from graphene_django import DjangoObjectType
from graphql_extensions.auth.decorators import login_required
from .models import Product, Category, AuthUser, Status, Pricetype


class UserType(DjangoObjectType):
    class Meta:
        model = AuthUser


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class StatusType(DjangoObjectType):
    class Meta:
        model = Status


class PricetypeType(DjangoObjectType):
    class Meta:
        model = Pricetype


class UpdateCategory(graphene.Mutation):
    class Arguments:
        categoryid = graphene.Int()
        title = graphene.String()

    category = graphene.Field(CategoryType)

    def mutate(self, info, categoryid, title):
        category = Category.objects.get(categoryid=categoryid)
        category.title = title
        category.save()
        return UpdateCategory(category=category)


class CreateCategory(graphene.Mutation):
    class Arguments:
        title = graphene.String()

    category = graphene.Field(CategoryType)

    def mutate(self, info, title):
        user_instance = AuthUser.objects.get(id=info.context.user.id)
        current_time = timezone.now()
        category = Category(title=title, userid=user_instance, created=current_time)
        category.save()
        return CreateCategory(category=category)


class CreateProduct(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        description = graphene.String()

    product = graphene.Field(ProductType)

    def mutate(self, info, title, description):
        user_instance = AuthUser.objects.get(id=info.context.user.id)
        current_time = timezone.now()
        category = Category.objects.get(categoryid=1)
        product = Product(categoryid=category, title=title, description=description,
                            userid=user_instance, created=current_time)
        product.save()
        return CreateProduct(product=product)


class UpdateProduct(graphene.Mutation):
    class Arguments:
        productid = graphene.Int()
        title = graphene.String()
        description = graphene.String()

    product = graphene.Field(ProductType)

    def mutate(self, info, productid, title, description):
        product = Product.objects.get(productid=productid)
        product.title = title
        product.description = description
        product.save()
        return UpdateProduct(product=product)


class CreateStatus(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        value = graphene.String()

    status = graphene.Field(StatusType)

    def mutate(self, info, title, value):
        user_instance = AuthUser.objects.get(id=info.context.user.id)
        current_time = timezone.now()
        status = Status(title=title, value=value, userid=user_instance, created=current_time)
        status.save()
        return CreateStatus(status=status)


class UpdateStatus(graphene.Mutation):
    class Arguments:
        statusid = graphene.Int()
        title = graphene.String()
        value = graphene.String()

    status = graphene.Field(StatusType)

    def mutate(self, info, statusid, title, value):
        status = Status.objects.get(statusid=statusid)
        status.title = title
        status.value = value
        status.save()
        return UpdateStatus(status=status)


class CreatePriceType(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        description = graphene.String()
        ratio = graphene.Int()

    pricetype = graphene.Field(PricetypeType)

    def mutate(self, info, title, description, ratio):
        user_instance = AuthUser.objects.get(id=info.context.user.id)
        current_time = timezone.now()
        pricetype = Pricetype(title=title, description=description, ratio=ratio,
                                userid=user_instance, created=current_time)
        pricetype.save()
        return CreatePriceType(pricetype=pricetype)


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
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
    products = graphene.List(ProductType)
    product = graphene.List(ProductType,
                             productid=graphene.Int(),
                             title=graphene.String(),
                             userid=graphene.Int(),
                             page=graphene.Int())
    categories = graphene.List(CategoryType)
    statuses = graphene.List(StatusType)
    status = graphene.Field(StatusType,
                            title=graphene.String(),
                            statusid=graphene.Int())
    pricetypes = graphene.List(PricetypeType)
    pricetype = graphene.Field(PricetypeType,
                               pricetypeid=graphene.Int(),
                               title=graphene.String())

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

    def resolve_products(self, info, **kwargs ):
        return Product.objects.all().order_by('productid')

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

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_statuses(self, info, **kwargs):
        return Status.objects.all()

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


schema = graphene.Schema(query=Query, mutation=Mutation)
