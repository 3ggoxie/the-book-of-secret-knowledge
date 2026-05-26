##### Tool: [iostat](https://en.wikipedia.org/wiki/Iostat)

###### Show information about the CPU usage, and I/O statistics about all the partitions

```bash
iostat 2 10 -t -m
```

  * `2` - number of times with a defined time interval (delay)
  * `10` - each execution of the command (count)
  * `-t` - show timestamp
  * `-m` - fields in megabytes (`-k` - in kilobytes, default)

###### Show information only about the CPU utilization

```bash
iostat 2 10 -t -m -c
```

###### Show information only about the disk utilization

```bash
iostat 2 10 -t -m -d
```

###### Show information only about the LVM utilization

```bash
iostat -N
```

___
