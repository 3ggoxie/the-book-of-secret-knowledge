##### Tool: [vimdiff](http://vimdoc.sourceforge.net/htmldoc/diff.html)

###### Highlight the exact differences, based on characters and words

```bash
vimdiff file1 file2
```

###### Compare two JSON files

```bash
vimdiff <(jq -S . A.json) <(jq -S . B.json)
```

###### Compare Hex dump

```bash
d(){ vimdiff <(f $1) <(f $2);};f(){ hexdump -C $1 | cut -d' ' -f3- | tr -s ' ';}; d ~/bin1 ~/bin2
```

###### diffchar

Save [diffchar](https://raw.githubusercontent.com/vim-scripts/diffchar.vim/master/plugin/diffchar.vim) @ `~/.vim/plugins`

Click `F7` to switch between diff modes

Usefull `vimdiff` commands:

* `qa` to exit all windows
* `:vertical resize 70` to resize window
* set window width `Ctrl+W [N columns]+(Shift+)<\>`

___
