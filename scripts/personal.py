# coding=utf-8
"""
个人设定
"""

# 网站名称
WEB_NAME = "兔子草 | Atomic"

# git使用的提交署名
GIT_NAME = "tuzicao"
GIT_EMAIL = "13718054285@163.com"

# 文档根
FILE_ROOT = "docs"

# 生成网页
GENERATE_WEB = False

# 是否强制生成网页
GIT_WEB = False

COMMIT_TIME = None

# 是否使用git提交
GIT_COMMIT = True

# 是否添加所有变更
GIT_ADD = True

# 是否推送到远程分支
GIT_PUSH = True

# 不使用-m参数时的提交默认信息
DEFAULT_MESSAGE = "随便更新"

# 是否进行字数统计
COUNT_WORD = True

# 字数统计的顺序
# time代表按文件上一次提交的时间排序
# name代表按文件名（拼音顺序）进行排序
DEFAULT_ORDER = "time"
ALT_ORDER = "name" if DEFAULT_ORDER == "time" else "time"

# 词云生成词云的文件范围
# 空字符串表示生成所有字数变化文件的词云
# none表示不生成词云
# 其他字符串表示生成文件名含此字符串的词云
WORD_CLOUD_TYPE = "none"

# 词云统计后要做的工作
# s 生成与文档同名的.png文件，并保存在同一路径下
# p 生成词云图片并显示
# r 删除保存的词云图片
# 可以同时使用多个工作，例如sp
WORD_CLOUD_JOB = "p"

# 名词翻译方向
TRANSLATE_MODE = "eng2chs"
BACKWARD_MODE = TRANSLATE_MODE[4:7] + "2" + TRANSLATE_MODE[0:3]

# 默认翻译
# TRANSLATE_MODE，BACKWARD_MODE，或None
DEFAULT_TRANSLATE = None
# 默认的时间戳格式
TIME_FORMAT = "%y.%m.%d %H:%M"
# 默认的日期格式
DATE_FORMAT = "%Y-%m-%d"

# index
INDEX_NAME = "index.md"
INDEX_FULL_NAME = "full_index.md"

# 文档库开头
ARCHIVE_UPDATE = "{update_detail}"
ARCHIVE_TITLE = f"""---
layout: docs
title: {WEB_NAME}
update: {ARCHIVE_UPDATE}
---

"""

# 默认字符串，勿动
FIN_HEAD = "// finished work head"
FIN_TAIL = "// finished work tail"
FIN_TEM = '"template":true,'

HISTORY_PATH = "data/history.txt"
CHANGE_SAVE = "data/change.txt"

POST_PATH = "_posts/"
POST_DATE = "%Y-%m-%d"
POST_TITLE = POST_DATE + "-{title}.md"

FIN_TITLE = "## 已完结"
TBC_TITLE = "## 未完结"
FIN_MARKS = ["END", "完结", "Q.E.D."]
FIN_TAG = "FIN"
TBC_TAG = "TBC"
# 日志
LOG_PATH = "docs/logs"

# 首页post显示上限，0为关闭功能，-1为不设置上限
POST_MAX = 10

# 文件摘要长度
PREVIEW_LENGTH = 100

# 文件夹名
DIR_NAMES = {
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
IGNORE_FILES = [INDEX_FULL_NAME, INDEX_NAME, "README.md"]
IGNORE_PATH = [LOG_PATH, "docs/明星煌煌", "docs/_obsidian", "docs/material"]

# TAG类别（排序用）
PRIORITIZED_TAGS = ["2025蝙绿企划"]
CP_TAGS = [
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
PERSON_TAGS = [
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
ORGANIZATION_TAGS = [
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
