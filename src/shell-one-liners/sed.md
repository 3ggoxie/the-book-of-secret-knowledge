##### Tool: [sed](http://www.grymoire.com/Unix/Sed.html)

###### Print a specific line from a file

```bash
sed -n 10p /path/to/file
```

###### Remove a specific line from a file

```bash
sed -i 10d /path/to/file
# alternative (BSD): sed -i'' 10d /path/to/file
```

###### Remove a range of lines from a file

```bash
sed -i <file> -re '<start>,<end>d'
```

###### Replace newline(s) with a space

```bash
sed ':a;N;$!ba;s/\n/ /g' /path/to/file

# cross-platform compatible syntax:
sed -e ':a' -e 'N' -e '$!ba' -e 's/\n/ /g' /path/to/file
```

- `:a` create a label `a`
- `N` append the next line to the pattern space
- `$!` if not the last line, ba branch (go to) label `a`
- `s` substitute, `/\n/` regex for new line, `/ /` by a space, `/g` global match (as many times as it can)

Alternatives:

```bash
# perl version (sed-like speed):
perl -p -e 's/\n/ /' /path/to/file

# bash version (slow):
while read line ; do printf "%s" "$line " ; done < file
```

###### Delete string +N next lines

```bash
sed '/start/,+4d' /path/to/file
```

___
