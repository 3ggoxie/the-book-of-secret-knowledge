##### Tool: [inotifywait](https://en.wikipedia.org/wiki/GNU_Screen)

###### Init tool everytime a file in a directory is modified

```bash
while true ; do inotifywait -r -e MODIFY dir/ && ls dir/ ; done;
```

___
