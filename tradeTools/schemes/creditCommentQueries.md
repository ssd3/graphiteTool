# Create CreditComment
```
mutation CreateCreditComment($creditid: Int!, $comment: String!)
{
  createCreditcomment(creditid: $creditid, comment: $comment)
  {
    creditcomment{
      creditcommentid
      creditid{
        creditid
      }
      comment
      created
    }
  }
}


{
  "creditid": 1,
  "comment": "3commentCreditID"
}
```

# Update CreditComment
```
mutation UpdateCreditComment($creditcommentid: Int! $creditid: Int, $comment: String)
{
  updateCreditcomment(creditcommentid: $creditcommentid, creditid: $creditid, comment: $comment)
  {
    creditcomment{
      creditcommentid
      creditid{
        creditid
      }
      comment
      created
    }
  }
}


{
  "creditcommentid": 2,
  "creditid": 1,
  "comment": "updComment"
}
```

# Get all CreditComments
```
query getCreditComments
{
  creditcomments{
    creditcommentid
    creditid{
      creditid
    }
    comment
    created
  }
}
```

# Get all CreditComments by CreditID
```
query getCreditCommentsByCredit($creditid: Int!)
{
  creditcommentsBycredit(creditid: $creditid){
    creditcommentid
    creditid{
      creditid
    }
    comment
    created
  }
}


{
  "creditid": 1
}  
```

# Get CreditComment by ID
```
query getCreditComment($creditcommentid: Int!)
{
  creditcomment(creditcommentid: $creditcommentid){
    creditcommentid
    creditid{
      creditid
    }
    comment
    created
  }
}


{
  "creditcommentid": 3
}  
```
