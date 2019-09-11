# create credit complex
```
mutation CREATE_CREDIT_COMPLEX 
(
  $credittypeid: Int!,
  $buyerid: Int!,
	$fromwarehouseid: Int!,
  $towarehouseid: Int!,
  $tracknumber: String,
  $creditdetails: [CreditDetailInput]!,
  $creditlosses: [CreditLossInput],
  $comment: String
)
{
  result: createCreditcomplex
  (
    creditData: {
      credittypeid: $credittypeid,
      buyerid: $buyerid,
      fromwarehouseid: $fromwarehouseid,
      towarehouseid: $towarehouseid,
      tracknumber: $tracknumber
    }
    creditlossData: {
      creditlosses: $creditlosses
    }
    creditdetailsData: {
      creditdetails: $creditdetails
    }
    creditcommentData: {
      comment: $comment
    }
  )
  {
    credit {
      creditid
      credittype: credittypeid {
        credittypeid
        title
      }
      buyerid
      fromwarehouseid
      towarehouseid
      sent
      received
      tracknumber
    }
    creditlosses {
      creditlossid
      losstypeid {
        losstypeid
        title
      }
      rate
      notes
    }
    creditdetails {
      creditdetailsid
      debit: debitid {
        debitid
        qty: qty
        price: price
        pricetype: pricetypeid {
          pricetypeid
          title
          ratio
        }
        discount: discountid {
          discountid
          title
          rate
          units
        }
      }
      product: productid {
        productid
        title
      }
      price: price
      qty: qty
      pricetype: pricetypeid {
        pricetypeid
        title
        ratio
      }
    }
    creditcomment {
      creditcommentid
      comment
    }
  }
}
```

# variables create credit complex
```
{
  "credittypeid": 1,
  "buyerid": 2,
  "fromwarehouseid": 2,
  "towarehouseid": 1,
  "tracknumber": "xxx-yyy-zzz",
  "creditlosses": [
    {
      "losstypeid": 1,
      "rate": 1.5,
      "notes": "notes 1"
    },
    {
      "losstypeid": 2,
      "rate": 2.5,
      "notes": "notes 2"
    }
  ],
  "creditdetails": [
    {
      "debitid": 62,
      "productid": 89,
      "price": 10.2,
      "qty": 1.0,
      "pricetypeid": 1
    },
    {
      "debitid": 65,
      "productid": 92,
      "price": 10.2,
      "qty": 1.0,
      "pricetypeid": 1
    }
  ],
  "comment": "comment 14"
}
```

#update credit complex
```
mutation UPDATE_CREDIT_COMPLEX 
(
  $creditid: Int!,
  $credittypeid: Int!,
  $buyerid: Int!,
	$fromwarehouseid: Int!,
  $towarehouseid: Int!,
  $tracknumber: String,
  $sent: DateTime,
  $received: DateTime,
  $creditdetails: [CreditDetailUpdateInput]!,
  $creditlosses: [CreditLossUpdateInput],
  $creditcommentid: Int!,
  $creditcomment: String
)
{
  result: updateCreditcomplex
  (
    creditData: {
      creditid: $creditid,
      credittypeid: $credittypeid,
      buyerid: $buyerid,
      fromwarehouseid: $fromwarehouseid,
      towarehouseid: $towarehouseid,
      tracknumber: $tracknumber,
      sent: $sent,
      received: $received
    }
    creditlossData: {
      creditlosses: $creditlosses
    }
    creditdetailsData: {
      creditdetails: $creditdetails
    }
    creditcommentData: {
      creditcommentid: $creditcommentid,
      comment: $creditcomment
    }
  )
  {
    credit {
      creditid
      credittype: credittypeid {
        credittypeid
        title
      }
      buyerid
      fromwarehouseid
      towarehouseid
      sent
      received
      tracknumber
    }
    creditlosses {
      creditlossid
      losstypeid {
        losstypeid
        title
      }
      rate
      notes
    }
    creditdetails {
      creditdetailsid
      debit: debitid {
        debitid
        qty: qty
        price: price
        pricetype: pricetypeid {
          pricetypeid
          title
          ratio
        }
        discount: discountid {
          discountid
          title
          rate
          units
        }
      }
      product: productid {
        productid
        title
      }
      price: price
      qty: qty
      pricetype: pricetypeid {
        pricetypeid
        title
        ratio
      }
    }
    creditcomment {
      creditcommentid
      comment
    }
  }
}
```
#update credit complex variables
```
{
  "creditid": 81,
  "credittypeid": 2,
  "buyerid": 2,
  "fromwarehouseid": 2,
  "towarehouseid": 1,
  "tracknumber": "xxx-yyy-zzz",
  "sent": "2019-09-11T15:35:37.495Z",
  "creditlosses": [
    {
      "creditid": 81,
      "creditlossid": 116,
      "losstypeid": 2,
      "rate": 1,
      "notes": null
    },
    {
      "creditid": 81,
      "creditlossid": 117,
      "losstypeid": 3,
      "rate": 1,
      "notes": null
    },
    {
      "creditid": 81,
      "losstypeid": 1,
      "rate": 1,
      "notes": "other"
    }
  ],
  "creditdetails": [
    {
      "creditid": 81,
      "debitid": 64,
      "productid": 91,
      "price": 1500,
      "qty": 1,
      "pricetypeid": 1
    },
    {
      "creditdetailsid": 98,
      "creditid": 81,
      "debitid": 65,
      "productid": 92,
      "price": 15.8,
      "qty": 1,
      "pricetypeid": 1
    }
  ],
  "creditcommentid": 72,
  "creditcomment": "comment xxx-yyy-zzz"
}
```