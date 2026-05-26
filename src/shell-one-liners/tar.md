##### Tool: [tar](https://en.wikipedia.org/wiki/Tar_(computing))

###### System backup with exclude specific directories

```bash
cd /
tar -czvpf /mnt/system$(date +%d%m%Y%s).tgz --directory=/ \
--exclude=proc/* --exclude=sys/* --exclude=dev/* --exclude=mnt/* .
```

###### System backup with exclude specific directories (pigz)

```bash
cd /
tar cvpf /backup/snapshot-$(date +%d%m%Y%s).tgz --directory=/ \
--exclude=proc/* --exclude=sys/* --exclude=dev/* \
--exclude=mnt/* --exclude=tmp/* --use-compress-program=pigz .
```

___
