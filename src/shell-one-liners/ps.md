##### Tool: [ps](https://en.wikipedia.org/wiki/Ps_(Unix))

###### Show a 4-way scrollable process tree with full details

```bash
ps awwfux | less -S
```

###### Processes per user counter

```bash
ps hax -o user | sort | uniq -c | sort -r
```

###### Show all processes by name with main header

```bash
ps -lfC nginx
```

___
