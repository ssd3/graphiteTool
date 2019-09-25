import graphene
from django.db.models import Q
from django.utils import timezone
from graphene_django import DjangoObjectType
from graphene import relay
from tradeTools.models import *
from graphene_django.filter import DjangoFilterConnectionField


class WarehouseType(DjangoObjectType):
    class Meta:
        model = Warehouse
        filter_fields = {'title': ['exact', 'icontains', 'istartswith']}
        interfaces = (relay.Node,)


class WarehouseConnection(relay.Connection):
    class Meta:
        node = WarehouseType


class CreateWarehouse(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String()
        active = graphene.Boolean(required=True)
        incoming = graphene.Boolean(required=True)
        outgoing = graphene.Boolean(required=True)

    warehouse = graphene.Field(WarehouseType)

    def mutate(self, info, **kwargs):
        user_instance = AuthUser.objects.get(pk=info.context.user.id)
        current_time = timezone.now()

        warehouse = Warehouse(title=kwargs.get("title"),
                              description=kwargs.get("description", None),
                              active=kwargs.get("active"),
                              userid=user_instance,
                              created=current_time,
                              incoming=kwargs.get("incoming"),
                              outgoing=kwargs.get("outgoing"))
        warehouse.save()
        return CreateWarehouse(warehouse=warehouse)


class UpdateWarehouse(graphene.Mutation):
    class Arguments:
        warehouseid = graphene.Int(required=True)
        title = graphene.String(required=True)
        description = graphene.String()
        active = graphene.Boolean(required=True)
        incoming = graphene.Boolean(required=True)
        outgoing = graphene.Boolean(required=True)

    warehouse = graphene.Field(WarehouseType)

    def mutate(self, info, **kwargs):
        warehouse = Warehouse.objects.get(pk=kwargs.get("warehouseid"))
        warehouse.title = kwargs.get("title")
        warehouse.description = kwargs.get("description", None)
        warehouse.active = kwargs.get("active")
        warehouse.incoming = kwargs.get("incoming")
        warehouse.outgoing = kwargs.get("outgoing")
        warehouse.save()
        return UpdateWarehouse(warehouse=warehouse)


class WarehouseMutation(graphene.ObjectType):
    create_warehouse = CreateWarehouse.Field()
    update_warehouse = UpdateWarehouse.Field()


class WarehouseQuery(graphene.ObjectType):
    warehouses = DjangoFilterConnectionField(WarehouseType,
                                             active=graphene.Boolean(),
                                             incoming=graphene.Boolean(),
                                             outgoing=graphene.Boolean())

    warehouse = graphene.List(WarehouseType,
                              warehouseid=graphene.Int(),
                              title=graphene.String(),
                              active=graphene.Boolean(),
                              incoming=graphene.Boolean(),
                              outgoing=graphene.Boolean())

    def resolve_warehouses(self, info, **kwargs):
        active = kwargs.get('active')
        incoming = kwargs.get('incoming')
        outgoing = kwargs.get('outgoing')

        if active is True and incoming is True:
            return Warehouse.objects.filter(Q(active=active, incoming=incoming))

        if active is True and outgoing is True:
            return Warehouse.objects.filter(Q(active=active, outgoing=outgoing))

        if None in (active, incoming, outgoing):
            return Warehouse.objects.all()

    def resolve_warehouse(self, info, **kwargs):
        for key, value in kwargs.items():
            if value is not None:
                warehouse = {key: value}
                return Warehouse.objects.filter(**warehouse)

        return None

        """
        warehouseid = kwargs.get('warehouseid')
        title = kwargs.get('title')
        active = kwargs.get('active')
        in_field = kwargs.get('in_field')
        out = kwargs.get('out')
        
        if warehouseid is not None:
            return Warehouse.objects.filter(pk=warehouseid)

        if title is not None:
            return Warehouse.objects.filter(title=title)

        if active is not None:
            return Warehouse.objects.filter(active=active)

        if in_field is not None:
            return Warehouse.objects.filter(in_field=in_field)

        if out is not None:
            return Warehouse.objects.filter(out=out)
        
        return None
        """
