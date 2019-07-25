# CreateDebitComplex (Product + ProductDetails + ProductComment + Debit)
```
mutation CreateDebitComplex
(
  $categoryid: Int!,
  $title: String!,
  $description: String,
  $model: String,
  $url: String,
  $serialno: String,
  $weight: Decimal,
  $height: Decimal,
  $width: Decimal,
  $length: Decimal,
  $comment: String,
  $warehouseid: Int!,
  $qty: Decimal!,
  $price: Decimal!,
  $pricetypeid: Int!,
  $discountid: Int!,
  $tracknumber: String!,
  $statusid: Int!,
  $notes: String
)
{
  createDebitcomplex(
    productData: {
      categoryid: $categoryid,
      title: $title,
      description: $description
    }
    productdetailsData: {
      model: $model,
      url: $url,
      serialno: $serialno,
      weight: $weight,
      height: $height,
      width: $width,
      length: $length
    }
    productcommentData: {
      comment: $comment
    }
    debitData: {
      warehouseid: $warehouseid,
			qty: $qty,
      price: $price,
      pricetypeid: $pricetypeid,
      discountid: $discountid,
      tracknumber: $tracknumber,
      statusid: $statusid,
      notes: $notes
    }
  )
  {
    product
    {
      productid
      categoryid{
        categoryid
        title
      }
      title
      description
    }
    productdetails {
      productdetailsid
      model
      url
      serialno
      weight
      height
      width
      length
    }
    productcomment{
      productcommentid
      comment
    }
    debit
    {
      debitid
      warehouseid{
        warehouseid
      }
      tracknumber
    }
  }
}
```

# CreateDebitComplex (Product + ProductDetails + ProductComment + Debit) variables
```
{
  "categoryid": 1,
  "title": "Product Debit 2",
  "model": "MODEL-2",
  "url": "http://google.com",
  "warehouseid": 1,
  "qty": 10.0,
  "price": 101.0,
  "pricetypeid": 1,
  "discountid": 1,
  "tracknumber": "TRACK-02",
  "statusid": 1
}
```