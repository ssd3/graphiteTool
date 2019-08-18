# Get all CreditTypes
```
query getCreditTypes
{
  credittypes{
    credittypeid
    title
    description
    created
  }
}
```

# Get CreditType by ID
```
query getCreditType($credittypeid: Int!)
{
  credittype(credittypeid: $credittypeid){
    credittypeid
    title
    description
    created
  }
}


{
  "credittypeid": 1
}
```

# Create CreditType
```
mutation CreateCreditType($title: String!, $description: String)
{
    createCredittype(title: $title, description: $description)
    {
    credittype{
      credittypeid
      title
      description
    }
  }
}

{
  "title": "Square",
  "description": "SquareDesc"
}
```

# Update CreditType
```
mutation UpdateCreditType($credittypeid: Int!, $title: String, $description: String)
{
    updateCredittype(credittypeid: $credittypeid, title: $title, description: $description)
    {
    credittype{
      credittypeid
      title
      description
    }
  }
}

{
  "credittypeid": 4,
  "title": "SquareUPD",
  "description": "SqDescriptionUPD"
}
```

