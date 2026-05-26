##### Tool: [kill](https://en.wikipedia.org/wiki/Kill_(command))

###### Kill a process running on port

```bash
kill -9 $(lsof -i :<port> | awk '{l=$2} END {print l}')
```

___
