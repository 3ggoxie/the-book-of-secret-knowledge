##### Tool: [curl](https://curl.haxx.se)

```bash
curl -Iks https://www.google.com
```

  * `-I` - show response headers only
  * `-k` - insecure connection when using ssl
  * `-s` - silent mode (not display body)

```bash
curl -Iks --location -X GET -A "x-agent" https://www.google.com
```

  * `--location` - follow redirects
  * `-X` - set method
  * `-A` - set user-agent

```bash
curl -Iks --location -X GET -A "x-agent" --proxy http://127.0.0.1:16379 https://www.google.com
```

  * `--proxy [socks5://|http://]` - set proxy server

```bash
curl -o file.pdf -C - https://example.com/Aiju2goo0Ja2.pdf
```

  * `-o` - write output to file
  * `-C` - resume the transfer

###### Find your external IP address (external services)

```bash
curl ipinfo.io
curl ipinfo.io/ip
curl icanhazip.com
curl ifconfig.me/ip ; echo
```

###### Repeat URL request

```bash
# URL sequence substitution with a dummy query string:
curl -ks https://example.com/?[1-20]

# With shell 'for' loop:
for i in {1..20} ; do curl -ks https://example.com/ ; done
```

###### Check DNS and HTTP trace with headers for specific domains

```bash
### Set domains and external dns servers.
_domain_list=(google.com) ; _dns_list=("8.8.8.8" "1.1.1.1")

for _domain in "${_domain_list[@]}" ; do

  printf '=%.0s' {1..48}

  echo

  printf "[\\e[1;32m+\\e[m] resolve: %s\\n" "$_domain"

  for _dns in "${_dns_list[@]}" ; do

    # Resolve domain.
    host "${_domain}" "${_dns}"

    echo

  done

  for _proto in http https ; do

    printf "[\\e[1;32m+\\e[m] trace + headers: %s://%s\\n" "$_proto" "$_domain"

    # Get trace and http headers.
    curl -Iks -A "x-agent" --location "${_proto}://${_domain}"

    echo

  done

done

unset _domain_list _dns_list
```

___
