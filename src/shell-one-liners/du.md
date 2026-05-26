##### Tool: [du](https://en.wikipedia.org/wiki/GNU_Screen)

###### Show 20 biggest directories with 'K M G'

```bash
du | \
sort -r -n | \
awk '{split("K M G",v); s=1; while($1>1024){$1/=1024; s++} print int($1)" "v[s]"\t"$2}' | \
head -n 20
```

___
