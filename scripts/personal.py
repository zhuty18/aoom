# coding=utf-8

# 网站名称
WEB_NAME = "兔子草"

# git使用的提交署名
GIT_NAME = "tuzicao"
GIT_EMAIL = "13718054285@163.com"

COMMIT_TIME = None

# 是否使用git提交
GIT_COMMIT = True

# 是否添加所有变更
GIT_ADD = False

# 是否推送到远程分支
GIT_PUSH = False

# 不使用-m参数时的提交默认信息
DEFAULT_MESSAGE = "随便更新"

# 是否进行字数统计
COUNT_WORD = False

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

# 生成网页
GENERATE_WEB = False

# 默认的时间戳格式
TIME_FORMAT = "%y.%m.%d %H:%M"
