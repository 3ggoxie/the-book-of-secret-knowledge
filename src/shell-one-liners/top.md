##### Tool: [top](https://en.wikipedia.org/wiki/Top_(software))

###### Use top to monitor only all processes with the specific string

```bash
top -p $(pgrep -d , <str>)
```

  * `<str>` - process containing string (eg. nginx, worker)

___
