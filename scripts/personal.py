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

# post上限，0为关闭功能，-1为不设置上限
POST_MAX = 10
PREVIEW_LENGTH = 100

FIN_TITLE = "## 已完结"
TBC_TITLE = "## 未完结"

# 文件夹名
DIR_NAMES = {
    "DC": "DC",
    "DM": "数码宝贝",
    "GTM": "银魂",
    "FT": "童话系列（欧美）",
    "DMC": "鬼泣",
    "M": "漫威",
    "ON/O": "其他原创",
    "Others": "其他",
    "QZ": "全职",
    "SC": "影评",
    "SWY": "食物语",
    "translation": "翻译",
    "X": "X战警",
    "XJ": "仙剑",
    "YYS": "阴阳师",
    "YWJ": "曳尾记",
    "ON": "原创小说",
    "translation/batfamily": "翻译-蝙家",
    "translation/BruceHal": "翻译-蝙绿蝙",
    "": "所有目录",
    "batlantern": "蝙绿官糖",
    "blob": "短篇",
    "logs": "日志",
}

LOG_PATH = "docs/logs"
