##### Tool: [git](https://git-scm.com/)

###### Log alias for a decent view of your repo

```bash
# 1)
git log --oneline --decorate --graph --all

# 2)
git log --graph \
--pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' \
--abbrev-commit
```

___
