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
      product: productid {
        productid
        title
      }
      creditprice: price
      creditqty: qty
      creditpricetype: pricetypeid {
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
      "productid": 71,
      "price": 10.2,
      "qty": 1.0,
      "pricetypeid": 1
    },
    {
      "productid": 72,
      "price": 10.2,
      "qty": 1.0,
      "pricetypeid": 1
    }
  ],
  "comment": "comment 14"
}
```