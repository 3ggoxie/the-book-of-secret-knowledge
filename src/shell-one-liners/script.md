##### Tool: [script](https://en.wikipedia.org/wiki/Script_(Unix))

###### Record and replay terminal session

```bash
### Record session
# 1)
script -t 2>~/session.time -a ~/session.log

# 2)
script --timing=session.time session.log

### Replay session
scriptreplay --timing=session.time session.log
```

___
