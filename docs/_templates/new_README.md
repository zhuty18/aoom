# <% tp.file.folder() %>

## 未完结

```dataview
TABLE WITHOUT ID
file.link + " " +filter(file.tags,(x) => !contains(x,"FIN")) as 文件名, length as 字数, dateformat(choice(date,date,auto_date),"yy.MM.dd") as 修改时间
WHERE contains(file.folder,"<% tp.file.folder() %>") and length and !contains(file.tags,"FIN")
SORT choice(date,date,auto_date) DESC
```

## 已完结

```dataview
TABLE WITHOUT ID
file.link + " " +filter(file.tags,(x) => !contains(x,"FIN")) as 文件名, length as 字数, dateformat(choice(date,date,auto_date),"yy.MM.dd") as 修改时间
WHERE contains(file.folder,"<% tp.file.folder() %>") and length and contains(file.tags,"FIN")
SORT choice(date,date,auto_date) DESC
```
