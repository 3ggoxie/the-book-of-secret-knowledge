##### Tool: [who](https://en.wikipedia.org/wiki/Who_(Unix))

###### Find last reboot time

```bash
who -b
```

###### Detect a user sudo-su'd into the current shell

```bash
[[ $(who -m | awk '{ print $1 }') == $(whoami) ]] || echo "You are su-ed to $(whoami)"
```

___
