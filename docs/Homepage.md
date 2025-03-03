# 你好！

今天是你使用Obsidian的第`\=ceil((date(now)-date("2025-01-15")).days)`天。

你在这里有`$=dv.pages("-#FIN").where((x) => x.length).length`个坑，`$=dv.pages("#FIN").length`个 #FIN ，完结率`$=Math.round((dv.pages("-#FIN").where((x) => x.length).length/dv.pages("").where((x) => x.length).length)*1000)/10`%，不愧是你！

```dataview
TABLE WITHOUT ID
key as 文件名,
length(filter(rows,(x) => !contains(x.tags,"FIN"))) as 坑数,
round((length(filter(rows,(x) => contains(x.tags,"FIN")))/length(rows))*100,1)+"%" as 完结率,
round(sum(filter(rows,(x) => !contains(x.tags,"FIN")).count)/10000,1)+"万" as 坑字数,
round(sum(filter(rows,(x) => contains(x.tags,"FIN")).count)/sum(rows.count)*100,1)+"%" as 完结字数比
FROM -"trash"
WHERE count
GROUP BY file.folder
SORT length(rows) DESC
LIMIT 3
```

你正在搞的 #2025蝙绿企划 有`$=dv.pages('#2025蝙绿企划 and -#FIN').where((x) => x.length).length`个坑，完结率`$=Math.round((dv.pages('#FIN and #2025蝙绿企划').where((x) => x.count).length/dv.pages('#2025蝙绿企划').where((x) => x.count).length)*1000)/10`%。你写了`$=dv.pages("#2025蝙绿企划").where((x) => x.count).count.sum()`。
