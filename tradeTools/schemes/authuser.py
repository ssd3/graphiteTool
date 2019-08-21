import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from tradeTools.models import AuthUser
from tradeTools.libs.total_count import ExtendedConnection


class AuthUserType(DjangoObjectType):
    class Meta:
        model = AuthUser
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection


class AuthUserConnection(relay.Connection):
    class Meta:
        node = AuthUserType


class AuthUserQuery(graphene.ObjectType):
    users = DjangoFilterConnectionField(AuthUserType)

    def resolve_staff(self, info, **kwargs):
        querySet = Q(is_staff=True) & Q(is_active=True)
        return AuthUser.objects.filter(querySet)
