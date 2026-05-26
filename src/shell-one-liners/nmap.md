##### Tool: [nmap](https://nmap.org/)

###### Ping scans the network

```bash
nmap -sP 192.168.0.0/24
```

###### Show only open ports

```bash
nmap -F --open 192.168.0.0/24
```

###### Full TCP port scan using with service version detection

```bash
nmap -p 1-65535 -sV -sS -T4 192.168.0.0/24
```

###### Nmap scan and pass output to Nikto

```bash
nmap -p80,443 192.168.0.0/24 -oG - | nikto.pl -h -
```

###### Recon specific ip:service with Nmap NSE scripts stack

```bash
# Set variables:
_hosts="192.168.250.10"
_ports="80,443"

# Set Nmap NSE scripts stack:
_nmap_nse_scripts="+dns-brute,\
                   +http-auth-finder,\
                   +http-chrono,\
                   +http-cookie-flags,\
                   +http-cors,\
                   +http-cross-domain-policy,\
                   +http-csrf,\
                   +http-dombased-xss,\
                   +http-enum,\
                   +http-errors,\
                   +http-git,\
                   +http-grep,\
                   +http-internal-ip-disclosure,\
                   +http-jsonp-detection,\
                   +http-malware-host,\
                   +http-methods,\
                   +http-passwd,\
                   +http-phpself-xss,\
                   +http-php-version,\
                   +http-robots.txt,\
                   +http-sitemap-generator,\
                   +http-shellshock,\
                   +http-stored-xss,\
                   +http-title,\
                   +http-unsafe-output-escaping,\
                   +http-useragent-tester,\
                   +http-vhosts,\
                   +http-waf-detect,\
                   +http-waf-fingerprint,\
                   +http-xssed,\
                   +traceroute-geolocation.nse,\
                   +ssl-enum-ciphers,\
                   +whois-domain,\
                   +whois-ip"

# Set Nmap NSE script params:
_nmap_nse_scripts_args="dns-brute.domain=${_hosts},http-cross-domain-policy.domain-lookup=true,"
_nmap_nse_scripts_args+="http-waf-detect.aggro,http-waf-detect.detectBodyChanges,"
_nmap_nse_scripts_args+="http-waf-fingerprint.intensive=1"

# Perform scan:
nmap --script="$_nmap_nse_scripts" --script-args="$_nmap_nse_scripts_args" -p "$_ports" "$_hosts"
```

___
