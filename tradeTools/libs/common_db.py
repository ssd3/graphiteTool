from django.utils import timezone
from tradeTools.models import *


def create_product(info, data):
    product = Product(categoryid=Category.objects.get(pk=data.get("categoryid")),
                      title=data.get("title"),
                      description=data.get("description", None),
                      userid=AuthUser.objects.get(pk=info.context.user.id),
                      created=timezone.now())
    product.save()
    return product


def update_product(data):
    product = Product.objects.get(pk=data.get("productid"))
    product.categoryid = Category.objects.get(pk=data.get("categoryid"))
    product.title = data.get("title")
    product.description = data.get("description", None)

    product.save()
    return product


def create_productdetails(info, data):
    productdetails = Productdetails(productid=Product.objects.get(pk=data.get("productid")),
                                    model=data.get("model", None),
                                    url=data.get("url", None),
                                    serialno=data.get("serialno", None),
                                    weight=data.get("weight", 0.0),
                                    height=data.get("height", 0.0),
                                    width=data.get("width", 0.0),
                                    lenght=data.get("lenght", 0.0),
                                    userid=AuthUser.objects.get(pk=info.context.user.id),
                                    created=timezone.now())
    productdetails.save()
    return productdetails


def update_productdetails(data):
    productdetails = Productdetails.objects.get(pk=data.get("productdetailsid"))
    productdetails.productid = Product.objects.get(pk=data.get("productid"))
    productdetails.model = data.get("model", None)
    productdetails.url = data.get("url", None)
    productdetails.serialno = data.get("serialno", None)
    productdetails.weight = data.get("weight", 0.0)
    productdetails.height = data.get("height", 0.0)
    productdetails.width = data.get("width", 0.0)
    productdetails.lenght = data.get("lenght", 0.0)

    productdetails.save()
    return productdetails


def create_productcomment(info, data):
    productcomment = Productcomment(productid=Product.objects.get(pk=data.get("productid")),
                                    comment=data.get("comment"),
                                    userid=AuthUser.objects.get(pk=info.context.user.id),
                                    created=timezone.now())
    productcomment.save()
    return productcomment


def update_productcomment(data):
    productcomment = Productcomment.objects.get(pk=data.get("productcommentid"))
    productcomment.comment = data.get("comment")

    productcomment.save()
    return productcomment


def create_debit(info, data):
    debit = Debit(warehouseid=Warehouse.objects.get(pk=data.get("warehouseid")),
                  productid=Product.objects.get(pk=data.get("productid")),
                  qty=data.get("qty", 0.00),
                  price=data.get("price", 0.00),
                  pricetypeid=Pricetype.objects.get(pk=data.get("pricetypeid")),
                  discountid=Discount.objects.get(pk=data.get("discountid")),
                  tracknumber=data.get("tracknumber"),
                  statusid=Status.objects.get(pk=data.get("statusid")),
                  notes=data.get("notes", None),
                  userid=AuthUser.objects.get(pk=info.context.user.id),
                  created=timezone.now())

    debit.save()
    return debit


def update_debit(data):
    debit = Debit.objects.get(pk=data.get("debitid"))
    debit.warehouseid = Warehouse.objects.get(pk=data.get("warehouseid"))
    debit.productid = Product.objects.get(pk=data.get("productid"))
    debit.pricetypeid = Pricetype.objects.get(pk=data.get("pricetypeid"))
    debit.discountid = Discount.objects.get(pk=data.get("discountid"))
    debit.statusid = Status.objects.get(pk=data.get("statusid"))
    debit.qty = data.get("qty")
    debit.price = data.get("price")
    debit.tracknumber = data.get("tracknumber")
    debit.notes = data.get("notes", None)

    debit.save()
    return debit


def create_credit(info, data):
    credit = Credit(credittypeid=Credittype.objects.get(pk=data.get('credittypeid')),
                    buyerid=AuthUser.objects.get(pk=info.context.user.id),
                    fromwarehouseid=Warehouse.objects.get(pk=data.get('fromwarehouseid')),
                    userid=AuthUser.objects.get(pk=info.context.user.id),
                    towarehouseid=Warehouse.objects.get(pk=data.get('towarehouseid')),
                    created=timezone.now(),
                    sent=data.get('sent'),
                    received=data.get('received'))

    credit.save()
    return credit

def update_credit(data):
    credit = Credit.objects.get(pk=data.get('creditid'))
    credit.credittypeid = Credittype.objects.get(pk=data.get('credittypeid'))
    credit.buyerid = data.get('buyerid')
    credit.fromwarehouseid = Warehouse.objects.get(pk=data.get('fromwarehouseid'))
    credit.towarehouseid = Warehouse.objects.get(pk=data.get('towarehouseid'))

    credit.save()
    return credit

def create_creditdetail(info, data):
    creditdetail = Creditdetails(creditid=Credit.objects.get(pk=data.get('creditid')),
                                 productid=Product.objects.get(pk=data.get('productid')),
                                 price=data.get('price', 0.00),
                                 qty=data.get('qty', 0.00),
                                 pricetypeid=Pricetype.objects.get(pk=data.get('pricetypeid')),
                                 userid=AuthUser.objects.get(pk=info.context.user.id),
                                 created=timezone.now())

    creditdetail.save()
    return creditdetail

def update_creditdetail(data):
    creditdetail = Creditdetails.objects.get(pk=data.get('creditdetailid'))
    creditdetail.creditid = Credit.objects.get(pk=data.get('creditid'))
    creditdetail.productid = Product.objects.get(pk=data.get('productid'))
    creditdetail.price = data.get('price')
    creditdetail.qty = data.get('qty')
    creditdetail.pricetypeid = Pricetype.objects.get(pk=data.get('pricetypeid'))

    creditdetail.save()
    return creditdetail
