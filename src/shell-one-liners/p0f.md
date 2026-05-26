##### Tool: [p0f](http://lcamtuf.coredump.cx/p0f3/)

###### Set iface in promiscuous mode and dump traffic to the log file

```bash
p0f -i enp0s25 -p -d -o /dump/enp0s25.log
```

  * `-i` - listen on the specified interface
  * `-p` - set interface in promiscuous mode
  * `-d` - fork into background
  * `-o` - output file

___
