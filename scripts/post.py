# coding = utf-8

"""
发布文件到POST_PATH文件夹
"""

import os

from file_status import 文件管理
from personal import DOC_ROOT, POST_PATH, 首页POST上限
from utils import 制作文件夹, 路径名

POST_LIST = []


def 发布文件(filename):
    """发布单个文件"""
    POST_LIST.append(文件管理(filename).发布())


def 发布日志(filename):
    """post一条日志"""
    文件管理(filename).标注发布(True)


def 额外发布指定量(发布上限=首页POST上限):
    """额外发布指定量"""
    if 发布上限 >= 0:
        POST_LIST.sort(key=lambda x: x[0], reverse=True)

        posted = 0
        for item in POST_LIST:
            文件 = 文件管理(item[1])
            posted += 文件.标注发布()
            if posted == 发布上限:
                break


def 强制发布文件(filename):
    """标记本次改动的文件为post"""
    文件 = 文件管理(filename)
    for item in POST_LIST:
        if 文件.标题() in item:
            文件管理(item).标注发布()
            break


def 发布全部文件(path, allow_tbc=False):
    """发布所有文件"""
    others = []
    for item in os.listdir(path):
        文件路径 = os.path.join(path, item)
        if 路径名(文件路径):
            if "AI" not in 文件路径:
                others.append(文件路径)
            else:
                发布全部文件(文件路径, allow_tbc)
        else:
            文件 = 文件管理(文件路径)
            if 文件.应发布():
                if 文件.已完结() or allow_tbc:
                    发布文件(文件路径)
    for item in others:
        发布全部文件(item, allow_tbc)


if __name__ == "__main__":
    制作文件夹(POST_PATH)

    发布全部文件(DOC_ROOT, True)
    额外发布指定量()
