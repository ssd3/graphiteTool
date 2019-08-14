# Get all credits
```
query {
  credits{
  totalcount
    edges{
      node{
        creditid
        buyerid
        fromwarehouseid
        towarehouseid
        userid{
          id
          username
        }
        sent
        received        
      }
    }
  }
}
```

# Get credit by ID
```
query getCreditById($creditid: Int!){
  credit(creditid: $creditid){
    creditid
    buyerid
    fromwarehouseid
    towarehouseid
	  userid{
      id
      username
    }
    sent
    received    
  }
}
```

# Variable credit by ID
```
{
  "creditid": 1
}
```

# Credit create
```
mutation CreateCredit($credittypeid: Int!, $buyerid: Int!,
                      $fromwarehouseid: Int, $towarehouseid: Int,
                      $sent: DateTime, $received: DateTime)
{
    createCredit(credittypeid: $credittypeid,
                 buyerid: $buyerid,
                 fromwarehouseid: $fromwarehouseid,
                 towarehouseid: $towarehouseid,
                 sent: $sent, received: $received)
    {
    credit{
      creditid
      buyerid
      fromwarehouseid
      towarehouseid
      userid{
        id
        username
      }
      created
      sent
      received      
    }
  }
}
```

# Variable credit create
```
{
  "credittypeid": 1,
  "buyerid": 3,
  "fromwarehouseid": 5,
  "towarehouseid": 6  
}
```

# Update credit
```
mutation UpdateCredit($creditid: Int!, $credittypeid: Int!,
                      $buyerid: Int!, $fromwarehouseid: Int!,
                      $towarehouseid: Int!)
{
    updateCredit(creditid: $creditid, credittypeid: $credittypeid,
                 buyerid: $buyerid, fromwarehouseid: $fromwarehouseid,
                 towarehouseid: $towarehouseid)
  {
    credit{
      creditid
      buyerid
      fromwarehouseid
      towarehouseid      
    }
  }
}
```

# Variable update credit
```
{
  "creditid": 1,
  "credittypeid": 1,
  "buyerid": 5,
  "fromwarehouseid": 5,
  "towarehouseid": 5
}
```