# 你好！

今天是你使用Obsidian的第`\=ceil((date(now)-date("2025-01-15")).days)`天。

你在这里有`$=dv.pages('-#FIN and -"trash"').where((x) => x.word_count).length`个坑，`$=dv.pages('#FIN and -"trash"').length`个 #FIN ，完结率`$=Math.round((dv.pages('-#FIN and -"trash"').where((x) => x.word_count).length/dv.pages('-"trash"').where((x) => x.word_count).length)*1000)/10`%，不愧是你！

你的完结作品中，平均完结字数为`$=Math.round(dv.pages('#FIN and -"trash"').where((x) => x.word_count).word_count.sum()/dv.pages('-"trash" and #FIN').where((x) => x.word_count).length)`。

你创建了`$=dv.pages().where((x) => x.word_count).file.tags.distinct().length`个标签。`$=dv.pages().where((x) => x.word_count).file.tags.distinct()`

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

### 概述

#2025蝙绿企划 累计写了`$=Math.round(dv.pages('#2025蝙绿企划').where((x) => x.word_count).word_count.sum()/100)/100`万字，完结率`$=Math.round((dv.pages('#2025蝙绿企划 and #FIN').where((x) => x.word_count).length/dv.pages('#2025蝙绿企划').where((x) => x.word_count).length)*1000)/10`%，还有`$=dv.pages('#2025蝙绿企划 and -#FIN').where((x) => x.word_count).length`个坑。`$="<progress value="+(dv.pages('#2025蝙绿企划 and #FIN').where((x) => x.word_count).length)+" max="+dv.pages('#2025蝙绿企划').where((x) => x.word_count).length+"></progress>"`

### 文字

```dataview
LIST WITHOUT ID
"- ["+choice((date(now)-date(choice(date,date,auto_date))).day < 3,"f","b")+"] " +
file.link + " " +
filter(file.tags,(x) => !contains(x,"2025蝙绿企划")&!contains(x,"BatLantern")&!contains(x,"FIN")) +
" <meter value="+ word_count/max(8000,word_count*1.1) + " max=1 min=0 low=0.3 high=0.7 optimum=0.9></meter>" +
word_count + "字"
FROM #2025蝙绿企划
WHERE word_count
SORT choice(date,date,auto_date) DESC
SORT contains(file.tags,"FIN")
LIMIT 5
```

### 总表

>[!example]+ 2025蝙绿企划一览
>
> ```dataview
> TABLE WITHOUT ID
> file.link as 文件,
> filter(file.tags,(x) => !contains(x,"2025蝙绿企划")&!contains(x,"BatLantern")&!contains(x,"FIN")) as 标签,
> word_count as 字数,
> "<meter value="+ word_count/max(8000,word_count*1.1) + " max=1 min=0 low=0.3 high=0.7 optimum=0.9></meter>" as 进度,
> ceil((date(now)-choice(date,date,auto_date)).day) + "天前" as 更新于
> FROM #2025蝙绿企划
> WHERE word_count
> SORT choice(date,date,auto_date) DESC
> SORT contains(file.tags,"FIN")
> ```

## 任务

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

### 脑洞

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

![write_down](write_down.md)

## 坑

>[!important]- 坑一览
>
> ```dataview
> TABLE WITHOUT ID
> file.link as 文件,
> filter(file.tags,(x) => !contains(x,"2025蝙绿企划")&!contains(x,"BatLantern")&!contains(x,"FIN")) as 标签,
> word_count as 字数,
> "<meter value="+ word_count/max(8000,word_count*1.1) + " max=1 min=0 low=0.3 high=0.7 optimum=0.9></meter>" as 进度,
> floor((date(now)-choice(date,date,auto_date)).day) + "天前" as 更新于
> FROM -#FIN and -"trash"
> WHERE word_count
> SORT choice(date,date,auto_date) DESC
> ```
