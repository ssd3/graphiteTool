# Get credit details
```
query getCreditDetails($creditid: Int!){
  creditdetails(creditid: $creditid){
    creditdetailsid
    creditid{
      creditid
    }
    productid{
      productid
    }
    price
    qty
    pricetypeid{
      title
    }    
  }
}
```

# Var
```
{
  "creditid": 1
}
```

# Get credit details by id
```
query getCreditDetail($creditdetailid: Int!){
  creditdetail(creditdetailid: $creditdetailid){
    creditdetailsid
    creditid{
      creditid
    }
    productid{
      productid
    }
    price
    qty
    pricetypeid{
      title
    }    
  }
}
```

# Var
```
{
  "creditdetailid": 1
}
```

# Create credit detail
```
mutation CreateCreditDetail($creditid: Int!, $productid: Int!,
                            $price: Int!, $qty: Int!,
                            $pricetypeid: Int!)
{
  createCreditdetail(creditid: $creditid, productid: $productid,
                    price: $price, qty: $qty, pricetypeid: $pricetypeid)
  {
    creditdetail{
      creditdetailsid
      creditid{
        creditid        
      }
      productid{
        productid
        title
      }
      price
      qty
      pricetypeid{
        pricetypeid
        title
      }
      userid{
        id
        username
      }
      created
    }
  }
}
```

# Variable create credit detail
```
{
  "creditid": 1,
  "productid": 2,
  "price": 100,
  "qty": 2,
  "pricetypeid": 2
}
```

# Update credit detail
```
mutation UpdateCreditDetail($creditdetailid: Int!, $creditid: Int!,
                $productid: Int!, $price: Int!, $qty: Int!,
                $pricetypeid: Int!)
{
  updateCreditdetail(creditdetailid: $creditdetailid, creditid: $creditid,
                productid: $productid, price: $price, qty: $qty,
                pricetypeid: $pricetypeid)
  {
    creditdetail{
      creditdetailsid
      creditid{
        creditid
      }
      productid{
        title
      }
      price
      qty
      created
    }
  }
}
```

# Var update credit detail
```
{
  "creditdetailid": 1,
  "creditid": 1,
  "productid": 1,
  "price": 300,
  "qty": 20,
  "pricetypeid": 1  
}
```