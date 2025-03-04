---
word_count: 307
auto_date: 2025-03-04
---

# 你好！

今天是你使用Obsidian的第`\=ceil((date(now)-date("2025-01-15")).days)`天。

你在这里有`$=dv.pages("-#FIN").where((x) => x.word_count).length`个坑，`$=dv.pages("#FIN").length`个 #FIN ，完结率`$=Math.round((dv.pages("-#FIN").where((x) => x.word_count).length/dv.pages("").where((x) => x.word_count).length)*1000)/10`%，不愧是你！

```dataview
TABLE WITHOUT ID
key as 文件名,
length(filter(rows,(x) => !contains(x.tags,"FIN"))) as 坑数,
round((length(filter(rows,(x) => contains(x.tags,"FIN")))/length(rows))*100,1)+"%" as 完结率,
round(sum(filter(rows,(x) => !contains(x.tags,"FIN")).word_count)/10000,1)+"万" as 坑字数,
round(sum(filter(rows,(x) => contains(x.tags,"FIN")).word_count)/sum(rows.word_count)*100,1)+"%" as 完结字数比
FROM -"trash"
WHERE word_count
GROUP BY file.folder
SORT length(rows) DESC
LIMIT 3
```

## 重要任务

```tasks
FILTER BY FUNCTION task.status.symbol == "!" || task.status.symbol == "*"
(due this week) OR (no due date)
SORT BY FUNCTION task.status.symbol
```

## 2025蝙绿企划

#2025蝙绿企划 有`$=dv.pages('#2025蝙绿企划 and -#FIN').where((x) => x.word_count).length`个坑，完结率`$=Math.round(dv.pages('#FIN and #2025蝙绿企划').where((x) => x.word_count).length/dv.pages('#2025蝙绿企划').where((x) => x.word_count).length*1000)/10`%。你写了`$=Math.round(dv.pages("#2025蝙绿企划").where((x) => x.word_count).word_count.sum()/100)/100`万字。

```dataview
LIST WITHOUT ID
choice((date(now)-date(choice(date,date,auto_date))).day < 3,"- [f]","- [b]") + " " +
file.link + " " +
filter(file.tags,(x) => !contains(x,"2025蝙绿企划")&!contains(x,"BatLantern")&!contains(x,"FIN")) + " " +
length + "字 " +
dateformat(choice(date,date,auto_date),"yy.M.d")
FROM #2025蝙绿企划
WHERE !contains(file.path,"logs") and !contains(file.name,"todo")
SORT choice(date,date,auto_date) DESC
SORT contains(file.tags,"FIN")
LIMIT 4
```

## 待办事项

```tasks
FILTER BY FUNCTION (task.status.symbol != "!" && task.status.symbol != "*" && task.status.type == "IN_PROGRESS" )|| task.status.type == "TODO"
SORT BY FUNCTION task.status.symbol
```

## 脑洞

```tasks
FILTER BY FUNCTION task.status.type == "NON_TASK"
```

## 已完成

```tasks
DONE
FILTER BY FUNCTION task.status.type!="NON_TASK"
SORT BY done REVERSE
HIDE EDIT BUTTON
```

