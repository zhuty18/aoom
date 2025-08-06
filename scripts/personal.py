# coding=utf-8

"""个人设定"""

import time

网站名 = "兔子草 | Atomic"

GIT署名 = "tuzicao"
GIT邮箱 = "13718054285@163.com"

DOC_ROOT = "docs"

# 本次提交时间，留空作为运行时的公共变量
COMMIT_TIME = None

if COMMIT_TIME is None:
    COMMIT_TIME = time.time()

GIT提交 = True
GIT添加 = True
GIT推送 = True
GIT默认信息 = "随便更新"

进行统计 = True

# 名词翻译方向
翻译模式 = "eng2chs"
反向翻译 = 翻译模式[4:7] + "2" + 翻译模式[0:3]

# 默认翻译
# TRANSLATE_MODE，BACKWARD_MODE，或None
翻译行为 = None

# 时间格式
时间格式 = "%y.%m.%d %H:%M"
TIME_FORMAT = "%Y-%m-%d"

# 默认字符串，勿动
隐藏区开头 = "// finished work head"
隐藏区结尾 = "// finished work tail"
隐藏区初始值 = '"template":true,'

历史文件 = "data/history.txt"

# POST相关
POST_PATH = "src/contents"
POST日期格式 = "%Y-%m-%d"
POST文件格式 = POST日期格式 + "-{title}.md"
# 首页post显示上限，0为关闭功能，-1为不设置上限
首页POST上限 = 10
EXCERPT_LENGTH = 100

FIN_MARKS = ["END", "完结", "Q.E.D."]
完结TAG = "FIN"
未完TAG = "TBC"
AI_TAG = "AI批评"

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
TAGS_优先 = ["2025蝙绿企划"]
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
    "七期",
]
