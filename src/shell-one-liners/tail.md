##### Tool: [tail](https://en.wikipedia.org/wiki/Tail_(Unix))

###### Annotate tail -f with timestamps

```bash
tail -f file | while read ; do echo "$(date +%T.%N) $REPLY" ; done
```

###### Analyse an Apache access log for the most common IP addresses

```bash
tail -10000 access_log | awk '{print $1}' | sort | uniq -c | sort -n | tail
```

###### Analyse web server log and show only 5xx http codes

```bash
tail -n 100 -f /path/to/logfile | grep "HTTP/[1-2].[0-1]\" [5]"
```

___
