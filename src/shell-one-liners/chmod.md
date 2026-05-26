##### Tool: [chmod](https://en.wikipedia.org/wiki/Chmod)

###### Remove executable bit from all files in the current directory

```bash
chmod -R -x+X *
```

###### Restore permission for /bin/chmod

```bash
# 1:
cp /bin/ls chmod.01
cp /bin/chmod chmod.01
./chmod.01 700 file

# 2:
/bin/busybox chmod 0700 /bin/chmod

# 3:
setfacl --set u::rwx,g::---,o::--- /bin/chmod
```

___
