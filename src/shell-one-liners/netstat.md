##### Tool: [netstat](https://en.wikipedia.org/wiki/Netstat)

###### Graph # of connections for each hosts

```bash
netstat -an | awk '/ESTABLISHED/ { split($5,ip,":"); if (ip[1] !~ /^$/) print ip[1] }' | \
sort | uniq -c | awk '{ printf("%s\t%s\t",$2,$1) ; for (i = 0; i < $1; i++) {printf("*")}; print "" }'
```

###### Monitor open connections for specific port including listen, count and sort it per IP

```bash
watch "netstat -plan | grep :443 | awk {'print \$5'} | cut -d: -f 1 | sort | uniq -c | sort -nk 1"
```

###### Grab banners from local IPv4 listening ports

```bash
netstat -nlt | grep 'tcp ' | grep -Eo "[1-9][0-9]*" | xargs -I {} sh -c "echo "" | nc -v -n -w1 127.0.0.1 {}"
```

___
