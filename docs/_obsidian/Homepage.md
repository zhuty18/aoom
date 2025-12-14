---
count_ideal: 8000
count_unit: 2000
day_awhile: 60
day_ideal: 3
day_notlong: 30
day_recent: 14
max_list: 12
percent_high: 0.7
percent_ideal: 0.9
percent_low: 0.3
---

# 兔子草

## 你好！

今天是`\=dateformat(date(today),"DD，EEEE")`，你使用Obsidian的第`\=ceil((date(now)-date("2025-01-15")).days)`天。

```dataviewjs
let home = dv.current()
const { MyUtils } = await cJS()
let last = dv.pages().where(x => x.finished).sort(x => x.date ? x.date : x.auto_date, "desc")[0]
let interval = MyUtils.last_update(last)

let output = "上一次完结是" + MyUtils.last_update_str(last, home) + "。完结内容《" + last.file.link + "》 " + last.file.tags.join(" ") + " ，" + MyUtils.count_text(MyUtils.count(last)) + "。"
if (interval < home.day_recent) {
    output += "干得漂亮！"
} else if (interval < home.day_notlong) {
    output += "继续努力！"
} else if (interval < home.day_awhile) {
    output += "要加油啊！"
} else {
    output += "唉！"
}
dv.paragraph(output)

let all_data = MyUtils.pages_raw_data(dv.pages(), home)
let percent = all_data.fin_percent
output = `你在这里有${all_data.tbc}个坑，${all_data.fin}个已完结，完结率${MyUtils.percent_meter(percent, home)}，`
if (percent > home.percent_high) {
    output += "了不起！"
} else if (percent > home.percent_low) {
    output += "不愧是你！"
} else {
    output += "可以的！"
}
dv.paragraph(output)

output = `总字数${MyUtils.count_text(all_data.fin_count)}，完结字数比${MyUtils.percent_meter(all_data.fin_count / all_data.all_count, home)}，平均完结字数${MyUtils.count_text(all_data.fin_count_avg)}<progress value=${all_data.fin_count_avg} min=0 max=${home.count_ideal}></progress>。`
dv.paragraph(output)
```

### 正在进行

```dataviewjs
let home = dv.current()
const { MyUtils } = await cJS()
let recent_pages = MyUtils.work_of(dv.pages().where(x => !x.finished), home.max_list)
dv.list(recent_pages.map(x => MyUtils.short_text(x, home)))
```

### AI评论

```dataviewjs
let home = dv.current()
const { MyUtils } = await cJS()
let finished = dv.pages().where(x => x.finished).sort(x => x.date ? x.date : x.auto_date, "desc").limit(home.max_list)
let ai = dv.pages('"AI"')

function info (x,ai) {
  let ai_one = ai.filter((y) => x.file.name==y.file.name)
  return [x.file.name,x.file.tags.join(" "),`[${ai_one.length>0?"🔋 By ":"🪫"}${ai_one.author.join("")}](AI/${x.file.name.replaceAll(" ","%20")})`]
}

dv.list(finished.map((x) => info(x,ai).join(" ")))
```

### 最近更新

```dataviewjs
let home = dv.current()
const { MyUtils } = await cJS()
let recent_pages = MyUtils.work_of(dv.pages().where(x => MyUtils.last_update(x) < home.day_notlong), home.max_list)
dv.table(["文件", "进度", "更新"], recent_pages.map(x => [x.file.link, MyUtils.count_meter(x, home, 2), MyUtils.last_update_str(x, home)]))
```

### 坑品概览

```dataviewjs
const { MyUtils } = await cJS()
let folders = MyUtils.work_of(dv.pages()).file.folder.distinct()
let tbc_folders = MyUtils.work_of(dv.pages().where(x => !x.finished)).file.folder.distinct()
dv.paragraph("你创建了" + folders.length + "个文件夹，" + tbc_folders.length + "个有坑。")
```

>[!abstract]- 有坑文件夹一览
>
> ```dataviewjs
> let home = dv.current()
> const { MyUtils } = await cJS()
> let folders = MyUtils.work_of(dv.pages().where(x => !x.finished)).file.folder.distinct()
> dv.table(["文件夹", "坑数", "完结率", "坑字数", "完结字数比", "平均完结字数"], folders.sort(x => MyUtils.work_of(dv.pages().where(y => y.file.folder.indexOf(x) >= 0)).length, "desc").map(x => MyUtils.pages_data(dv.pages().where(y => y.file.folder.indexOf(x) >= 0), x, home)))
> ```

