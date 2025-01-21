# 文档库

## 无tag文档

```dataview
LIST
WHERE !file.tags|length(filter(file.tags,(x)=>!contains(x,"FIN")))=0 and file.folder="DC"|file.folder="QZ"
```
