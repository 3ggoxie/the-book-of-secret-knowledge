##### Tool: [network-other](https://github.com/trimstray/the-book-of-secret-knowledge#tool-network-other)

###### Get all subnets for specific AS (Autonomous system)

```bash
AS="AS32934"
whois -h whois.radb.net -- "-i origin ${AS}" | \
grep "^route:" | \
cut -d ":" -f2 | \
sed -e 's/^[ \t]//' | \
sort -n -t . -k 1,1 -k 2,2 -k 3,3 -k 4,4 | \
cut -d ":" -f2 | \
sed -e 's/^[ \t]/allow /' | \
sed 's/$/;/' | \
sed 's/allow  */subnet -> /g'
```

###### Resolves domain name from dns.google.com with curl and jq

```bash
_dname="google.com" ; curl -s "https://dns.google.com/resolve?name=${_dname}&type=A" | jq .
```
