##### Tool: [ngrep](http://ngrep.sourceforge.net/usage.html)

```bash
ngrep -d eth0 "www.domain.com" port 443
```

  * `-d [iface|any]` - set interface
  * `[domain]` - set hostname
  * `port [1-65535]` - set port number

```bash
ngrep -d eth0 "www.domain.com" src host 10.240.20.2 and port 443
```

  * `(host [ip|hostname])` - filter by ip or hostname
  * `(port [1-65535])` - filter by port number

```bash
ngrep -d eth0 -qt -O ngrep.pcap "www.domain.com" port 443
```

  * `-q` - quiet mode (only payloads)
  * `-t` - added timestamps
  * `-O [filename]` - save output to file, `-I [filename]` - reading from file

```bash
ngrep -d eth0 -qt 'HTTP' 'tcp'
```

  * `HTTP` - show http headers
  * `tcp|udp` - set protocol
  * `[src|dst] host [ip|hostname]` - set direction for specific node

```bash
ngrep -l -q -d eth0 -i "User-Agent: curl*"
```

  * `-l` - stdout line buffered
  * `-i` - case-insensitive search

___
