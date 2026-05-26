##### 工具: [gpg](https://www.gnupg.org/)

###### 导出公钥

```bash
gpg --export --armor "username" > username.pkey
```

  * `--export` - 导出所有密钥或特定密钥
  * `-a|--armor` - 创建 ASCII 格式输出

###### 加密文件

```bash
gpg -e -r "username" dump.sql
```

  * `-e|--encrypt` - 加密数据
  * `-r|--recipient` - 为特定用户名加密

###### 解密文件

```bash
gpg -o dump.sql -d dump.sql.gpg
```

  * `-o|--output` - 用作输出文件
  * `-d|--decrypt` - 解密数据（默认）

###### 搜索收件人

```bash
gpg --keyserver hkp://keyserver.ubuntu.com --search-keys "username"
```

  * `--keyserver` - 设置特定密钥服务器
  * `--search-keys` - 在密钥服务器上搜索密钥

###### 列出加密文件中的所有数据包

```bash
gpg --batch --list-packets archive.gpg
gpg2 --batch --list-packets archive.gpg
```

___