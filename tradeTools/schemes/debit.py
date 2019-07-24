import graphene
from django.utils import timezone
from graphene_django import DjangoObjectType
from graphene import relay
from tradeTools.models import *

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
        filter_fields = ['qty_expr', 'price_expr', 'created_expr']
        interface = (relay.Node, )


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
        warehouse = Warehouse.objects.get(pk=kwargs.get("warehouseid"))
        product = Product.objects.get(pk=kwargs.get("productid"))
        pricetype = Pricetype.objects.get(pk=kwargs.get("pricetypeid"))
        discount = Discount.objects.get(pk=kwargs.get("discountid"))
        status = Status.objects.get(pk=kwargs.get("statusid"))
        user = AuthUser.objects.get(pk=info.context.user.id)
        created = timezone.now()

        debit = Debit(warehouseid=warehouse,
                      productid=product,
                      qty=kwargs.get("qty", 0.00),
                      price=kwargs.get("price", 0.00),
                      pricetypeid=pricetype,
                      discountid=discount,
                      tracknumber=kwargs.get("tracknumber"),
                      statusid=status,
                      notes=kwargs.get("notes", None),
                      userid=user,
                      created=created)

        debit.save()
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
        debit = Debit.objects.get(pk=kwargs.get("debitid"))
        debit.warehouseid = Warehouse.objects.get(pk=kwargs.get("warehouseid"))
        debit.productid = Product.objects.get(pk=kwargs.get("productid"))
        debit.pricetypeid = Pricetype.objects.get(pk=kwargs.get("pricetypeid"))
        debit.discountid = Discount.objects.get(pk=kwargs.get("discountid"))
        debit.statusid = Status.objects.get(pk=kwargs.get("statusid"))
        debit.qty = kwargs.get("qty")
        debit.price = kwargs.get("price")
        debit.tracknumber = kwargs.get("tracknumber")
        debit.notes = kwargs.get("notes", None)

        debit.save()
        return UpdateDebit(debit=debit)


class DebitMutation(graphene.ObjectType):
    create_debit = CreateDebit.Field()
    update_debit = UpdateDebit.Field()


class DebitQuery(graphene.ObjectType):
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

    debit = graphene.Field(DebitType,
                           debitid=graphene.Int())

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

    @staticmethod
    def resolve_debit(self, info, **kwargs):
        debitid = kwargs.get('debitid')

        if debitid is not None:
            return Debit.objects.get(pk=debitid)

        return None
