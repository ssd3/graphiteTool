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

# Get statuses with date range
```
query getStatuses($search: String, $date_from: DateTime, $date_to: DateTime) {
    statuses(search: $search, dateFrom: $date_from, dateTo: $date_to) {
      statusid
      title
      value
      created
	}
}
```

# Variables (statuses with date)
```
{  
  "search": "New",
  "date_from": "2019-06-28T15:11:50.669948+03",
  "date_to": "2019-08-02T13:01:34.286063+03"
}
```