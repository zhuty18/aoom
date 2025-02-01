# TODO

## 当前任务

```dataview
TASK
WHERE status = "!" and contains(text,"📚") and contains(file.path,"logs")
```

## 待办事项

```tasks
FILTER BY FUNCTION (task.status.symbol != "!" && task.status.type == "IN_PROGRESS") || task.status.type == "TODO"
SORT BY status.type
SORT BY path REVERSE
```

## 脑洞

```tasks
FILTER BY FUNCTION task.status.type == "NON_TASK"
```

## 已完成任务

```tasks
DONE
SORT BY status.type
SORT BY done REVERSE
```
