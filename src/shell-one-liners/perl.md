##### Tool: [perl](https://www.perl.org/)

###### Search and replace (in place)

```bash
perl -i -pe's/SEARCH/REPLACE/' filename
```

###### Edit of `*.conf` files changing all foo to bar (and backup original)

```bash
perl -p -i.orig -e 's/\bfoo\b/bar/g' *.conf
```

###### Prints the first 20 lines from `*.conf` files

```bash
perl -pe 'exit if $. > 20' *.conf
```

###### Search lines 10 to 20

```bash
perl -ne 'print if 10 .. 20' filename
```

###### Delete first 10 lines (and backup original)

```bash
perl -i.orig -ne 'print unless 1 .. 10' filename
```

###### Delete all but lines between foo and bar (and backup original)

```bash
perl -i.orig -ne 'print unless /^foo$/ .. /^bar$/' filename
```

###### Reduce multiple blank lines to a single line

```bash
perl -p -i -00pe0 filename
```

###### Convert tabs to spaces (1t = 2sp)

```bash
perl -p -i -e 's/\t/  /g' filename
```

###### Read input from a file and report number of lines and characters

```bash
perl -lne '$i++; $in += length($_); END { print "$i lines, $in characters"; }' filename
```
