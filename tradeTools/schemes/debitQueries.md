# Debits get (edges/nodes)
```
query getDebits
(
  $first: Int, 
  $last: Int, 
  $before: String, 
  $after: String, 
  $warehouseid: ID, 
  $tracknumber: String,
  $notes: String
) {
  debits(
    first: $first, 
    last: $last, 
    before: $before, 
    after: $after, 
    warehouseid: $warehouseid, 
    tracknumber: $tracknumber,
    notes_Icontains: $notes
	) 
  {
    edges {
      cursor
      node {
        debitid
        warehouse: warehouseid {
          warehouseid
          title
        }
        tracknumber
        notes
        user: userid {
          id
          username
        }
        created
        products: productSet {
          productid
          category: categoryid {
            categoryid
            title
          }
          title
          qty
          price
          price2
          price3
          status: statusid {
            statusid
            title
            color
          }
          description
          pricetype: pricetypeid {
            pricetypeid
            title
            ratio
          }
          discount: discountid {
            discountid
            title
          }
        }
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
  "warehouseid": 2,
  "tracknumber": "TR003-0921",
  "notes": "Notes"
}
```

# Debit simple mutation create
```
mutation createDebit
(
  $warehouseid: Int!,
  $tracknumber: String!,
  $notes: String
)
{
  result: createDebit
  (
		warehouseid: $warehouseid,
    tracknumber: $tracknumber,
    notes: $notes
  )
  {
    debit{
      debitid
      warehouse: warehouseid {
        warehouseid
        title
      }
      tracknumber
      notes
      user: userid {
        id
        username
      }
      created
      products: productSet {
        productid
        category: categoryid {
          categoryid
          title
        }
        title
        qty
        price
        price2
        price3
        status: statusid {
          statusid
          title
          color
        }
        description
        pricetype: pricetypeid {
          pricetypeid
          title
          ratio
        }
        discount: discountid {
          discountid
          title
        }
      }
    }
  }
}
```

# Debit simple mutation variables
```
{
  "warehouseid": 2,
  "tracknumber": "TR001-0921",
  "notes": null
}
```

# Debit get by id

```
query getDebitById($debitid: Int!)
{
  debit(debitid: $debitid)
  {
  	debitid
    warehouse: warehouseid {
      warehouseid
      title
    }
    tracknumber
    notes
    user: userid {
      id
      username
    }
    created
    products: productSet {
      productid
      category: categoryid {
        categoryid
        title
      }
      title
      qty
      price
      price2
      price3
      status: statusid {
        statusid
        title
        color
      }
      description
      pricetype: pricetypeid {
      	pricetypeid
        title
        ratio
      }
      discount: discountid {
        discountid
        title
      }
    }
  }
}
```
# Debit get by id variables
```
variables:
{
  "debitid": 4
}
```

# Debit simple mutation update
```
mutation updateDebit
(
  $debitid: Int!,
  $warehouseid: Int!,
	$tracknumber: String!,
	$notes: String
)
{
	result: updateDebit(
    debitid: $debitid,
		warehouseid: $warehouseid,
    tracknumber: $tracknumber,
    notes: $notes
  )
  {
		debit{
      debitid
      warehouse: warehouseid {
        warehouseid
        title
      }
      tracknumber
      notes
      user: userid {
        id
        username
      }
      created
      products: productSet {
        productid
        category: categoryid {
          categoryid
          title
        }
        title
        qty
        price
        price2
        price3
        status: statusid {
          statusid
          title
          color
        }
        description
        pricetype: pricetypeid {
          pricetypeid
          title
          ratio
        }
        discount: discountid {
          discountid
          title
        }
      }
    }
  }
}
```

# Debit simple mutation update variables
```
{
  "debitid": 4,
  "warehouseid": 1,
  "tracknumber": "TR003-0921"
}
```

# Get debits by text (4 tables) with TotalCount
```
query getDebits
(
  $search_text: String
)
{  
  debitsBytext(searchText: $search_text){  
    totalCount
    edges{     
      node{        
    		debitid
        warehouse: warehouseid {
          warehouseid
          title
        }
        tracknumber
        notes
        user: userid {
          id
          username
        }
        created
        products: productSet {
          productid
          category: categoryid {
            categoryid
            title
          }
          title
          qty
          price
          price2
          price3
          status: statusid {
            statusid
            title
            color
          }
          description
          pricetype: pricetypeid {
            pricetypeid
            title
            ratio
          }
          discount: discountid {
            discountid
            title
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
  "search_text": "1"
}
```


```
# Update Debit's StatusID 
```
```
mutation UpdateDebitStatusID($debitid: [Int]!, $statusid: Int!)
{
  updateDebitStatusid(debitid: $debitid, statusid: $statusid)
  {
    debit{
      debitid
      statusid{
        statusid
      }
    }
  }
}
```
```
# Var upd debit's statusid
```
```
{
  "debitid": [2,6,8],
  "statusid": 2
}
```