# coding=utf-8

"""个人设定"""

import time

网站名 = "兔子草 | Atomic"

GIT署名 = "tuzicao"
GIT邮箱 = "13718054285@163.com"

文档根 = "docs"

# 本次提交时间，留空作为运行时的公共变量
提交时间 = None

if 提交时间 is None:
    提交时间 = time.time()

GIT提交 = True
GIT添加 = True
GIT推送 = True
GIT默认信息 = "随便更新"

进行统计 = True

# 字数统计的顺序
# time代表按文件上一次提交的时间排序
# name代表按文件名（拼音顺序）进行排序
默认顺序 = "time"
其他顺序 = "name" if 默认顺序 == "time" else "time"

# 词云生成词云的文件范围
# 空字符串表示生成所有字数变化文件的词云
# none表示不生成词云
# 其他字符串表示生成文件名含此字符串的词云
词云范围 = "none"

# 词云统计后要做的工作
# s 生成与文档同名的.png文件，并保存在同一路径下
# p 生成词云图片并显示
# r 删除保存的词云图片
# 可以同时使用多个工作，例如sp
词云工作 = "p"

# 名词翻译方向
翻译模式 = "eng2chs"
反向翻译 = 翻译模式[4:7] + "2" + 翻译模式[0:3]

# 默认翻译
# TRANSLATE_MODE，BACKWARD_MODE，或None
翻译行为 = None

# 时间格式
时间格式 = "%y.%m.%d %H:%M"
日期格式 = "%Y-%m-%d"

# index
INDEX文件 = "index.md"
INDEX文件_完整 = "full_index.md"

# 文档库开头
文档库更新字符串 = "{update_detail}"
文档库YAML = f"""---
layout: docs
title: {网站名}
update: {文档库更新字符串}
---

"""
标题_已完结 = "## 已完结"
标题_未完结 = "## 未完结"

# 默认字符串，勿动
隐藏区开头 = "// finished work head"
隐藏区结尾 = "// finished work tail"
隐藏区初始值 = '"template":true,'

历史文件 = "data/history.txt"
更改文件 = "data/change.txt"

# POST相关
POST路径 = "src/contents/"
POST日期格式 = "%Y-%m-%d"
POST文件格式 = POST日期格式 + "-{title}.md"
# 首页post显示上限，0为关闭功能，-1为不设置上限
首页POST上限 = 10
摘要长度 = 100

完结标志 = ["END", "完结", "Q.E.D."]
完结TAG = "FIN"
未完TAG = "TBC"
AI批评TAG = "AI批评"

# 日志
日志路径 = "docs/logs"

# 文件夹名
文件夹名 = {
    "AI": "AI批评",
    "blob": "短篇",
    "DC": "DC",
    "DM": "数码宝贝",
    "DMC": "鬼泣",
    "DR": "龙族",
    "FT": "童话系列（欧美）",
    "GTM": "银魂",
    "logs": "日志",
    "M": "漫威",
    "ON": "原创小说",
    "ON/O": "其他原创",
    "Others": "其他",
    "QZ": "全职",
    "SC": "影评",
    "SWY": "食物语",
    "translation": "翻译",
    "translation/batfamily": "翻译-蝙家",
    "translation/BruceHal": "翻译-蝙绿蝙",
    "X": "X战警",
    "XJ": "仙剑",
    "YWJ": "曳尾记",
    "YYS": "阴阳师",
    "": "所有目录",
}

# 格式化+字数统计时忽略的文件与路径
忽略文件 = [INDEX文件_完整, INDEX文件, "README.md"]
AI评论路径 = "docs/AI"
忽略路径 = [
    日志路径,
    "docs/明星煌煌",
    "docs/_obsidian",
    "docs/material",
    AI评论路径,
]

# TAG类别（排序用）
TAGS_优先 = ["2025蝙绿企划"]
TAGS_CP = [
    "无CP",
    "混邪",
    "其他CP",
    "BatLantern",
    "BruTalia",
    "BatWonder",
    "JayTim",
    "JayKyle",
    "JayRoy",
    "JayRose",
    "BirdFlash",
    "DamiJon",
    "DickJayTim",
    "GuyKyle",
    "HalSin",
    "WonderSteve",
    "叶攻",
    "叶王",
    "叶乐",
    "叶邱",
    "修伞",
    "双一",
    "张楚",
    "王柔",
    "王乐",
    "剑诅",
    "DVD",
    "恺楚",
]
TAGS_角色 = [
    "孙翔",
    "叶修",
    "周泽楷",
    "邱非",
    "王杰希",
    "黄少天",
    "唐柔",
    "张佳乐",
    "韩文清",
    "苏沐秋",
    "喻文州",
    "楚云秀",
    "张新杰",
    "孙哲平",
]
TAGS_组织 = [
    "蝙家",
    "灯团",
    "正联",
    "霸图",
    "百花",
    "微草",
    "国家队",
    "嘉世",
    "兴欣",
    "蓝雨",
]
