# create creditloss

```
mutation CREATE_CREDITLOSS
(
  $creditid: Int!, 
  $losstypeid: Int!, 
  $rate: Decimal!, 
  $notes: String
)
{
  createCreditloss
  (
    creditid: $creditid, 
    losstypeid: $losstypeid, 
    rate: $rate, 
    notes: $notes
  )
  {
    result: creditloss {
      creditlossid,
      creditid {
        creditid
      }
      losstypeid {
        losstypeid
        title
      }
      rate
      notes
    }
  }
}
```

# variables create creditloss
```
{
  "creditid": 2,
  "losstypeid": 3,
  "rate": 7.5
}
```

# update credit loss
```
mutation UPDATE_CREDITLOSSES
(
  $creditlossid: Int!,
  $creditid: Int!, 
  $losstypeid: Int!, 
  $rate: Decimal!, 
  $notes: String
)
{
  updateCreditloss
  (
    creditlossid: $creditlossid,
    creditid: $creditid, 
    losstypeid: $losstypeid, 
    rate: $rate, 
    notes: $notes
  )
  {
    result: creditloss {
      creditlossid,
      creditid {
        creditid
      }
      losstypeid {
        losstypeid
        title
      }
      rate
      notes
    }
  }
}
```

# variables update credit loss
```
{
  "creditlossid": 4,
  "creditid": 2,
  "losstypeid": 1,
  "rate": 7.5,
  "notes": "Other losses"
}
```