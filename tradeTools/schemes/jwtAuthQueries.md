# TokenAuth
```
mutation TokenAuth($username: String!, $password: String!) {
  tokenAuth(username: $username, password: $password) {
    token
  }
}
```

# VerifyToken
```
mutation VerifyToken($token: String!) {
  verifyToken(token: $token) {
    payload
  }
}
```