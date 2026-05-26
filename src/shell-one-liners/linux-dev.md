##### Tool: [linux-dev](https://www.tldp.org/LDP/abs/html/devref1.html)

###### Testing remote connection to port

```bash
timeout 1 bash -c "</dev/<proto>/<host>/<port>" >/dev/null 2>&1 ; echo $?
```

  * `<proto` - set protocol (tcp/udp)
  * `<host>` - set remote host
  * `<port>` - set destination port

###### Read and write to TCP or UDP sockets with common bash tools

```bash
exec 5<>/dev/tcp/<host>/<port>; cat <&5 & cat >&5; exec 5>&-
```

___
