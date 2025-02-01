# TODO

## 当前任务

```dataview
TASK
WHERE contains(text,"进度")
```

## 待办事项

```tasks
filter by function task.status.type=="TODO" || task.status.type=="IN_PROGRESS"
short
hide task count
hide backlink
```

## 创意

```tasks
filter by function task.status.type=="NON_TASK"
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
