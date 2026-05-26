##### Tool: [last](https://www.howtoforge.com/linux-last-command/)

###### Was the last reboot a panic?

```bash
(last -x -f $(ls -1t /var/log/wtmp* | head -2 | tail -1); last -x -f /var/log/wtmp) | \
grep -A1 reboot | head -2 | grep -q shutdown && echo "Expected reboot" || echo "Panic reboot"
```

___
