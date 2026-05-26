##### Tool: [strace](https://en.wikipedia.org/wiki/Strace)

###### Track with child processes

```bash
# 1)
strace -f -p $(pidof glusterfsd)

# 2)
strace -f $(pidof php-fpm | sed 's/\([0-9]*\)/\-p \1/g')
```

###### Track process with 30 seconds limit

```bash
timeout 30 strace $(< /var/run/zabbix/zabbix_agentd.pid)
```

###### Track processes and redirect output to a file

```bash
ps auxw | grep '[a]pache' | awk '{print " -p " $2}' | \
xargs strace -o /tmp/strace-apache-proc.out
```

###### Track with print time spent in each syscall and limit length of print strings

```bash
ps auxw | grep '[i]init_policy' | awk '{print " -p " $2}' | \
xargs strace -f -e trace=network -T -s 10000
```

###### Track the open request of a network port

```bash
strace -f -e trace=bind nc -l 80
```

###### Track the open request of a network port (show TCP/UDP)

```bash
strace -f -e trace=network nc -lu 80
```

___
