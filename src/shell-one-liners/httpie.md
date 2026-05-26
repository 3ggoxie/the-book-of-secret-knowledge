##### Tool: [httpie](https://httpie.org/)

```bash
http -p Hh https://www.google.com
```

  * `-p` - print request and response headers
    * `H` - request headers
    * `B` - request body
    * `h` - response headers
    * `b` - response body

```bash
http -p Hh https://www.google.com --follow --verify no
```

  * `-F, --follow` - follow redirects
  * `--verify no` - skip SSL verification

```bash
http -p Hh https://www.google.com --follow --verify no \
--proxy http:http://127.0.0.1:16379
```

  * `--proxy [http:]` - set proxy server
