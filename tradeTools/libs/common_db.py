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
                    buyerid=AuthUser.objects.get(pk=data.get('buyerid')).id,
                    fromwarehouseid=Warehouse.objects.get(pk=data.get('fromwarehouseid')).warehouseid,
                    userid=AuthUser.objects.get(pk=info.context.user.id),
                    towarehouseid=Warehouse.objects.get(pk=data.get('towarehouseid')).warehouseid,
                    created=timezone.now(),
                    sent=data.get('sent'),
                    received=data.get('received'),
                    tracknumber=data.get('tracknumber'))

    credit.save()
    return credit


def update_credit(info, data):
    credit = Credit.objects.get(pk=data.get('creditid'))
    credit.credittypeid = Credittype.objects.get(pk=data.get('credittypeid'))
    credit.buyerid = AuthUser.objects.get(pk=data.get('buyerid')).id
    credit.fromwarehouseid = Warehouse.objects.get(pk=data.get('fromwarehouseid')).warehouseid
    credit.towarehouseid = Warehouse.objects.get(pk=data.get('towarehouseid')).warehouseid
    credit.tracknumber = data.get('tracknumber')
    credit.sent = data.get("sent")
    credit.received = data.get("received")

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


def create_creditdetails(info, data, credit):
    creditdetails = []
    for creditdetail in data:
        creditdetail = Creditdetails(creditid=credit,
                                     debitid=Debit.objects.get(pk=creditdetail.get('debitid')),
                                     productid=Product.objects.get(pk=creditdetail.get('productid')),
                                     price=creditdetail.get('price', 0.00),
                                     qty=creditdetail.get('qty', 0.00),
                                     pricetypeid=Pricetype.objects.get(pk=creditdetail.get('pricetypeid')),
                                     userid=AuthUser.objects.get(pk=info.context.user.id),
                                     created=timezone.now())

        creditdetail.save()
        creditdetails.append(creditdetail)
    return creditdetails


def update_creditdetails(info, data, credit):
    creditdetails = []
    for creditdetail in data:
        tmp_creditdetail = None
        if 'creditdetailsid' in creditdetail:
            tmp_creditdetail = Creditdetails.objects.get(pk=creditdetail.get('creditdetailsid'))
        if tmp_creditdetail is None:
            creditdetail.creditid = credit.creditid
            tmp_creditdetail = create_creditdetail(info, creditdetail)
        else:
            tmp_creditdetail = update_creditdetail(creditdetail)
        creditdetails.append(tmp_creditdetail)
    return creditdetails


def update_creditdetail(data):
    creditdetail = Creditdetails.objects.get(pk=data.get('creditdetailsid'))
    creditdetail.debitid = Debit.objects.get(pk=data.get('debitid'))
    creditdetail.creditid = Credit.objects.get(pk=data.get('creditid'))
    creditdetail.productid = Product.objects.get(pk=data.get('productid'))
    creditdetail.price = data.get('price')
    creditdetail.qty = data.get('qty')
    creditdetail.pricetypeid = Pricetype.objects.get(pk=data.get('pricetypeid'))

    creditdetail.save()
    return creditdetail


def create_status(info, data):
    status = Status(title=data.get('title'),
                    color=data.get('color'),
                    userid=AuthUser.objects.get(pk=info.context.user.id),
                    created=timezone.now())

    status.save()
    return status


def update_status(data):
    status = Status.objects.get(pk=data.get('statusid'))
    status.title = data.get('title')
    status.color = data.get('color')

    status.save()
    return status


def update_debit_statusid(data):
    Debit.objects.filter(pk__in=data.get('debitid')).update(statusid=Status.objects.get(pk=data.get('statusid')))
    debits = Debit.objects.filter(pk__in=data.get('debitid'))
    return debits


def create_credittype(info, data):
    credittype = Credittype(title=data.get('title'),
                            description=data.get('description'),
                            userid=AuthUser.objects.get(pk=info.context.user.id),
                            created=timezone.now())
    credittype.save()
    return credittype


def update_credittype(data):
    credittype = Credittype.objects.get(pk=data.get('credittypeid'))
    credittype.title = data.get('title')
    credittype.description = data.get('description')

    credittype.save()
    return credittype


def create_creditcomment(info, data, credit=None):
    creditid = None
    if credit is None:
        creditid = Credit.objects.get(pk=data.get('creditid'))
    else:
        creditid = credit

    creditcomment = Creditcomment(creditid=creditid,
                                  comment=data.get('comment'),
                                  userid=AuthUser.objects.get(pk=info.context.user.id),
                                  created=timezone.now())
    creditcomment.save()
    return creditcomment


def update_creditcomment(data):
    creditcomment = Creditcomment.objects.get(pk=data.get('creditcommentid'))
    creditcomment.comment = data.get('comment')

    creditcomment.save()
    return creditcomment


def create_losstype(info, data):
    losstype = Losstype(title=data.get('title'),
                        userid=AuthUser.objects.get(pk=info.context.user.id),
                        created=timezone.now())
    losstype.save()
    return losstype


def update_losstype(data):
    losstype = Losstype.objects.get(pk=data.get('losstypeid'))
    losstype.title = data.get('title')

    losstype.save()
    return losstype


def create_creditloss(info, data):
    creditloss = Creditloss(creditid=Credit.objects.get(pk=data.get('creditid')),
                            losstypeid=Losstype.objects.get(pk=data.get('losstypeid')),
                            rate=data.get('rate'),
                            notes=data.get('notes'),
                            userid=AuthUser.objects.get(pk=info.context.user.id),
                            created=timezone.now())
    creditloss.save()
    return creditloss


def create_creditlosses(info, data, credit):
    creditlosses = []
    for creditloss in data:
        tmp_creditloss = Creditloss(creditid=credit,
                                    losstypeid=Losstype.objects.get(pk=creditloss.get('losstypeid')),
                                    rate=creditloss.get('rate'),
                                    notes=creditloss.get('notes'),
                                    userid=AuthUser.objects.get(pk=info.context.user.id),
                                    created=timezone.now())
        tmp_creditloss.save()
        creditlosses.append(tmp_creditloss)
    return creditlosses


def update_creditlosses(info, data, credit):
    creditlosses = []
    for creditloss in data:
        tmp_creditloss = None
        if 'creditlossid' in creditloss:
            tmp_creditloss = Creditloss.objects.get(pk=creditloss.get('creditlossid'))
        if tmp_creditloss is None:
            creditloss.creditid = credit.creditid
            tmp_creditloss = create_creditloss(info, creditloss)
        else:
            tmp_creditloss = update_creditloss(creditloss)
        creditlosses.append(tmp_creditloss)
    return creditlosses


def update_creditloss(data):
    creditloss = Creditloss.objects.get(pk=data.get('creditlossid'))
    creditloss.losstypeid = Losstype.objects.get(pk=data.get('losstypeid'))
    creditloss.rate = data.get('rate')
    creditloss.notes = data.get('notes')

    creditloss.save()
    return creditloss
