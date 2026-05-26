##### Tool: [tcpdump](http://www.tcpdump.org/)

###### Filter incoming (on interface) traffic (specific <ip:port>)

```bash
tcpdump -ne -i eth0 -Q in host 192.168.252.1 and port 443
```

  * `-n` - don't convert addresses (`-nn` will not resolve hostnames or ports)
  * `-e` - print the link-level headers
  * `-i [iface|any]` - set interface
  * `-Q|-D [in|out|inout]` - choose send/receive direction (`-D` - for old tcpdump versions)
  * `host [ip|hostname]` - set host, also `[host not]`
  * `[and|or]` - set logic
  * `port [1-65535]` - set port number, also `[port not]`

###### Filter incoming (on interface) traffic (specific <ip:port>) and write to a file

```bash
tcpdump -ne -i eth0 -Q in host 192.168.252.1 and port 443 -c 5 -w tcpdump.pcap
```

  * `-c [num]` - capture only num number of packets
  * `-w [filename]` - write packets to file, `-r [filename]` - reading from file

###### Capture all ICMP packets

```bash
tcpdump -nei eth0 icmp
```

###### Check protocol used (TCP or UDP) for service

```bash
tcpdump -nei eth0 tcp port 22 -vv -X | egrep "TCP|UDP"
```

###### Display ASCII text (to parse the output using grep or other)

```bash
tcpdump -i eth0 -A -s0 port 443
```

###### Grab everything between two keywords

```bash
tcpdump -i eth0 port 80 -X | sed -n -e '/username/,/=ldap/ p'
```

###### Grab user and pass ever plain http

```bash
tcpdump -i eth0  port http -l -A | egrep -i \
'pass=|pwd=|log=|login=|user=|username=|pw=|passw=|passwd=|password=|pass:|user:|username:|password:|login:|pass |user ' \
--color=auto --line-buffered -B20
```

###### Extract HTTP User Agent from HTTP request header

```bash
tcpdump -ei eth0 -nn -A -s1500 -l | grep "User-Agent:"
```

###### Capture only HTTP GET and POST packets

```bash
tcpdump -ei eth0 -s 0 -A -vv \
'tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420' or 'tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x504f5354'
```

or simply:

```bash
tcpdump -ei eth0 -s 0 -v -n -l | egrep -i "POST /|GET /|Host:"
```

###### Rotate capture files

```bash
tcpdump -ei eth0 -w /tmp/capture-%H.pcap -G 3600 -C 200
```

  * `-G <num>` - pcap will be created every `<num>` seconds
  * `-C <size>` - close the current pcap and open a new one if is larger than `<size>`

###### Top hosts by packets

```bash
tcpdump -ei enp0s25 -nnn -t -c 200 | cut -f 1,2,3,4 -d '.' | sort | uniq -c | sort -nr | head -n 20
```

###### Excludes any RFC 1918 private address

```bash
tcpdump -nei eth0 'not (src net (10 or 172.16/12 or 192.168/16) and dst net (10 or 172.16/12 or 192.168/16))'
```

___
