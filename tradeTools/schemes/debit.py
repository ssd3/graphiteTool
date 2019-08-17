import graphene
from graphene_django import DjangoObjectType
from graphene import relay
from tradeTools.libs.common_db import *
from graphene_django.filter import DjangoFilterConnectionField
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from graphene import Connection
from tradeTools.libs.total_count import ExtendedConnection

'''
# django-filters expr
exact
iexact
contains
icontains
in
gt
gte
lt
lte
startswith
istartswith
endswith
iendswith
range
year
month
day
week_day
isnull
search
regex
iregex
'''

class DebitType(DjangoObjectType):
    class Meta:
        model = Debit
        filter_fields = {
            'warehouseid': ['exact', 'in'],
            'qty': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'tracknumber': ['icontains']
        }
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection


class DebitConnection(relay.Connection):
    class Meta:
        node = DebitType


class CreateDebit(graphene.Mutation):
    class Arguments:
        warehouseid = graphene.Int(required=True)
        productid = graphene.Int(required=True)
        qty = graphene.Decimal(required=True)
        price = graphene.Decimal(required=True)
        pricetypeid = graphene.Int(required=True)
        discountid = graphene.Int(required=True)
        tracknumber = graphene.String(required=True)
        statusid = graphene.Int(required=True)
        notes = graphene.String()

    debit = graphene.Field(DebitType)

    def mutate(self, info, **kwargs):
        debit = create_debit(info, kwargs)
        return CreateDebit(debit=debit)


class UpdateDebit(graphene.Mutation):
    class Arguments:
        debitid = graphene.Int(required=True)
        warehouseid = graphene.Int(required=True)
        productid = graphene.Int(required=True)
        qty = graphene.Decimal(required=True)
        price = graphene.Decimal(required=True)
        pricetypeid = graphene.Int(required=True)
        discountid = graphene.Int(required=True)
        tracknumber = graphene.String(required=True)
        statusid = graphene.Int(required=True)
        notes = graphene.String()

    debit = graphene.Field(DebitType)

    def mutate(self, info, **kwargs):
        debit = update_debit(kwargs)
        debit.save()
        return UpdateDebit(debit=debit)


class UpdateDebitStatusID(graphene.Mutation):
    class Arguments:
        debitid = graphene.List(graphene.Int)
        statusid = graphene.Int()

    debit = graphene.List(DebitType)

    def mutate(self, info, **kwargs):
        debit = update_debit_statusid(kwargs)
        return UpdateDebitStatusID(debit=debit)


class DebitMutation(graphene.ObjectType):
    create_debit = CreateDebit.Field()
    update_debit = UpdateDebit.Field()
    update_debit_statusid = UpdateDebitStatusID.Field()



class DebitQuery(graphene.ObjectType):
    '''
    debits = relay.ConnectionField(DebitConnection,
                                   debitid=graphene.Int(),
                                   warehouseid=graphene.Int(),
                                   productid=graphene.Int(),
                                   qty=graphene.Decimal(),
                                   qty_expr=graphene.String(),
                                   price=graphene.Decimal(),
                                   price_expr=graphene.String(),
                                   pricetypeid=graphene.Int(),
                                   discountid=graphene.Int(),
                                   tracknumber=graphene.String(),
                                   statusid=graphene.Int(),
                                   notes=graphene.String(),
                                   userid=graphene.Int(),
                                   created=graphene.DateTime(),
                                   created_expr=graphene.String())
'''
    debits_bytext = DjangoFilterConnectionField(DebitType,
                                                search_text=graphene.String(),
                                                page_num=graphene.Int(),
                                                rows_count=graphene.Int())

    debits = DjangoFilterConnectionField(DebitType)
    debit = graphene.Field(DebitType, debitid=graphene.Int())

    def resolve_debits_bytext(self, info, **kwargs):
        search_text = kwargs.get('search_text')
        page_num = kwargs.get('page_num')
        rows_count = kwargs.get('rows_count')

        debits_to = page_num * rows_count
        debits_from = debits_to - rows_count

        if search_text == "" or None:
            return Debit.objects.all().order_by('-debitid')


        products = Product.objects.filter(Q(title__icontains=search_text) | Q(description__icontains=search_text))
        product_details = Productdetails.objects.filter(Q(model__icontains=search_text))
        product_comments = Productcomment.objects.filter(Q(comment__icontains=search_text))
        warehouses = Warehouse.objects.filter(Q(title__icontains=search_text) | Q(description__icontains=search_text))
        pricetype = Pricetype.objects.filter(Q(title__icontains=search_text) | Q(description__icontains=search_text))
        discount = Discount.objects.filter(Q(title__icontains=search_text))
        status = Status.objects.filter(Q(title__icontains=search_text))
        user = AuthUser.objects.filter(Q(username__icontains=search_text))

        query_var = (Q(productid__in=products) |
                     Q(productid__productdetails__in=product_details) |
                     Q(productid__productcomment__in=product_comments) |
                     Q(warehouseid__in=warehouses) |
                     Q(pricetypeid__in=pricetype) |
                     Q(discountid__in=discount) |
                     Q(statusid__in=status) |
                     Q(userid__in=user) |
                     Q(tracknumber__icontains=search_text) |
                     Q(notes__icontains=search_text))

        debits = Debit.objects.filter(query_var).order_by('-debitid')[debits_from:debits_to]
        return Debit.objects.filter(pk__in=debits)

    def resolve_debits(self, info, **kwargs):
        return Debit.objects.all()

    @staticmethod
    def resolve_debit(self, info, **kwargs):
        debitid = kwargs.get('debitid')

        if debitid is not None:
            return Debit.objects.get(pk=debitid)

        return None

'''
    @staticmethod
    def resolve_debits(self, info, **kwargs):
        kwargs.pop('before', None)
        kwargs.pop('after', None)
        kwargs.pop('last', None)
        kwargs.pop('first', None)

        # filter expressions here such as gt gte lt lte etc
        qty_expr = kwargs.get('qty_expr', None)  # additional to qty field (qty gt 2.0)
        price_expr = kwargs.get('price_expr', None)
        created_expr = kwargs.get('created_expr', None)

        kwargs.pop('qty_expr', None)
        kwargs.pop('price_expr', None)
        kwargs.pop('created_expr', None)

        if len(kwargs) > 0:
            return Debit.objects.filter(**kwargs)

        return Debit.objects.all()
'''