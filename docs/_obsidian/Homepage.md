---
count_ideal: 8000
day_awhile: 90
day_ideal: 3
day_notlong: 30
day_recent: 14
max_list: 12
percent_high: 0.75
percent_ideal: 0.85
percent_low: 0.3
---

# 兔子草

## 你好！

今天是`\=dateformat(date(today),"DD，EEEE")`，你使用Obsidian的第`\=ceil((date(now)-date("2025-01-15")).days)`天。

当前运势`dice:1d100`：写文`dice: 1d100`，摸鱼`dice: 1d100`，干点正事`dice:1d100`。

```dataviewjs
let last = dv.pages("#FIN").where((x) => x.word_count).sort((x) => x.date ? x.date : x.auto_date, "desc")[0]
let interval = (dv.date("today") - dv.date(last.date ? last.date : last.auto_date)) / 1000 / 60 / 60 / 24

let this_page = dv.current()
let output = "上一次完结是" + interval + "天前。完结内容《" + last.file.link + "》， " + last.file.tags.filter((x) => x != ("#FIN")).join(" ") + " "
if (interval < this_page.day_recent) {
output += "干得漂亮！"
} else if (interval < this_page.day_notlong) {
output += "继续努力！"
} else if (interval < this_page.day_awhile) {
output += "要加油啊！"
} else {
output += "唉！"
}
dv.paragraph(output)

let unfin = dv.pages('-#FIN and -"trash"').where((x) => x.word_count)
let fin = dv.pages('#FIN and -"trash"').where((x) => x.word_count)
let all = dv.pages('-"trash"').where((x) => x.word_count)
let percent = fin.length / all.length
output = "你在这里有" + unfin.length + "个坑，" + fin.length + "个 #FIN ，完结率" + Math.round(percent * 1000) / 10 + "%<meter value=" + percent + " min=0 max=1 low=" + this_page.percent_low + " high=" + this_page.percent_high + " optimum=" + this_page.percent_ideal + "></meter>，"
if (percent > this_page.percent_high) {
output += "了不起！"
} else if (percent > this_page.percent_low) {
output += "不愧是你！"
} else {
output += "可以的！"
}
dv.paragraph(output)

output = "你的完结作品中，平均完结字数为" + Math.round(fin.word_count.avg()) + "。"
output += "<progress value=" + fin.word_count.avg() + " min=0 max=" + this_page.count_ideal + "></progress>"
dv.paragraph(output)

let tags = dv.pages().where((x) => x.word_count).file.tags.distinct()
dv.paragraph("你创建了" + tags.length + "个标签。")
```

>[!cite]- 所有标签
>`$=dv.pages('-"trash"').where((x) => x.word_count).file.tags.distinct().join(" ")`

### 正在进行

```dataviewjs
let home = dv.current()
var utils = require(app.vault.adapter.basePath + "/_obsidian/utils.js")
let recent_pages = utils.work_of(dv.pages("-#FIN"),dv.current().max_list)
dv.list(recent_pages.map((x) => utils.short_text(x,home)))
```

### 最近更新

```dataviewjs
let home = dv.current()
var utils = require(app.vault.adapter.basePath + "/_obsidian/utils.js")
let recent_pages = utils.work_of(dv.pages().where((x) => utils.last_update(x)< home.day_notlong),dv.current().max_list)
dv.table(["文件", "进度", "更新"], recent_pages.map((x) => [x.file.link,utils.count(x,home)+"<br>"+utils.count_meter(x,home),utils.last_update_str(x,home)]))
```

### 坑品概览

>[!abstract]- 坑品概览
>
> ```dataview
> TABLE WITHOUT ID
> key as 类别,
> length(filter(rows,(x) => !contains(x.tags,"FIN"))) as 坑数,
> round((length(filter(rows,(x) => contains(x.tags,"FIN")))/length(rows))*100,1)+"%" as 完结率,
> round(sum(filter(rows,(x) => !contains(x.tags,"FIN")).word_count)/10000,1)+"万" as 坑字数,
> round(sum(filter(rows,(x) => contains(x.tags,"FIN")).word_count)/sum(rows.word_count)*100,1)+"%" as 完结字数比,
> round(sum(filter(rows,(x) => contains(x.tags,"FIN")).word_count)/length(filter(rows,(x) => contains(x.tags,"FIN")))) as 平均完结字数
> FROM -"trash"
> WHERE word_count
> GROUP BY file.folder
> SORT length(rows) DESC
> ```

## 2025蝙绿企划

### 目标

