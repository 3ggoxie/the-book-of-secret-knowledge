##### Tool: [python](https://www.python.org/)

###### Static HTTP web server

```bash
# Python 3.x
python3 -m http.server 8000 --bind 127.0.0.1

# Python 2.x
python -m SimpleHTTPServer 8000
```

###### Static HTTP web server with SSL support

```bash
# Python 3.x
from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

httpd = HTTPServer(('localhost', 4443), BaseHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket,
        keyfile="path/to/key.pem",
        certfile='path/to/cert.pem', server_side=True)

httpd.serve_forever()

# Python 2.x
import BaseHTTPServer, SimpleHTTPServer
import ssl

httpd = BaseHTTPServer.HTTPServer(('localhost', 4443),
        SimpleHTTPServer.SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket,
        keyfile="path/tp/key.pem",
        certfile='path/to/cert.pem', server_side=True)

httpd.serve_forever()
```

###### Encode base64

```bash
python -m base64 -e <<< "sample string"
```

###### Decode base64

```bash
python -m base64 -d <<< "dGhpcyBpcyBlbmNvZGVkCg=="
```