```dataviewjs
const { MyUtils } = await cJS()
let tags = MyUtils.work_of(dv.pages()).file.tags.distinct()
let tbc_tags = MyUtils.work_of(dv.pages().where(x => !x.finished)).file.tags.distinct()
dv.paragraph("你创建了" + tags.length + "个标签，" + tbc_tags.length + "个有坑。")
```

>[!cite]- 有坑标签一览
>
> ```dataviewjs
> let home = dv.current()
> const { MyUtils } = await cJS()
> let tags = MyUtils.work_of(dv.pages().where(x => !x.finished)).file.tags.distinct()
> dv.table(["标签", "坑数", "完结率", "坑字数", "完结字数比", "平均完结字数"], tags.sort(x => MyUtils.work_of(dv.pages(x)).length, "desc").map(x => MyUtils.pages_data(dv.pages(x), x, home)))
> ```

## 2025蝙绿企划

### 目标

```dataviewjs
let home = dv.current()
const { MyUtils } = await cJS()
let all_data = MyUtils.pages_raw_data(dv.pages("#2025蝙绿企划"), home)
let percent = all_data.tbc_count / all_data.fin_count_theory
let output = "#2025蝙绿企划 累计写了" + MyUtils.count_text(all_data.all_count) + "，完成度" + MyUtils.percent_meter(percent, home) + "，还有" + all_data.tbc + "个坑，完结率" + MyUtils.percent_meter(all_data.fin_percent, home) + "。"
dv.paragraph(output)

let next = dv.date(dv.date("today").year + "-02-19")
if ((next - dv.date("today")) < 0) {
    next = dv.date((dv.date("today").year + 1) + "-02-19")
}
let interval = (next - dv.date("today")) / 1000 / 60 / 60 / 24
output = "估计还要写" + MyUtils.count_text(all_data.fin_count_theory - all_data.all_count) + "，距离下一个2.19还有" + interval + "天，平均每天" + MyUtils.count_text((all_data.fin_count_theory - all_data.all_count) / interval) + "。"
dv.paragraph(output)
```

### 缩略

```dataviewjs
let home = dv.current()
const { MyUtils } = await cJS()
let recent_pages = MyUtils.work_of(dv.pages('#2025蝙绿企划').where(x => !x.finished), home.max_list)
dv.list(recent_pages.map(x => MyUtils.pin_of(x, home) + x.file.link + " " + x.file.tags.filter((y) => y != "#2025蝙绿企划" && y != "#BatLantern").slice(0, 2).join(" ") + " " + MyUtils.count_meter(x, home)))
```

### 总表

>[!example]+ 2025蝙绿企划一览
>
> ```dataviewjs
> let home = dv.current()
> const { MyUtils } = await cJS()
> let recent_pages = MyUtils.work_of(dv.pages('#2025蝙绿企划'))
> dv.table(["文件", "标签", "字数", "更新"], recent_pages.map(x => [x.file.link, x.file.tags.filter((y) => y != "#2025蝙绿企划" && y != "#BatLantern").join("<br>"), MyUtils.count_meter(x, home, 2), MyUtils.last_update_str(x, home)]))
> ```

## 任务

### 待办

>[!question]- 待办事项
>
> ```dataview
> TASK
> FROM -"_obsidian"
> WHERE contains(tags,"#tasks") AND !completed AND status!="-"
> SORT status
>```

### 已完成

>[!info]- 已完成的任务
>
> ```dataview
> TASK
> FROM -"_obsidian"
> WHERE contains(tags,"#tasks") AND (completed OR status="-")
> SORT completion desc
> ```

## 总览

### 坑

```dataview
CALENDAR choice(date,date,auto_date)
WHERE typeof(choice(date,date,auto_date)) = "date" and word_count and !finished
```

>[!tldr]- 坑一览
>
> ```dataviewjs
> let home = dv.current()
> const { MyUtils } = await cJS()
> let recent_pages = MyUtils.work_of(dv.pages().where(x => !x.finished))
> dv.table(["文件", "标签", "字数", "更新"], recent_pages.map(x => [x.file.link, x.file.tags.join("<br>"), MyUtils.count_meter(x, home, 2), MyUtils.last_update_str(x, home)]))
> ```

### 已完结

```dataview
CALENDAR choice(date,date,auto_date)
WHERE typeof(choice(date,date,auto_date)) = "date" and word_count and finished
```

>[!tldr]- 完结一览
>
> ```dataviewjs
> let home = dv.current()
> const { MyUtils } = await cJS()
> let recent_pages = MyUtils.work_of(dv.pages().where(x => x.finished))
> dv.table(["文件", "标签", "字数", "更新"], recent_pages.map(x => [x.file.link, x.file.tags.join("<br>"), MyUtils.count(x), MyUtils.last_update_str(x, home)]))
> ```
