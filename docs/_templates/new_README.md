# <% tp.file.folder() %>

## 未完结

```dataview
TABLE WITHOUT ID
file.link as 文件名, length as 字数, dateformat(date,"yy.MM.dd") as 修改时间
WHERE contains(file.folder,"<% tp.file.folder() %>") and length and !contains(file.tags,"FIN")
SORT file.name
```

## 已完结

```dataview
TABLE WITHOUT ID
file.link as 文件名, length as 字数, dateformat(date,"yy.MM.dd") as 修改时间
WHERE contains(file.folder,"<% tp.file.folder() %>") and length and contains(file.tags,"FIN")
SORT file.name
```
