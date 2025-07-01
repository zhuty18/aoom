# Scripts

## 使用方法

1. 安装 python

    开发使用的 python 最低版本是 3.7.4。用3.8，3.9，3.12都做过测试。

    请确保安装的 python 版本不低于 3.7。

2. 安装依赖

    python -m pip install --user -r requirements.txt`即可

3. 根据你需要的功能运行脚本

## 主要功能

在[scripts/personal.py](./scripts/personal.py)中进行了一些默认值的设定，请在其中根据自己的喜好进行修改

### 自动使用 git 提交

执行命令`python update.py`

相关参数如下

|参数|含义|效果|
|:-|:-|:-|
|`-a`|是否添加所有修改|使用此参数，行为与默认值不同|
|`-c`|是否提交|使用此参数，行为与默认值不同|
|`-m`|提交信息|与`git commit -m [message]`的效果类似</br>如果不使用此参数，则会按照默认的信息提交|
|`-p`|是否推送到远程分支|使用此参数，行为与默认值不同|

如果不提交，则参数没有意义。

### 更新历史记录

从工作文件夹起，统计其与其所有子文件夹（多层嵌套）内各自存在的 MarkDown 文档的字数，在对应的文章中插入`auto_date`更新日期。更新仓库历史。

相关参数如下

|参数|含义|效果|
|:-|:-|:-|
|-s|字数统计|使用此参数，统计行为与默认值不同|

### 强制刷新历史记录

`python scripts/work_record.py`

强制刷新历史记录，包含自动隐藏已完成作品

## 搜索文件内容

`python scripts/search_for_key.py [关键词]`

会在所有 MarkDown 中搜索给定的关键词，在终端打印出结果

## 格式化

`python scripts/work_format.py [关键词]`

不使用关键词：

1. 从根目录起，把.txt 和.md 文件中的行尾符纠正为对应操作系统的；段首尾空白字符去除
2. 为.md 文件更新字数统计
3. 把.py 文件的行尾符纠正为对应操作系统的

使用关键词：

1. 格式化文件名含有指定关键词的文件
2. 更新字数统计，并打印字数统计详情

## 翻译名词

`python scripts/name_translate.py [filename]`

按预设的翻译方向翻译文本

|选项参数|效果|
|:-|:-|
|all|翻译所有文件|
|（文件夹）|翻译指定文件夹的所有文件|
|（关键词）|翻译标题含有关键词的文件|

## 随机姓氏

`python scripts/family_name.py`

生成一个随机中文姓氏

## 导出为$\LaTeX$

`python scripts/file_to_latex.py [keyword] [-d depth] [-o output_name] [-p path]`

深度depth为一级标题对应的$\LaTeX$标题，默认为0（chapter）。

输出路径path可以使用相对路径，默认为`./latex_output`。

输出文件名output_name默认为原文件名，可以自行制定（不含后缀）。

## 根据文件库拟合文件大小到字数的函数

`python scripts/live_calculate.py`
