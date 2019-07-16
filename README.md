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

```
mutation MyFirstMutation{
  createCategory(title:"NewMutationCategory"){
    category{   // expected returning fields to see after create
      title            
      categoryid
    }        
  }
}
```

# Mutation update

```
mutation MyFirstMutation{
  updateCategory(categoryid:22, title:"UpdatedMutationCategory"){
    category{
      title      
    }        
  }
}
```