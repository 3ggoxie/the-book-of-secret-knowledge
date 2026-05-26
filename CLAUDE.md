# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是 **The Book of Secret Knowledge**（秘密知识全书）——一个精心整理的工具、链接和资源集合，面向系统管理员、DevOps、渗透测试人员和安全研究人员。所有内容都存放在 `README.md` 中。

## 仓库结构

- `README.md` — 唯一的核心文件，包含所有按类别组织的工具、链接和描述
- `.github/CONTRIBUTING.md` — 贡献指南
- `static/img/` — 项目预览图片

## 如何贡献

### 添加新条目

直接在 `README.md` 的相应分类章节中添加 HTML 锚点链接，遵循现有格式：

```html
&nbsp;&nbsp; <a href="https://example.com/"><b>工具名称</b></a> - 描述。<br>
```

### 提交签名要求

所有提交必须包含 signed-off 行。项目有 prepare-commit-msg 钩子自动添加，也可以手动添加：
```
signed-off-by: 姓名 <email@example.com>
```

### 链接检查

提交 PR 前，使用贡献指南中的脚本检查失效链接：

```bash
for i in $(sed -n 's/.*href="\([^"]*\).*/\1/p' README.md | grep -v "^#") ; do
  _rcode=$(curl -s -o /dev/null -w "%{http_code}" "$i")
  if [[ "$_rcode" != "2"* ]] ; then echo " -> $i - $_rcode" ; fi
done
```

## 这个项目不是什么

- 不是软件项目 — 没有构建系统、包管理器或测试运行器
- 没有 Node.js、Python 或其他运行时依赖
- Markdown 内容没有 linter 或格式化工具
- 没有 CI/CD 流水线来验证更改

## 工作流程

1. Fork 并从 `master` 分支创建新分支
2. 直接编辑 `README.md`
3. 确保提交包含 signed-off 行
4. 提交 PR 到 `master` 分支，附上一行简短描述