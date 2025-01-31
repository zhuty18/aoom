# TODO

## 当前任务

```tasks
filter by function task.status.type=="IN_PROGRESS" && task.status.symbol!="I"
sort by path reverse
short
hide task count
hide backlink
```

还有`\=round((date("2025-02-18")-date(now)).day,0)`天，个人企划进度`$=dv.pages("#2025蝙绿企划 and #FIN").length`/`$=dv.pages("#2025蝙绿企划").length`，还剩`$=dv.pages("#2025蝙绿企划 and #TODO").length`篇，加油！

```dataview
LIST length + "字 "+dateformat(choice(date,date,auto_date),"yy.M.d ") + " " + filter(file.tags,(x) => !contains(x,"TODO")&!contains(x,"蝙绿")&!contains(x,"BatLantern"))
FROM #TODO and #2025蝙绿企划
SORT choice(date,date,auto_date) DESC
```

已完成`$=dv.pages("#2025蝙绿企划 and #FIN").length`篇。

```dataview
LIST length + "字 "+dateformat(choice(date,date,auto_date),"yy.M.d ") + " " + filter(file.tags,(x) => !contains(x,"FIN")&!contains(x,"蝙绿")&!contains(x,"BatLantern"))
FROM #2025蝙绿企划 and #FIN
```

## 待进行任务

```tasks
filter by function task.status.type == "TODO"
short
sort by urgency
hide task count
hide backlink
```

## 其他任务

其他还有`$=dv.pages("#TODO and -#2025蝙绿企划").length`篇，努力！

```dataview
LIST length + "字 "+dateformat(choice(date,date,auto_date),"yy.M.d ") + " " + filter(file.tags,(x) => !contains(x, "TODO") )
FROM #TODO and -#2025蝙绿企划
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
done
short
sort by status.type
sort by done reverse
hide backlink
hide task count
```
