##### Tool: [mount](https://en.wikipedia.org/wiki/Mount_(Unix))

###### Mount a temporary ram partition

```bash
mount -t tmpfs tmpfs /mnt -o size=64M
```

  * `-t` - filesystem type
  * `-o` - mount options

###### Remount a filesystem as read/write

```bash
mount -o remount,rw /
```

___
