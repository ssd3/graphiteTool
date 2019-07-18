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