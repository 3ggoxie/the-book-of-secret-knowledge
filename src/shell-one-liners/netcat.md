##### Tool: [netcat](http://netcat.sourceforge.net/)

```bash
nc -kl 5000
```

  * `-l` - listen for an incoming connection
  * `-k` - listening after client has disconnected
  * `>filename.out` - save receive data to file (optional)

```bash
nc 192.168.0.1 5051 < filename.in
```

  * `< filename.in` - send data to remote host

```bash
nc -vz 10.240.30.3 5000
```

  * `-v` - verbose output
  * `-z` - scan for listening daemons

```bash
nc -vzu 10.240.30.3 1-65535
```

  * `-u` - scan only udp ports

###### Transfer data file (archive)

```bash
server> nc -l 5000 | tar xzvfp -
client> tar czvfp - /path/to/dir | nc 10.240.30.3 5000
```

###### Launch remote shell

```bash
# 1)
server> nc -l 5000 -e /bin/bash
client> nc 10.240.30.3 5000

# 2)
server> rm -f /tmp/f; mkfifo /tmp/f
server> cat /tmp/f | /bin/bash -i 2>&1 | nc -l 127.0.0.1 5000 > /tmp/f
client> nc 10.240.30.3 5000
```

###### Simple file server

```bash
while true ; do nc -l 5000 | tar -xvf - ; done
```

###### Simple minimal HTTP Server

```bash
while true ; do nc -l -p 1500 -c 'echo -e "HTTP/1.1 200 OK\n\n $(date)"' ; done
```

###### Simple HTTP Server

  > Restarts web server after each request - remove `while` condition for only single connection.

```bash
cat > index.html << __EOF__
<!doctype html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title></title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>

    Hello! It's a site.

    
</body>
</html>
__EOF__
```

```bash
server> while : ; do \
(echo -ne "HTTP/1.1 200 OK\r\nContent-Length: $(wc -c <index.html)\r\n\r\n" ; cat index.html;) | \
nc -l -p 5000 \
; done
```

  * `-p` - port number

###### Simple HTTP Proxy (single connection)

```bash
#!/usr/bin/env bash

if [[ $# != 2 ]] ; then
  printf "%s\\n" \
         "usage: ./nc-proxy listen-port bk_host:bk_port"
fi

_listen_port="$1"
_bk_host=$(echo "$2" | cut -d ":" -f1)
_bk_port=$(echo "$2" | cut -d ":" -f2)

printf "  lport: %s\\nbk_host: %s\\nbk_port: %s\\n\\n" \
       "$_listen_port" "$_bk_host" "$_bk_port"

_tmp=$(mktemp -d)
_back="$_tmp/pipe.back"
_sent="$_tmp/pipe.sent"
_recv="$_tmp/pipe.recv"

trap 'rm -rf "$_tmp"' EXIT

mkfifo -m 0600 "$_back" "$_sent" "$_recv"

sed "s/^/=> /" <"$_sent" &
sed "s/^/<=  /" <"$_recv" &

nc -l -p "$_listen_port" <"$_back" | \
tee "$_sent" | \
nc "$_bk_host" "$_bk_port" | \
tee "$_recv" >"$_back"
```

```bash
server> chmod +x nc-proxy && ./nc-proxy 8080 192.168.252.10:8000
  lport: 8080
bk_host: 192.168.252.10
bk_port: 8000

client> http -p h 10.240.30.3:8080
HTTP/1.1 200 OK
Accept-Ranges: bytes
Cache-Control: max-age=31536000
Content-Length: 2748
Content-Type: text/html; charset=utf-8
Date: Sun, 01 Jul 2018 20:12:08 GMT
Last-Modified: Sun, 01 Apr 2018 21:53:37 GMT
```

###### Create a single-use TCP or UDP proxy

```bash
### TCP -> TCP
nc -l -p 2000 -c "nc [ip|hostname] 3000"

### TCP -> UDP
nc -l -p 2000 -c "nc -u [ip|hostname] 3000"

### UDP -> UDP
nc -l -u -p 2000 -c "nc -u [ip|hostname] 3000"

### UDP -> TCP
nc -l -u -p 2000 -c "nc [ip|hostname] 3000"
```

___
