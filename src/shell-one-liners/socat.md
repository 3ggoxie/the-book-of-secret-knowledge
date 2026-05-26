##### Tool: [socat](http://www.dest-unreach.org/socat/doc/socat.html)

###### Testing remote connection to port

```bash
socat - TCP4:10.240.30.3:22
```

  * `-` - standard input (STDIO)
  * `TCP4:<params>` - set tcp4 connection with specific params
    * `[hostname|ip]` - set hostname/ip
    * `[1-65535]` - set port number

###### Redirecting TCP-traffic to a UNIX domain socket under Linux

```bash
socat TCP-LISTEN:1234,bind=127.0.0.1,reuseaddr,fork,su=nobody,range=127.0.0.0/8 UNIX-CLIENT:/tmp/foo
```

  * `TCP-LISTEN:<params>` - set tcp listen with specific params
    * `[1-65535]` - set port number
    * `bind=[hostname|ip]` - set bind hostname/ip
    * `reuseaddr` - allows other sockets to bind to an address
    * `fork` - keeps the parent process attempting to produce more connections
    * `su=nobody` - set user
    * `range=[ip-range]` - ip range
  * `UNIX-CLIENT:<params>` - communicates with the specified peer socket
    * `filename` - define socket

___
