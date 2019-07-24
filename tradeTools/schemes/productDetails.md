# ProductDetails mutation create

```
mutation Mutation
(
  $productid: Int!,
  $model: String,
  $url: String,
  $serialno: String,
  $weight: Decimal,
	$height: Decimal,
	$width: Decimal,
  $length: Decimal
)
{
  result: createProductdetails(
    productid: $productid,
  	model: $model,
    url: $url,
    serialno: $serialno,
    weight: $weight,
    height: $height,
    width: $width,
    length: $length
  )
  {
    productdetails
    {
      productdetailsid
      productid{
        productid
        title
      }
      model
      url
      serialno
      weight
      height
      width
      length
    }
  }
}
```

# ProductDetails mutation create variables
```
{
  "productid": 30,
  "model": "Model 1",
  "url": "http://google.com",
  "serialno": "XC-001-991-234",
  "weight": null,
  "height": null,
  "width": null,
  "length": null
}
```

# ProductDetails mutation update
```
mutation Mutation
(
  $productdetailsid: Int!,
  $productid: Int!,
  $model: String,
  $url: String,
  $serialno: String,
  $weight: Decimal,
	$height: Decimal,
	$width: Decimal,
  $length: Decimal
)
{
  result: updateProductdetails(
    productdetailsid: $productdetailsid,
    productid: $productid,
  	model: $model,
    url: $url,
    serialno: $serialno,
    weight: $weight,
    height: $height,
    width: $width,
    length: $length
  )
  {
    productdetails
    {
      productdetailsid
      productid{
        productid
        title
        userid{
          id
          username
        }
      }
      model
      url
      serialno
      weight
      height
      width
      length
    }
  }
}
```

# ProductDetails mutation update variables
```
{
  "productdetailsid": 9,
  "productid": 30,
  "model": "Model 1",
  "url": "http://google.com/search",
  "serialno": "XC-001-991-234-123",
  "weight": 0.0,
  "height": 0.0,
  "width": 0.0,
  "length": 0.0
}
```

# ProductDetails query by ProductID
```
query getProductDetails($productid: Int!)
{
	result: productdetails(productid: $productid)
  {
    productdetailsid
    productid{
      productid
      title
    }
    model
    url
    serialno
    weight
    height
    width
    length
    userid{
      id
      username
    }
  }
}
```
# ProductDetails query by ProductID variables
```
{
  "productid": 30
}
```

# ProductDetails query by ID
```
query getProductDetailsById($productdetailsid: Int!)
{
	result: productdetail(productdetailsid: $productdetailsid)
  {
    productdetailsid
    productid{
      productid
      title
    }
    model
    url
    serialno
    weight
    height
    width
    length
    userid{
      id
      username
    }
  }
}
```

# ProductDetails query by ID variables
```
{
  "productdetailsid": 9
}
```