##### Tool: [secure-delete](https://wiki.archlinux.org/index.php/Securely_wipe_disk)

###### Secure delete with shred

```bash
shred -vfuz -n 10 file
shred --verbose --random-source=/dev/urandom -n 1 /dev/sda
```

###### Secure delete with scrub

```bash
scrub -p dod /dev/sda
scrub -p dod -r file
```

###### Secure delete with badblocks

```bash
badblocks -s -w -t random -v /dev/sda
badblocks -c 10240 -s -w -t random -v /dev/sda
```

###### Secure delete with secure-delete

```bash
srm -vz /tmp/file
sfill -vz /local
sdmem -v
swapoff /dev/sda5 && sswap -vz /dev/sda5
```

___
