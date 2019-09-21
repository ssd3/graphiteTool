# Get products by UserID with totalCount
```
query GET_PRODUCTS_BY_USER 
(
  $userid: Int!
)
{
  productsByUser
  (
    userid: $userid
  ) 
  {
		edges {
      node {
        productid
        debit: debitid {
          debitid
        }
        category: categoryid {
          categoryid
          title
        }
        title
        qty
        price
        price2
        price3
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
        status: statusid {
          statusid
          title
          color
        }
        description
        created
        user: userid {
          id
          username
        }        
      }
    }
		totalCount
    pageInfo {
      hasNextPage
      hasPreviousPage
      startCursor
      endCursor
    }
  }
}
```
# Get products by UserID with totalCount variables
```
{
	"userid": 1
}
```
#Products get
```
query GET_PRODUCTS {
  products {
    edges {
      node {
        productid
        category: categoryid {
          categoryid
          title
        }
        title
        description
        user: userid {
          id
          username
        }
        created
      }
    }
    pageInfo{
      hasNextPage
      hasPreviousPage
      startCursor
      endCursor
    }
  }
}
```
# Get products with totalCount
```
query {
    products {   
    totalCount
    edges {      
      node {                
        title
        userid
        {
            id
        }
      }
    }
  }
}
```
# Product get by id
```
query GET_PRODUCT($productid: Int!) {
  product(productid: $productid) {
    productid
    category: categoryid {
      categoryid
      title
    }
    title
    description
    user: userid {
      id
      username
    }
    created
  }
}
```
# Product get by id variables
```
{
  "productid": 13
}
```
# Product create
```
mutation CREATE_PRODUCT
(
  $debitid: Int!,
  $categoryid: Int!,
  $title: String!,
  $qty: Decimal!,
  $price: Decimal!,
  $price2: Decimal!,
  $price3: Decimal!,
  $pricetypeid: Int!,
  $discountid: Int!,
  $statusid: Int!,
  $description: String
)
{
  createProduct
  (
    debitid: $debitid,
  	categoryid: $categoryid,
    title: $title,
    qty: $qty,
    price: $price,
    price2: $price2,
    price3: $price3,
    pricetypeid: $pricetypeid,
    discountid: $discountid,
    statusid: $statusid,
    description: $description
  )
  {
    product {
      productid
      debit: debitid {
        debitid
      }
      category: categoryid {
        categoryid
        title
      }
      title
      qty
      price
      price2
      price3
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
      status: statusid {
        statusid
        title
        color
      }
      description
      created
      user: userid {
        id
        username
      }
    }
  }
}
```
# Create product variables
```
{
  "debitid": 4,
  "categoryid": 1,
  "title": "Product-3 0921",
  "qty": 10,
  "price": 0,
  "price2": 0,
  "price3": 0,
  "pricetypeid": 1,
  "discountid": 1,
  "statusid": 1,
  "description": null
}
```

# Get products total count 
```
query {
    products {   
    	totalCount
    }
}
```
# Product create variables
```
{
  "categoryid": 3,
  "title": "Product New",
  "description": "Product New description"
}
```


# Product update
```
mutation UPDATE_PRODUCT
(
  $productid: Int!,
  $debitid: Int!,
  $categoryid: Int!,
  $title: String!,
  $qty: Decimal!,
  $price: Decimal!,
  $price2: Decimal!,
  $price3: Decimal!,
  $pricetypeid: Int!,
  $discountid: Int!,
  $statusid: Int!,
  $description: String
)
{
  updateProduct
  (
    productid: $productid,
    debitid: $debitid,
  	categoryid: $categoryid,
    title: $title,
    qty: $qty,
    price: $price,
    price2: $price2,
    price3: $price3,
    pricetypeid: $pricetypeid,
    discountid: $discountid,
    statusid: $statusid,
    description: $description
  )
  {
    product {
      productid
      debit: debitid {
        debitid
      }
      category: categoryid {
        categoryid
        title
      }
      title
      qty
      price
      price2
      price3
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
      status: statusid {
        statusid
        title
        color
      }
      description
      created
      user: userid {
        id
        username
      }
    }
  }
}

```
# Product update variables
```
{
  "productid": 3,
  "debitid": 4,
  "categoryid": 1,
  "title": "Product-3 0921",
  "qty": 10,
  "price": 0,
  "price2": 0,
  "price3": 0,
  "pricetypeid": 1,
  "discountid": 1,
  "statusid": 1,
  "description": null
}
```

# Get products by category title
```
query getProductsByCategoryTitle($category_title: String){
  productsBycategoryTitle(categoryTitle: $category_title){    
    edges{
      node{       
        title
        categoryid{
          categoryid
          title
        }
      }
    }
  }
}
```

# Variable get products by category title
```
{
  "category_title": "def"
}
```

# Get products by UserID and (optional) by CategoryID
```
query getProductsByUserID($category_title: String){
  productsByuser(categoryTitle: $category_title){    
    edges{
      node{
        title
        userid{
          id
        }
        categoryid{
          categoryid
          title
        }
      }
    }
  }
}
```

# Variable get products by UserID and (optional) by CategoryID
```
{
  "category_title": "categ"
}
```

# Get product by debitid
```
query GET_PRODUCT_BY_DEBIT
(
  $debitid: Int!
)
{
  productsByDebit
  (
    debitid: $debitid
  ) {
    edges {
      node {
        productid
        debit: debitid {
          debitid
        }
        category: categoryid {
          categoryid
          title
        }
        title
        qty
        price
        price2
        price3
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
        status: statusid {
          statusid
          title
          color
        }
        description
        created
        user: userid {
          id
          username
        }        
      }
    }
		totalCount
    pageInfo {
      hasNextPage
      hasPreviousPage
      startCursor
      endCursor
    }
  }
}
```
# Get product by debitid variables
```
{
  "debitid": 4
}
```