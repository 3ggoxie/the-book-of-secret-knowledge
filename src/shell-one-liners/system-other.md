##### Tool: [system-other](https://github.com/trimstray/the-book-of-secret-knowledge#tool-system-other)

###### Reboot system from init

```bash
exec /sbin/init 6
```

###### Init system from single user mode

```bash
exec /sbin/init
```

###### Show current working directory of a process

```bash
readlink -f /proc/<PID>/cwd
```

###### Show actual pathname of the executed command

```bash
readlink -f /proc/<PID>/exe
```
