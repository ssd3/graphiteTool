# Get all statuses
```
query getStatuses($search: String) {
    statuses(search: $search) {
      statusid
      title
      value
      created
	}
}
```

# Variable below
```
{
  "search": "1"
}
```

```
{
  "search": "New"
}
```