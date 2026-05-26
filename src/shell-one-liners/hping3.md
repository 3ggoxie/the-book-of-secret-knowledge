##### Tool: [hping3](http://www.hping.org/)

```bash
hping3 -V -p 80 -s 5050 <scan_type> www.google.com
```

  * `-V|--verbose` - verbose mode
  * `-p|--destport` - set destination port
  * `-s|--baseport` - set source port
  * `<scan_type>` - set scan type
    * `-F|--fin` - set FIN flag, port open if no reply
    * `-S|--syn` - set SYN flag
    * `-P|--push` - set PUSH flag
    * `-A|--ack` - set ACK flag (use when ping is blocked, RST response back if the port is open)
    * `-U|--urg` - set URG flag
    * `-Y|--ymas` - set Y unused flag (0x80 - nullscan), port open if no reply
    * `-M 0 -UPF` - set TCP sequence number and scan type (URG+PUSH+FIN), port open if no reply

```bash
hping3 -V -c 1 -1 -C 8 www.google.com
```

  * `-c [num]` - packet count
  * `-1` - set ICMP mode
  * `-C|--icmptype [icmp-num]` - set icmp type (default icmp-echo = 8)

```bash
hping3 -V -c 1000000 -d 120 -S -w 64 -p 80 --flood --rand-source <remote_host>
```

  * `--flood` - sent packets as fast as possible (don't show replies)
  * `--rand-source` - random source address mode
  * `-d --data` - data size
  * `-w|--win` - winsize (default 64)

___
