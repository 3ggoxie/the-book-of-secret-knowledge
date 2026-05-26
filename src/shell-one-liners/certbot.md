##### Tool: [certbot](https://certbot.eff.org/)

###### Generate multidomain certificate

```bash
certbot certonly -d example.com -d www.example.com
```

###### Generate wildcard certificate

```bash
certbot certonly --manual --preferred-challenges=dns -d example.com -d *.example.com
```

###### Generate certificate with 4096 bit private key

```bash
certbot certonly -d example.com -d www.example.com --rsa-key-size 4096
```

___
