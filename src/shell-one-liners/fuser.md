##### Tool: [fuser](https://en.wikipedia.org/wiki/Fuser_(Unix))

###### Show which processes use the files/directories

```bash
fuser /var/log/daemon.log
fuser -v /home/supervisor
```

###### Kills a process that is locking a file

```bash
fuser -ki filename
```

  * `-i` - interactive option

###### Kills a process that is locking a file with specific signal

```bash
fuser -k -HUP filename
```

  * `--list-signals` - list available signal names

###### Show what PID is listening on specific port

```bash
fuser -v 53/udp
```

###### Show all processes using the named filesystems or block device

```bash
fuser -mv /var/www
```

___
