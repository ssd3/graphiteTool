# graphiteTool

# graphql
1. run http://127.0.0.1:8000/graphql
2. type query
example: 

```
query {
  products {
    productid
    title
    created
  }
}
```

# Mutation create
@log in in admin panel before mutation(category tbl uses UserID)
```
mutation Mutation($categoryid: Int!, $title: String!, $description: String)
{
  result: createProduct(
    categoryid: $categoryid
    title: $title,
    description: $description
  ){
    product{   
      productid
      title            
      description
      categoryid {
        categoryid
        title
      }
      userid {
        id
        username
      }
    }        
  }
}
```
and Query Variables example
```
{
  "categoryid": 1,
  "title": "Product Title 555"
}
```


# Mutation update

```
mutation Mutation($productid: Int!, $categoryid: Int!, $title: String!, $description: String)
{
  result: updateProduct(
    productid: $productid,
    categoryid: $categoryid
    title: $title,
    description: $description
  ){
    product{   
      productid
      title            
      description
      categoryid {
        categoryid
        title
      }
      userid {
        id
        username
      }
    }        
  }
}
```
and Query Variables example
```
{
  "productid": 28,
  "categoryid": 1,
  "title": "Product Title 777"
  "description": "Product Title 777 description"
}
```

# Products relay

```
{
    products (first: 2) {
        edges {
        	cursor
        	node {
            	        productid
            	        title
        	    }
        }
        pageInfo {
        	startCursor
        	endCursor
        	hasNextPage
        	hasPreviousPage
        }
    }
}

```


# Edit Length to Lenght
```
1. models.py class ProductDetails
lenght = models.DecimalField(db_column='Lenght', max_digits=10, decimal_places=2, blank=True, null=True)
Class Meta: managed = True
2. py manage.py makemigrations tradeTools
3. py manage.py migrate
4. go to pgadmin ProductDetails->props->columns->rename to Lenght
```

# Rename status.color -> value
```
py manage.py makemigrations tradeTools
py manage.py migrate
pgadmin rename field
```

# Update Credi/CreditLoss fields
```
py manage.py makemigrations tradeTools
py manage.py migrate
```