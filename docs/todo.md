# TODO

## 当前任务

```tasks
not done
sort by path reverse
short
tags include #2025蝙绿企划
hide task count
hide backlink
hide tags
```

```dataview
LIST length + "字 "+dateformat(choice(date,date,auto_date),"yy.M.d ") + " " + filter(file.tags,(x) => !contains(x,"蝙绿")&!contains(x,"BatLantern"))
FROM #2025蝙绿企划 and -#FIN
WHERE !contains(file.path,"logs")
SORT choice(date,date,auto_date) DESC
```

已完成`$=dv.pages("#2025蝙绿企划 and #FIN").length`篇。

```dataview
LIST length + "字 "+dateformat(choice(date,date,auto_date),"yy.M.d ") + " " + filter(file.tags,(x) => !contains(x,"FIN")&!contains(x,"蝙绿")&!contains(x,"BatLantern"))
FROM #2025蝙绿企划 and #FIN
```

## 待进行任务

```tasks
not done
short
NOT (tags include #2025蝙绿企划)
sort by urgency
hide task count
hide backlink
```

## 创意

```tasks
filter by function task.status.symbol=="I"
sort by path reverse
short
hide task count
hide backlink
```

## 已完成任务

```tasks
filter by function task.status.type=="DONE" || task.status.type=="CANCELLED"
short
sort by status.type
sort by done reverse
hide backlink
hide task count
```
