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
mutation Mutation{
  createCategory(title:"NewMutationCategory"){
    category{   // expected returning fields to see after create
      title            
      categoryid
    }        
  }
}
```

```
mutation Mutation{
  createProduct(title:"NewMutationProd", description:"MutProdDesc"){
    product{   
      title            
      description
    }        
  }
}
```


# Mutation update

```
mutation Mutation{
  updateCategory(categoryid:22, title:"UpdatedMutationCategory"){
    category{
      title      
    }        
  }
}
```