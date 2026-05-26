##### Tool: [vmstat](https://en.wikipedia.org/wiki/Vmstat)

###### Show current system utilization (fields in kilobytes)

```bash
vmstat 2 20 -t -w
```

  * `2` - number of times with a defined time interval (delay)
  * `20` - each execution of the command (count)
  * `-t` - show timestamp
  * `-w` - wide output
  * `-S M` - output of the fields in megabytes instead of kilobytes

###### Show current system utilization will get refreshed every 5 seconds

```bash
vmstat 5 -w
```

###### Display report a summary of disk operations

```bash
vmstat -D
```

###### Display report of event counters and memory stats

```bash
vmstat -s
```

###### Display report about kernel objects stored in slab layer cache

```bash
vmstat -m
```
