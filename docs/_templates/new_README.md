# <% tp.file.folder() %>

## 未完结

```dataviewjs
let home = dv.page("/_obsidian/Homepage")
const { MyUtils } = await cJS()
let pages = MyUtils.work_of(dv.pages('"<% tp.file.folder() %>"')).where((x) => x.word_count && (!x.finished))

dv.table(["文件", "标签", "字数", "更新"], pages.map(x => [x.file.link, x.file.tags.join("<br>"), MyUtils.count_meter(x, home, 2), MyUtils.last_update_str(x, home)]))
```

## 已完结

```dataviewjs
let home = dv.page("/_obsidian/Homepage")
const { MyUtils } = await cJS()
let pages = MyUtils.work_of(dv.pages('"<% tp.file.folder() %>"')).where((x) => x.word_count && x.finished)

dv.table(["文件", "标签", "字数", "更新"], pages.map(x => [x.file.link, x.file.tags.join("<br>"), MyUtils.count_meter(x, home, 2), MyUtils.last_update_str(x, home)]))
```
