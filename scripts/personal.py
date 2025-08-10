# coding=utf-8

"""个人设定"""

import time

网站名 = "兔子草 | Atomic"

GIT_NAME = "tuzicao"
GIT_EMAIL = "13718054285@163.com"

DOC_ROOT = "docs"

# 本次提交时间，留空作为运行时的公共变量
COMMIT_TIME = None

if COMMIT_TIME is None:
    COMMIT_TIME = time.time()

GIT_COMMIT = True
GIT_ADD = True
GIT_PUSH = True
GIT_DEFAULT_MESSAGE = "随便更新"

RUN_STAT = True

# 名词翻译方向
TRANSLATE_MODE = "eng2chs"

# 默认翻译
# TRANSLATE_MODE，BACKWARD_MODE，或None
翻译行为 = None

# 时间格式
TIME_FORMAT = "%y.%m.%d %H:%M"
DATE_FORMAT = "%Y-%m-%d"

# 默认字符串，勿动
HIDE_HEAD = "// finished work head"
HIDE_TAIL = "// finished work tail"
HIDE_DEFAULT = '"template":true,'

PATH_HISTORY = "data/history.txt"

# POST相关
POST_PATH = "src/contents"
# 首页post显示上限，0为关闭功能，-1为不设置上限
MAXIMUM_POST = 10
EXCERPT_LENGTH = 100

FIN_MARKS = ["END", "完结", "Q.E.D."]
FIN_PATHS = ["batlantern", "blob", "logs"]

AI_TAG = "AI批评"

# 日志
日志路径 = "docs/logs"

# 文件夹名
NAME_OF_DIR = {
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
IGNORE_FILES = ["README.md"]
AI_PATH = "docs/AI"
IGNORE_PATHS = [
    日志路径,
    "docs/明星煌煌",
    "docs/_obsidian",
    "docs/material",
    AI_PATH,
]

# TAG类别（排序用）
TAGS_PRIORITY = ["2025蝙绿企划"]
TAGS_CP = [
    "无CP",
    "混邪",
    "其他CP",
    "BatLantern",
    "BruTalia",
    "BatWonder",
    "Clex",
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
TAGS_CHARACTER = [
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
TAGS_ORGANIZATION = [
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
    "七期",
]
