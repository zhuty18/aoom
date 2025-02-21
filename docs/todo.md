# TODO

## 重要任务

```tasks
FILTER BY FUNCTION task.status.symbol == "!" || task.status.symbol == "*"
(due this week) OR (no due date)
```

## #2025蝙绿企划
```dataview
list without id
choice((date(now)-date(choice(date,date,auto_date))).day < 3,"- [f]","- [b]") + " " +
file.link + " " +
filter(file.tags,(x) => !contains(x,"2025蝙绿企划")&!contains(x,"BatLantern")&!contains(x,"FIN")) + " " +
length + "字 " +
dateformat(choice(date,date,auto_date),"yy.M.d")
FROM #2025蝙绿企划
WHERE !contains(file.path,"logs") and !contains(file.name,"todo")
SORT choice(date,date,auto_date) DESC
SORT contains(file.tags,"FIN")
LIMIT 12
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
