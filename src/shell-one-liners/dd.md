##### Tool: [dd](https://en.wikipedia.org/wiki/Dd_(Unix))

###### Show dd status every so often

```bash
dd <dd_params> status=progress
watch --interval 5 killall -USR1 dd
```

###### Redirect output to a file with dd

```bash
echo "string" | dd of=filename
```

___
