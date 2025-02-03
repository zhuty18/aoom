# TODO

## 重要任务

```dataview
TASK
WHERE status = "!" and contains(text,"📚") and contains(file.path,"logs")
SORT status
```

```tasks
FILTER BY FUNCTION task.status.symbol == "!"
```

## 待办事项

```tasks
FILTER BY FUNCTION (task.status.symbol != "!" && task.status.type == "IN_PROGRESS" )|| task.status.type == "TODO"
SORT BY FUNCTION task.status.symbol
```

## 脑洞

```tasks
FILTER BY FUNCTION task.status.type == "NON_TASK"
SORT BY path REVERSE
```

## 已完成

```tasks
DONE
FILTER BY FUNCTION task.status.type!="NON_TASK"
SORT BY done REVERSE
HIDE EDIT BUTTON
```
