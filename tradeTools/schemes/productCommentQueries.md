# ProductComment mutation create

```
mutation CreateProductComment 
(
  $productid: Int!,
  $comment: String!
)
{
  result: createProductcomment
  (
    productid: $productid,
  	comment: $comment
  )
  {
    productcomment
    {
      productcommentid
      productid {
        productid
        title
      }
      comment
      userid {
        id
        username
      }
      created
    }
  }
}
```
# ProductComment mutation create variables
```
{
  "productid": 28,
  "comment": "Product 28 comment"
}
```
# ProductComment mutation update
```
mutation UpdateProductComment 
(
  $productcommentid: Int!,
  $comment: String!
)
{
  result: updateProductcomment
  (
    productcommentid: $productcommentid,
  	comment: $comment
  )
  {
    productcomment
    {
      productcommentid
      productid {
        productid
        title
      }
      comment
      userid {
        id
        username
      }
      created
    }
  }
}
```
# ProductComment mutation update variables
```
{
  "productcommentid": 5,
  "comment": "Product 28 comment updated"
}
```
# ProductComments query by ProductID
```
query getProductComments($productid: Int!)
{
  results: productcomments(productid: $productid)
  {
    productcommentid
    productid{
      productid
      title
    }
    comment
    userid{
      id
      username
    }
    created
  }
}
```
# ProductComments query by ProductID variables
```
{
	"productid": 28
}
```

# ProductComment query by ID
```
query getProductCommentById($productcommentid: Int!)
{
  result: productcomment(productcommentid: $productcommentid)
  {
    productcommentid
    productid{
      productid
      title
    }
    comment
    userid{
      id
      username
    }
    created
  }
}
```
# ProductComment query by ID variables
```
{
	"productcommentid": 5
}
```