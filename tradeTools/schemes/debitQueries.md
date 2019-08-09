# Debits get (edges/nodes)
```
query getDebits($first: Int, $last: Int, $before: String, $after: String, 
  $qty_expr: String, $price_expr: String, $created_expr: String,
  $debitid: Int, $warehouseid: Int, $productid: Int, $qty: Decimal, $price: Decimal, $pricetypeid: Int, $discountid: Int, $tracknumber: String, $statusid: Int, $notes: String, $userid: Int, $created: DateTime) {
  debits(first: $first, last: $last, before: $before, after: $after, 
    qtyExpr: $qty_expr, priceExpr: $price_expr, createdExpr: $created_expr,
    debitid: $debitid, warehouseid: $warehouseid, productid: $productid, qty: $qty, price: $price, pricetypeid: $pricetypeid, discountid: $discountid, tracknumber: $tracknumber, statusid: $statusid, notes: $notes, userid: $userid, created: $created) {
    edges {
      cursor
      node {
        debitid
        warehouse: warehouseid {
          warehouseid
          title
        }
        product: productid {
          productid
          title
        }
        qty
        price
        created
      }
    }
    pageInfo {
      hasNextPage
      hasPreviousPage
      startCursor
      endCursor
    }
  }
}

```

# Debits get variables
```
{
  "first": null,
  "last": null,
  "before": null,
  "after": null,
  "qty_expr": null,
  "debitid": null,
  "warehouseid": 1,
  "productid": null,
  "qty": null,
  "qty_expr": null,
  "price_expr": null,
  "price": null,
  "pricetypeid": null,
	"discountid": null,
	"tracknumber": null,
	"statusid": null,
	"notes": null,
	"userid": null,
	"created": null
}
```

# Debit simple mutation create
```
mutation Mutation($warehouseid: Int!,
                    $productid: Int!,
  					$qty: Decimal!,
  					$price: Decimal!,
  					$pricetypeid: Int!,
  					$discountid: Int!,
  					$tracknumber: String!,
  					$statusid: Int!,
  					$notes: String)
{
  result: createDebit(
		warehouseid: $warehouseid,
		productid: $productid,
  	    qty: $qty,
  	    price: $price,
  	    pricetypeid: $pricetypeid,
  	    discountid: $discountid,
  	    tracknumber: $tracknumber,
  	    statusid: $statusid,
  	    notes: $notes
  )
  {
    debit{
      debitid
      warehouse: warehouseid {
        warehouseid
        title
      }
      product: productid {
        productid
        title
      }
      qty
      price
      pricetype: pricetypeid {
        pricetypeid
        title
      }
      discount: discountid {
        discountid
        title
        value
        units
      }
      tracknumber
      status: statusid {
        statusid
        title
        value
      }
      notes
      user: userid {
        id
        username
      }
      created
    }
  }
}

```

# Debit simple mutation variables
```
{
  "warehouseid": 1,
  "productid": 24,
  "qty": 1.0,
  "price": 10.0,
  "pricetypeid": 1,
  "discountid": 1,
  "tracknumber": "TR001QWE121111345",
  "statusid": 1,
  "notes": null
}
```

# Debit get by id

```
query getDebitById($debitid: Int!)
{
  debit(debitid: $debitid){
    debitid
    warehouseid{
      title
      warehouseid
    }
    productid{
      productid
      categoryid{
        categoryid
        title
      }
      title
    }
    qty
    price
    pricetypeid{
      pricetypeid
      title
      ratio
    }
    discountid{
      discountid
      title
      value
      units
    }
    tracknumber
    statusid{
      statusid
      title
      value
    }
    notes
    created
  }
}

variables:
{
  "debitid": 17
}
```

# Debit simple mutation update
```
mutation Mutation($debitid: Int!,
  					$warehouseid: Int!,
            $productid: Int!,
  					$qty: Decimal!,
  					$price: Decimal!,
  					$pricetypeid: Int!,
  					$discountid: Int!,
  					$tracknumber: String!,
  					$statusid: Int!,
  					$notes: String)
{
  result: updateDebit(
    debitid: $debitid,
		warehouseid: $warehouseid,
		productid: $productid,
  	    qty: $qty,
  	    price: $price,
  	    pricetypeid: $pricetypeid,
  	    discountid: $discountid,
  	    tracknumber: $tracknumber,
  	    statusid: $statusid,
  	    notes: $notes
  )
  {
    debit{
      debitid
      warehouse: warehouseid {
        warehouseid
        title
      }
      product: productid {
        productid
        title
      }
      qty
      price
      pricetype: pricetypeid {
        pricetypeid
        title
      }
      discount: discountid {
        discountid
        title
        value
        units
      }
      tracknumber
      status: statusid {
        statusid
        title
        value
      }
      notes
      user: userid {
        id
        username
      }
      created
    }
  }
}

```

# Debit simple mutation update variables

```
{
  "debitid": 21,
  "warehouseid": 1,
  "productid": 31,
  "qty": 10.0,
  "price": 100.0,
  "pricetypeid": 1,
  "discountid": 1,
  "tracknumber": "TR001QWE1211113456",
  "statusid": 1,
  "notes": "update debit"
}
```

# Get debits by text (4 tables) with TotalCount
```
query getDebits($search_text: String){  
  debitsBytext(searchText: $search_text){  
    totalCount
    edges{     
      node{        
        debitid      
        productid{
          productid
          title
          productdetailsSet{
            productid{
              productid
            }
            model
          }
          productcommentSet{
            productid{
              productid
            }
            comment            
          }
        }        
      }
    }
  }
}
```

# Variable for get debits by text (4 tables)
```
{
  "search_text": "Model" or "777" or "Product"
}
```
