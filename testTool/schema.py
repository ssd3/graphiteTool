import graphene
from graphene_django import DjangoObjectType
from .models import TestCategory


class TestCategoryType(DjangoObjectType):
    class Meta:
        model = TestCategory


class Query(graphene.ObjectType):
    testcategories = graphene.List(TestCategoryType)

    def resolve_testcategories(self, info, **kwargs):
        return TestCategory.objects.all()
