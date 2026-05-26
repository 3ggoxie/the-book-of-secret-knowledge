##### Tool: [grep](http://www.grymoire.com/Unix/Grep.html)

###### Search for a "pattern" inside all files in the current directory

```bash
grep -rn "pattern"
grep -RnisI "pattern" *
fgrep "pattern" * -R
```

###### Show only for multiple patterns

```bash
grep 'INFO*'\''WARN' filename
grep 'INFO\|WARN' filename
grep -e INFO -e WARN filename
grep -E '(INFO|WARN)' filename
egrep "INFO|WARN" filename
```

###### Except multiple patterns

```bash
grep -vE '(error|critical|warning)' filename
```

###### Show data from file without comments

```bash
grep -v ^[[:space:]]*# filename
```

###### Show data from file without comments and new lines

```bash
egrep -v '#|^$' filename
```

###### Show strings with a dash/hyphen

```bash
grep -e -- filename
grep -- -- filename
grep "\-\-" filename
```

###### Remove blank lines from a file and save output to new file

```bash
grep . filename > newfilename
```
