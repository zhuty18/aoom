# TODO

```tasks
not done
sort by urgency
short mode
```

还有`=round((date("2025-02-18")-date(now)).day,0)`天，个人企划进度`$=dv.pages("#2025蝙绿企划 and #FIN").length`/`$=dv.pages("#2025蝙绿企划").length`，还剩`$=dv.pages("#2025蝙绿企划 and #TODO").length`篇，加油！

```dataview
LIST length + "字 "+dateformat(choice(date,date,auto_date),"yy.M.d ")
FROM #TODO and #2025蝙绿企划
SORT choice(date,date,auto_date) DESC
```

其他还有`$=dv.pages("#TODO and -#2025蝙绿企划").length`篇，努力！

```dataview
LIST length + "字 "+dateformat(choice(date,date,auto_date),"yy.M.d ")
FROM #TODO and -#2025蝙绿企划
```

```tasks
done
short mode
sort by status.type
sort by done reverse
```