```dataviewjs
let unfin = dv.pages('#2025蝙绿企划 and -#FIN').where((x) => x.word_count)
let fin = dv.pages('#2025蝙绿企划 and #FIN').where((x) => x.word_count)
let all = dv.pages('#2025蝙绿企划').where((x) => x.word_count)
let this_page = dv.current()
let theory = unfin.map((x) => Math.max(this_page.count_ideal, x.word_count / this_page.percent_ideal)).sum()
let percent = all.word_count.sum() / (theory + fin.word_count.sum())
let output = "#2025蝙绿企划 累计写了" + Math.round(all.word_count.sum() / 100) / 100 + "万字，完成度" + Math.round(percent * 1000) / 10 + "%，完结率" + Math.round(fin.length / all.length * 1000) / 10 + "%。还有" + unfin.length + "个坑，估计还要写" + Math.round(theory / 100) / 100 + "万字。<meter value=" + percent + " min=0 max=1 low=" + this_page.percent_low + " high=" + this_page.percent_high + " optimum=" + this_page.percent_ideal + "></meter>"
dv.paragraph(output)
```

### 缩略

```dataviewjs
let home = dv.current()
var utils = require(app.vault.adapter.basePath + "/_obsidian/utils.js")
let recent_pages = utils.work_of(dv.pages('#2025蝙绿企划 and -#FIN'), home.max_list)
dv.list(recent_pages.map((x) => utils.pin_of(x, home) + x.file.link + x.file.tags.filter((y) => y != "#FIN" && y != "#2025蝙绿企划" && y != "#BatLantern").slice(0, 2).join(" ") + utils.count_meter(x, home)))
```

### 总表

>[!example]+ 2025蝙绿企划一览
>
> ```dataviewjs
> let home = dv.current()
> var utils = require(app.vault.adapter.basePath + "/_obsidian/utils.js")
> let recent_pages=utils.work_of(dv.pages('#2025蝙绿企划'),-1)
> dv.table(["文件", "标签", "字数", "进度", "更新"], recent_pages.map((x) => [x.file.link,x.file.tags.filter((y) => y != "#FIN" && y != "#2025蝙绿企划" && y != "#BatLantern").join("<br>"),utils.count(x),utils.count_meter(x,home),utils.last_update_str(x)]))
> ```

## 任务

### 重要任务

```tasks
FILTER BY FUNCTION task.status.symbol == "!"
```

### 当前任务

```tasks
FILTER BY FUNCTION task.status.symbol == "!" || task.status.symbol == "*"
(due this week) OR (no due date)
SORT BY FUNCTION task.status.symbol
```

### 待办

```tasks
FILTER BY FUNCTION (task.status.symbol != "!" && task.status.symbol != "*" && task.status.type == "IN_PROGRESS" )|| task.status.type == "TODO"
SORT BY FUNCTION task.status.symbol
```

### 灵感

```tasks
FILTER BY FUNCTION task.status.type == "NON_TASK"
```

### 已完成

>[!info]- 已完成的任务
>
> ```tasks
> DONE
> FILTER BY FUNCTION task.status.type!="NON_TASK"
> SORT BY done REVERSE
> HIDE EDIT BUTTON
> ```

## 随笔

![随笔](write_down.md)

## 总览

### 坑

```dataview
CALENDAR choice(date,date,auto_date)
FROM -#FIN
WHERE typeof(choice(date,date,auto_date)) = "date" and word_count
```

>[!tldr]- 坑一览
>
> ```dataviewjs
> let home = dv.current()
> var utils = require(app.vault.adapter.basePath + "/_obsidian/utils.js")
> let recent_pages=utils.work_of(dv.pages('-#FIN'),-1)
> dv.table(["文件", "标签", "字数", "进度", "更新"], recent_pages.map((x) => [x.file.link,x.file.tags.join("<br>"),utils.count(x),utils.count_meter(x,home),utils.last_update_str(x)]))
> ```

### 已完结

```dataview
CALENDAR choice(date,date,auto_date)
FROM #FIN
WHERE typeof(choice(date,date,auto_date)) = "date" and word_count
```

>[!tldr]- 完结一览
>
> ```dataviewjs
> let home = dv.current()
> var utils = require(app.vault.adapter.basePath + "/_obsidian/utils.js")
> let recent_pages=utils.work_of(dv.pages('#FIN'),-1)
> dv.table(["文件", "标签", "字数", "更新"], recent_pages.map((x) => [x.file.link,x.file.tags.filter((y) => y != "#FIN").join("<br>"),utils.last_update_str(x)]))
> ```
