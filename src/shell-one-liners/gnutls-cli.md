##### Tool: [gnutls-cli](https://gnutls.org/manual/html_node/gnutls_002dcli-Invocation.html)

###### Testing connection to remote host (with SNI support)

```bash
gnutls-cli -p 443 google.com
```

###### Testing connection to remote host (without SNI support)

```bash
gnutls-cli --disable-sni -p 443 google.com
```

___
