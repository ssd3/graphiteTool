import graphene
from graphene_django import DjangoObjectType
from graphene import relay
from tradeTools.libs.common_db import *
from graphene_django.filter import DjangoFilterConnectionField
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from graphene import Connection

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

'''
TotalCount doesn't work like in products because debit uses DjangoFilterConnectionField (not relay.Connection)
TotalCount works with adding following class below
'''
class TotalCountConnection(Connection):
    class Meta:
        abstract = True

    total_count = graphene.Int()

    def resolve_total_count(root, info, **kwargs):
        return root.length


class DebitType(DjangoObjectType):
    class Meta:
        model = Debit
        filter_fields = {
            'warehouseid': ['exact', 'in'],
            'qty': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'notes': ['icontains']
        }
        interfaces = (relay.Node, )
        connection_class = TotalCountConnection


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
        return UpdateDebit(debit=debit)


class DebitMutation(graphene.ObjectType):
    create_debit = CreateDebit.Field()
    update_debit = UpdateDebit.Field()


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
                                                search_text=graphene.String())
    debits = DjangoFilterConnectionField(DebitType)
    debit = graphene.Field(DebitType, debitid=graphene.Int())

    def resolve_debits_bytext(self, info, **kwargs):
        search_text = kwargs.get('search_text')
        debits_ids = []

        for debit in Debit.objects.all():
            try:
                if search_text in debit.tracknumber:
                    debits_ids.append(debit.debitid)
                    continue

                if debit.notes:
                    if search_text in debit.notes:
                        debits_ids.append(debit.debitid)
                        continue

                product = Product.objects.filter(productid=debit.productid_id)
                if product.filter(Q(title__icontains=search_text) | Q(description__icontains=search_text)):
                    debits_ids.append(debit.debitid)
                    continue

                product_details = Productdetails.objects.filter(productid=debit.productid_id)
                if product_details.filter(Q(model__icontains=search_text)):
                    debits_ids.append(debit.debitid)
                    continue

                product_comments = Productcomment.objects.filter(productid=debit.productid_id)
                if product_comments.filter(Q(comment__icontains=search_text)):
                    debits_ids.append(debit.debitid)
                    continue

                warehouse = Warehouse.objects.filter(warehouseid=debit.warehouseid_id)
                if warehouse.filter(Q(title__icontains=search_text) | Q(description__icontains=search_text)):
                    debits_ids.append(debit.debitid)
                    continue

                pricetype = Pricetype.objects.filter(pricetypeid=debit.pricetypeid_id)
                if pricetype.filter(Q(title__icontains=search_text) | Q(description__icontains=search_text)):
                    debits_ids.append(debit.debitid)
                    continue

                discount = Discount.objects.filter(discountid=debit.discountid_id)
                if discount.filter(Q(title__icontains=search_text)):
                    debits_ids.append(debit.debitid)
                    continue

                status = Status.objects.filter(statusid=debit.statusid_id)
                if status.filter(Q(title__icontains=search_text)):
                    debits_ids.append(debit.debitid)
                    continue

                user = AuthUser.objects.filter(id=debit.userid_id)
                if user.filter(Q(username__icontains=search_text)):
                    debits_ids.append(debit.debitid)
                    continue

            except ObjectDoesNotExist:
                print(ObjectDoesNotExist)

        return Debit.objects.filter(pk__in=debits_ids)

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