![Homepage](Homepage.md#当前任务)

```dataview
TABLE WITHOUT ID
file.link as 文件,
word_count+"<br><meter value="+ word_count/max(8000,word_count*1.1) + " max=1 min=0 low=0.3 high=0.7 optimum=0.9></meter>" as 进度,
floor((date(now)-choice(date,date,auto_date)).day) + "天前" as 更新
FROM -#FIN and -"trash"
WHERE word_count
SORT choice(date,date,auto_date) DESC
LIMIT 15
```
