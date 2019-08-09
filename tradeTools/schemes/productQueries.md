# Get products by UserID
```
query {
    productsByuser {   
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

# Get products
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

# Get products total count 
```
query {
    products {   
    	totalCount
    }
}
```