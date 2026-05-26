##### 工具: [terminal](https://en.wikipedia.org/wiki/Linux_console)

###### 不退出重新加载 shell

```bash
exec $SHELL -l
```

###### 关闭 shell 但保持所有子进程运行

```bash
disown -a && exit
```

###### 不保存 shell 历史地退出

```bash
kill -9 $$
unset HISTFILE && exit
```

###### 执行分支条件

```bash
true && echo success
false || echo failed
```

###### 将 stdout 和 stderr 管道到不同的命令

```bash
some_command > >(/bin/cmd_for_stdout) 2> >(/bin/cmd_for_stderr)
```

###### 将 stdout 和 stderr 重定向到单独的文件并同时打印到屏幕

```bash
(some_command 2>&1 1>&3 | tee errorlog ) 3>&1 1>&2 | tee stdoutlog
```

###### 你最常用命令的列表

```bash
history | \
awk '{CMD[$2]++;count++;}END { for (a in CMD)print CMD[a] " " CMD[a]/count*100 "% " a;}' | \
grep -v "./" | \
column -c3 -s " " -t | \
sort -nr | nl |  head -n 20
```

###### 净化 bash 历史

```bash
function sterile() {

  history | awk '$2 != "history" { $1=""; print $0 }' | egrep -vi "\
curl\b+.*(-E|--cert)\b+.*\b*|\
curl\b+.*--pass\b+.*\b*|\
curl\b+.*(-U|--proxy-user).*:.*\b*|\
curl\b+.*(-u|--user).*:.*\b*
.*(-H|--header).*(token|auth.*)\b+.*|\
wget\b+.*--.*password\b+.*\b*|\
http.?://.+:.+@.*\
" > $HOME/histbuff; history -r $HOME/histbuff;

}

export PROMPT_COMMAND="sterile"
```

  > 另请参阅: [A naive utility to censor credentials in command history](https://github.com/lbonanomi/go/blob/master/revisionist.go).

###### 快速备份文件

```bash
cp filename{,.orig}
```

###### 清空一个文件（截断到 0 大小）

```bash
>filename
```

###### 删除文件夹中不匹配特定文件扩展名的所有文件

```bash
rm !(*.foo|*.bar|*.baz)
```

###### 传递多行字符串到文件

```bash
# cat  >filename ... - 覆盖文件
# cat >>filename ... - 追加到文件
cat > filename << __EOF__
data data data
__EOF__
```

###### 使用 vim 编辑远程主机上的文件

```bash
vim scp://user@host//etc/fstab
```

###### 创建目录并同时进入

```bash
mkd() { mkdir -p "$@" && cd "$@"; }
```

###### 将大写文件名转换为小写

```bash
rename 'y/A-Z/a-z/' *
```

###### 在终端上打印一行字符

```bash
printf "%`tput cols`s" | tr ' ' '#'
```

###### 显示不带行号的 shell 历史

```bash
history | cut -c 8-
fc -l -n 1 | sed 's/^\s*//'
```

###### 退出会话后运行命令

```bash
cat > /etc/profile << __EOF__
_after_logout() {

  username=$(whoami)

  for _pid in $(ps afx | grep sshd | grep "$username" | awk '{print $1}') ; do

    kill -9 $_pid

  done

}
trap _after_logout EXIT
__EOF__
```

###### 生成数字序列

```bash
for ((i=1; i<=10; i+=2)) ; do echo $i ; done
# alternative: seq 1 2 10

for ((i=5; i<=10; ++i)) ; do printf '%02d\n' $i ; done
# alternative: seq -w 5 10

for i in {1..10} ; do echo $i ; done
```

###### 简单的 Bash 文件监视

```bash
unset MAIL; export MAILCHECK=1; export MAILPATH='$FILE_TO_WATCH?$MESSAGE'
```

___