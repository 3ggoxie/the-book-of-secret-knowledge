##### Tool: [dump](https://en.wikipedia.org/wiki/Dump_(program))

###### System backup to file

```bash
dump -y -u -f /backup/system$(date +%d%m%Y%s).lzo /
```

###### Restore system from lzo file

```bash
cd /
restore -rf /backup/system$(date +%d%m%Y%s).lzo
```

___
