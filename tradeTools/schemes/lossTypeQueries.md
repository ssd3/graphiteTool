# Сreate LossType 
```
mutation CreateLossType($title: String!)
{
  createLosstype(title: $title)
  {
    losstype
    {
      losstypeid
      title
      created
    }
  }
}

{
  "title": "LossType3"
}
```


# Update LossType
```
mutation updateLossType($losstypeid: Int!, $title: String!)
{
  updateLosstype(losstypeid: $losstypeid, title: $title)
  {
    losstype
    {
      losstypeid
      title
      created
    }
  }
}

{
  "losstypeid": 3,
  "title": "LossType3"
}
```

# Get LossTypes
```
query getLossTypes{
  losstypes{
    losstypeid
    title
    created
  }
}
```

# Get LossType
```
query getLossType($losstypeid: Int!){
  losstype(losstypeid: $losstypeid){
    losstypeid
    title
    created
  }
}
```