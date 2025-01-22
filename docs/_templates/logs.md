---
date: {{date}}
---

# {{date:YY.M.D}}日志

```dataview
LIST
WHERE choice(date, date = date({{date}}), auto_date = date({{date}})) and !contains(file.folder,"logs")
```

## 清单

- [ ] #task 待办事项
