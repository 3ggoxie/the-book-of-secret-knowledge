##### Tool: [diff](https://en.wikipedia.org/wiki/Diff)

###### Compare two directory trees

```bash
diff <(cd directory1 && find | sort) <(cd directory2 && find | sort)
```

###### Compare output of two commands

```bash
diff <(cat /etc/passwd) <(cut -f2 /etc/passwd)
```

___
