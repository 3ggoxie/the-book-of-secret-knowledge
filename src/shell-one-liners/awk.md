##### Tool: [awk](http://www.grymoire.com/Unix/Awk.html)

###### Search for matching lines

```bash
# egrep foo
awk '/foo/' filename
```

###### Search non matching lines

```bash
# egrep -v foo
awk '!/foo/' filename
```

###### Print matching lines with numbers

```bash
# egrep -n foo
awk '/foo/{print FNR,$0}' filename
```

###### Print the last column

```bash
awk '{print $NF}' filename
```

###### Find all the lines longer than 80 characters

```bash
awk 'length($0)>80{print FNR,$0}' filename
```

###### Print only lines of less than 80 characters

```bash
awk 'length < 80' filename
```

###### Print double new lines a file

```bash
awk '1; { print "" }' filename
```

###### Print line numbers

```bash
awk '{ print FNR "\t" $0 }' filename
awk '{ printf("%5d : %s\n", NR, $0) }' filename   # in a fancy manner
```

###### Print line numbers for only non-blank lines

```bash
awk 'NF { $0=++a " :" $0 }; { print }' filename
```

###### Print the line and the next two (i=5) lines after the line matching regexp

```bash
awk '/foo/{i=5+1;}{if(i){i--; print;}}' filename
```

###### Print the lines starting at the line matching 'server {' until the line matching '}'

```bash
awk '/server {/,/}/' filename
```

###### Print multiple columns with separators

```bash
awk -F' ' '{print "ip:\t" $2 "\n port:\t" $3' filename
```

###### Remove empty lines

```bash
awk 'NF > 0' filename

# alternative:
awk NF filename
```

###### Delete trailing white space (spaces, tabs)

```bash
awk '{sub(/[ \t]*$/, "");print}' filename
```

###### Delete leading white space

```bash
awk '{sub(/^[ \t]+/, ""); print}' filename
```

###### Remove duplicate consecutive lines

```bash
# uniq
awk 'a !~ $0{print}; {a=$0}' filename
```

###### Remove duplicate entries in a file without sorting

```bash
awk '!x[$0]++' filename
```

###### Exclude multiple columns

```bash
awk '{$1=$3=""}1' filename
```

###### Substitute foo for bar on lines matching regexp

```bash
awk '/regexp/{gsub(/foo/, "bar")};{print}' filename
```

###### Add some characters at the beginning of matching lines

```bash
awk '/regexp/{sub(/^/, "++++"); print;next;}{print}' filename
```

###### Get the last hour of Apache logs

```bash
awk '/'$(date -d "1 hours ago" "+%d\\/%b\\/%Y:%H:%M")'/,/'$(date "+%d\\/%b\\/%Y:%H:%M")'/ { print $0 }' \
/var/log/httpd/access_log
```

___
