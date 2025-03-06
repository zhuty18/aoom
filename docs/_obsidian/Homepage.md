---
ideal_count: 8000
ideal_percent: 0.85
low_percent: 0.3
high_percent: 0.75
recent_day: 14
notlong_day: 30
awhile_day: 90
max_list: 12
now_day: 3
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
output = "你在这里有"+unfin.length+"个坑，"+fin.length+"个 #FIN ，完结率"+Math.round(percent*1000)/10+"%<meter value="+percent+" min=0 max=1 low="+this_page.low_percent+" high="+this_page.high_percent+" optimum="+this_page.ideal_percent+"></meter>，"
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

>[!cite]- 所有标签
>`$=dv.pages('-"trash"').where((x) => x.word_count).file.tags.distinct().join(" ")`

### 正在进行

```dataviewjs
let home=dv.current()
let recent_pages=dv.pages('-"trash" and -#FIN').where((x)=>x.word_count).sort((x)=>x.word_count,"desc").sort((x)=>x.date?x.date:x.auto_date,"desc").slice(0,home.max_list)
function out(x){
let before_days=(dv.date("today")-dv.date(x.date?x.date:x.auto_date))/1000/60/60/24
let res="- ["+(before_days<home.now_day?"f":"n")+"] "+x.file.link+" "
res += x.file.tags.slice(0,2).join(" ")
let real_time_count=Math.round(x.file.size/3-Math.min(x.file.size/6,Math.max(50,x.file.size/200)))
let count=Math.max(x.word_count,real_time_count)
res += " <meter value="+ count/Math.max(home.ideal_count,count/home.ideal_percent)+" max=1 min=0 low="+home.low_percent+" high="+home.high_percent+" optimum="+home.ideal_percent+"></meter>"
return res
}
dv.list(recent_pages.map((x)=>out(x)))
```

### 最近更新

```dataview
TABLE
round(max(word_count,round(file.size/3-min(file.size/6,max(50,file.size/200)))))+choice(contains(file.tags,"FIN"),"<br><meter value=1 max=1 optimum=1></meter>","<br><meter value="+ max(word_count,round(file.size/3-min(file.size/6,max(50,file.size/200))))/max(this.ideal_count,max(word_count,round(file.size/3-min(file.size/6,max(50,file.size/200))))/this.ideal_percent) + " max=1 min=0 low="+this.low_percent+" high="+this.high_percent+" optimum="+this.ideal_percent+"></meter>") as 进度,
(date(today)-choice(date,date,auto_date)).day + "天前" as 更新
FROM -"trash"
WHERE word_count and (date(today)-choice(date,date,auto_date)).day < this.notlong_day and choice(date,date,auto_date)
SORT word_count DESC
SORT choice(date,date,auto_date) DESC
LIMIT this.max_list
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
let theory = unfin.map((x)=>Math.max(this_page.ideal_count,x.word_count/this_page.ideal_percent)).sum()
let percent=all.word_count.sum()/(theory+fin.word_count.sum())
let output = "#2025蝙绿企划 累计写了"+Math.round(all.word_count.sum()/100)/100+"万字，完成度"+Math.round(percent*1000)/10+"%，完结率"+Math.round(fin.length/all.length*1000)/10+"%。还有"+unfin.length+"个坑，估计还要写"+Math.round(theory/100)/100+"万字。<meter value="+percent+" min=0 max=1 low="+this_page.low_percent+" high="+this_page.high_percent+" optimum="+this_page.ideal_percent+"></meter>"
dv.paragraph(output)
```

### 缩略

```dataviewjs
let home=dv.current()
let recent_pages=dv.pages('-"trash" and #2025蝙绿企划 and -#FIN').where((x)=>x.word_count).sort((x)=>x.word_count,"desc").sort((x)=>x.date?x.date:x.auto_date,"desc").slice(0,home.max_list)
function out(x){
let before_days=(dv.date("today")-dv.date(x.date?x.date:x.auto_date))/1000/60/60/24
let res="- ["+(before_days<home.now_day?"f":"n")+"] "+x.file.link+" "
res += x.file.tags.slice(0,2).join(" ")
let real_time_count=Math.round(x.file.size/3-Math.min(x.file.size/6,Math.max(50,x.file.size/200)))
let count=Math.max(x.word_count,real_time_count)
res += " <meter value="+ count/Math.max(home.ideal_count,count/home.ideal_percent)+" max=1 min=0 low="+home.low_percent+" high="+home.high_percent+" optimum="+home.ideal_percent+"></meter>"
return res
}
dv.list(recent_pages.map((x)=>out(x)))
```

### 总表

>[!example]+ 2025蝙绿企划一览
>
> ```dataview
> TABLE WITHOUT ID
> file.link as 文件,
> join(filter(file.tags,(x) => !contains(x,"2025蝙绿企划")&!contains(x,"BatLantern")&!contains(x,"FIN")),"<br>") as 标签,
> word_count as 字数,
> choice(contains(file.tags,"FIN"),"<meter value=1 max=1 optimum=1></meter>","<meter value="+ max(word_count,round(file.size/3-min(file.size/6,max(50,file.size/200))))/max(this.ideal_count,max(word_count,round(file.size/3-min(file.size/6,max(50,file.size/200))))/this.ideal_percent) + " max=1 min=0 low="+this.low_percent+" high="+this.high_percent+" optimum="+this.ideal_percent+"></meter>") as 进度,
> (date(today)-choice(date,date,auto_date)).day + "天前" as 更新于
> FROM #2025蝙绿企划
> WHERE word_count
> SORT choice(date,date,auto_date) DESC
> SORT contains(file.tags,"FIN")
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
> ```dataview
> TABLE WITHOUT ID
> file.link as 文件,
> join(filter(file.tags,(x) => !contains(x,"2025蝙绿企划")),"<br>") as 标签,
> word_count as 字数,
> "<meter value="+ word_count/max(this.ideal_count,word_count/this.ideal_percent) + " max=1 min=0 low="+this.low_percent+" high="+this.high_percent+" optimum="+this.ideal_percent+"></meter>" as 进度,
> (date(today)-choice(date,date,auto_date)).day + "天前" as 更新于
> FROM -#FIN and -"trash"
> WHERE word_count
> SORT choice(date,date,auto_date) DESC
> ```

### 已完结

```dataview
CALENDAR choice(date,date,auto_date)
FROM #FIN
WHERE typeof(choice(date,date,auto_date)) = "date" and word_count
```

>[!tldr]- 完结一览
>
> ```dataview
> TABLE WITHOUT ID
> file.link as 文件,
> join(filter(file.tags,(x) => !contains(x,"FIN")),"<br>") as 标签,
> word_count as 字数,
> (date(today)-choice(date,date,auto_date)).day + "天前" as 更新于
> FROM #FIN and -"trash"
> WHERE word_count
> SORT choice(date,date,auto_date) DESC
> ```
