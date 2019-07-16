import graphene
from django.utils import timezone
from graphene_django import DjangoObjectType
from graphql_extensions.auth.decorators import login_required
from .models import Product, Category, AuthUser


class UserType(DjangoObjectType):
    class Meta:
        model = AuthUser


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


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


class CategoryMutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType,
                          userid=graphene.Int(),
                          username=graphene.String(),
                          email=graphene.String(),
                          description=graphene.String())

    products = graphene.List(ProductType)
    categories = graphene.List(CategoryType)

    @login_required
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

    @login_required
    def resolve_products(self, info, **kwargs):
        return Product.objects.all().order_by('-productid')


    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()


schema = graphene.Schema(query=Query, mutation=CategoryMutation)
