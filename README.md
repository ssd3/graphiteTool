# graphiteTool
graphiteTool



1. py manage.py shell
2. from productApp.models import User, Product
3. Product.objects.all()
4. User.objects.all()

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