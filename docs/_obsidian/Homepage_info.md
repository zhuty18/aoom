---
ideal_count: 8000
ideal_percent: 0.85
low_percent: 0.3
high_percent: 0.75
recent_day: 14
notlong_day: 40
awhile_day: 90
---

# 兔子草

## 你好！

今天是你使用Obsidian的第`\=ceil((date(now)-date("2025-01-15")).days)`天。

```dataviewjs
let last = dv.pages("#FIN").where((x) => x.word_count).sort((x) => x.date ? x.date : x.auto_date, "desc")[0]
let interval = (dv.date("today") - dv.date(last.date ? last.date : last.auto_date)) / 1000 / 60 / 60 / 24

let this_page = dv.current()
let output = "上一次完结是" + interval + "天前。完结内容" + last.file.link + "， " + last.file.tags.filter((x) => x != ("#FIN")).join(" ") + " "
if (interval < this_page.recent_day) {
output += "干得漂亮！"
} else if (interval < this_page.notlong_day) {
output += "继续努力！"
} else if (interval < this_page.awhile_day) {
output += "要加油啊！"
} else {
output += "唉！"
}
dv.paragraph(output)

let unfin = dv.pages('-#FIN and -"trash"').where((x) => x.word_count)
let fin = dv.pages('#FIN and -"trash"').where((x) => x.word_count)
let all = dv.pages('-"trash"').where((x) => x.word_count)
let percent = fin.length/all.length
output = "你在这里有"+unfin.length+"个坑，"+fin.length+"个 #FIN ，完结率"+Math.round(percent*1000)/10+"%，"
if (percent > this_page.high_percent) {
output += "了不起！"
} else if (percent > this_page.low_percent) {
output += "不愧是你！"
} else {
output += "可以的！"
}
dv.paragraph(output)

output = "你的完结作品中，平均完结字数为"+Math.round(fin.word_count.avg())+"。"
output += "<progress value="+fin.word_count.avg()+" min=0 max="+this_page.ideal_count+"></progress>"
dv.paragraph(output)

let tags=dv.pages().where((x) => x.word_count).file.tags.distinct()
dv.paragraph("你创建了"+tags.length+"个标签。")
```

## 最近更新

```dataview
TABLE WITHOUT ID
file.link as 文件,
word_count+"<br><meter value="+ word_count/max(this.ideal_count,word_count/this.ideal_percent) + " max=1 min=0 low="+this.low_percent+" high="+this.high_percent+" optimum="+this.ideal_percent+"></meter>" as 进度,
(date(today)-choice(date,date,auto_date)).day + "天前" as 更新
FROM -#FIN and -"trash"
WHERE word_count and (date(today)-choice(date,date,auto_date)).day < this.notlong_day and choice(date,date,auto_date)
SORT choice(date,date,auto_date) DESC
LIMIT 15
```

## 坑品概览

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

# 2025蝙绿企划

## 概述

#2025蝙绿企划 累计写了`$=Math.round(dv.pages('#2025蝙绿企划').where((x) => x.word_count).word_count.sum()/100)/100`万字，完结率`$=Math.round((dv.pages('#2025蝙绿企划 and #FIN').where((x) => x.word_count).length/dv.pages('#2025蝙绿企划').where((x) => x.word_count).length)*1000)/10`%，还有`$=dv.pages('#2025蝙绿企划 and -#FIN').where((x) => x.word_count).length`个坑。`$="<progress value="+(dv.pages('#2025蝙绿企划 and #FIN').where((x) => x.word_count).length)+" max="+dv.pages('#2025蝙绿企划').where((x) => x.word_count).length+"></progress>"`

## 文字

```dataview
LIST WITHOUT ID
"- ["+choice((date(now)-date(choice(date,date,auto_date))).day < 3,"f","b")+"] " +
file.link + " " +
filter(file.tags,(x) => !contains(x,"2025蝙绿企划")&!contains(x,"BatLantern")&!contains(x,"FIN")) +
" <meter value="+ word_count/max(this.ideal_count,word_count/this.ideal_percent) + " max=1 min=0 low="+this.low_percent+" high="+this.high_percent+" optimum="+this.ideal_percent+"></meter> " +
word_count + "字"
FROM #2025蝙绿企划
WHERE word_count
SORT choice(date,date,auto_date) DESC
SORT contains(file.tags,"FIN")
LIMIT 5
```

## 总表

>[!example]+ 2025蝙绿企划一览
>
> ```dataview
> TABLE WITHOUT ID
> file.link as 文件,
> join(filter(file.tags,(x) => !contains(x,"2025蝙绿企划")&!contains(x,"BatLantern")&!contains(x,"FIN")),"<br>") as 标签,
> word_count as 字数,
> "<meter value="+ word_count/max(this.ideal_count,word_count/this.ideal_percent) + " max=1 min=0 low="+this.low_percent+" high="+this.high_percent+" optimum="+this.ideal_percent+"></meter>" as 进度,
> ceil((date(now)-choice(date,date,auto_date)).day) + "天前" as 更新于
> FROM #2025蝙绿企划
> WHERE word_count
> SORT choice(date,date,auto_date) DESC
> SORT contains(file.tags,"FIN")
> ```

# 任务

## 当前任务

```tasks
FILTER BY FUNCTION task.status.symbol == "!" || task.status.symbol == "*"
(due this week) OR (no due date)
SORT BY FUNCTION task.status.symbol
```

## 待办

```tasks
FILTER BY FUNCTION (task.status.symbol != "!" && task.status.symbol != "*" && task.status.type == "IN_PROGRESS" )|| task.status.type == "TODO"
SORT BY FUNCTION task.status.symbol
```

## 脑洞

```tasks
FILTER BY FUNCTION task.status.type == "NON_TASK"
```

## 已完成

>[!info]- 已完成的任务
>
> ```tasks
> DONE
> FILTER BY FUNCTION task.status.type!="NON_TASK"
> SORT BY done REVERSE
> HIDE EDIT BUTTON
> ```

# 随笔

![随笔](write_down.md)

# 总览

## 坑

```dataview
CALENDAR choice(date,date,auto_date)
FROM -#FIN
WHERE typeof(choice(date,date,auto_date)) = "date" and word_count
```

>[!important]- 坑一览
>
> ```dataview
> TABLE WITHOUT ID
> file.link as 文件,
> join(filter(file.tags,(x) => !contains(x,"2025蝙绿企划")),"<br>") as 标签,
> word_count as 字数,
> "<meter value="+ word_count/max(this.ideal_count,word_count/this.ideal_percent) + " max=1 min=0 low="+this.low_percent+" high="+this.high_percent+" optimum="+this.ideal_percent+"></meter>" as 进度,
> floor((date(now)-choice(date,date,auto_date)).day) + "天前" as 更新于
> FROM -#FIN and -"trash"
> WHERE word_count
> SORT choice(date,date,auto_date) DESC
> ```

## 已完结

```dataview
CALENDAR choice(date,date,auto_date)
FROM #FIN
WHERE typeof(choice(date,date,auto_date)) = "date" and word_count
```

>[!important]- 完结一览
>
> ```dataview
> TABLE WITHOUT ID
> file.link as 文件,
> join(filter(file.tags,(x) => !contains(x,"FIN")),"<br>") as 标签,
> word_count as 字数,
> (date(today)-choice(date,date,auto_date)).day+ "天前" as 更新于
> FROM #FIN and -"trash"
> WHERE word_count
> SORT choice(date,date,auto_date) DESC
> ```
