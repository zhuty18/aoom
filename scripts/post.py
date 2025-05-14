# coding = utf-8
"""
发布文件到POST_PATH文件夹
"""
import os
import sys

from file_status import 文件管理
from personal import (
    AI批评TAG,
    INDEX文件,
    POST路径,
    完结TAG,
    未完TAG,
    首页POST上限,
    文档根,
    日志路径,
)
from utils import 制作索引, 制作索引_路径, 相对路径, 获取文件_关键字, 路径名

POST_LIST = []


def 发布文件(filename):
    """发布单个文件"""
    POST_LIST.append(文件管理.从路径(filename).发布())


def 发布日志(filename):
    """post一条日志"""
    文件管理(filename).标注发布(True)


def 额外发布指定量(发布上限=首页POST上限):
    """额外发布指定量"""
    if 发布上限 >= 0:
        POST_LIST.sort()
        POST_LIST.reverse()

        posted = 0
        for item in POST_LIST:
            文件 = 文件管理(item)
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
    for item in os.listdir(path):
        文件路径 = os.path.join(path, item)
        if 路径名(文件路径):
            发布全部文件(文件路径, allow_tbc)
        elif 日志路径 in 相对路径(path):
            发布日志(文件路径)
        else:
            文件 = 文件管理(文件路径)
            if 文件.应发布():
                if 文件.已完结() or allow_tbc:
                    发布文件(文件路径)


if __name__ == "__main__":
    if not os.path.exists(POST路径):
        os.mkdir(POST路径)
    制作索引_路径("tags", "标签")
    制作索引("tags", 未完TAG)
    制作索引("tags", 完结TAG)
    制作索引("tags", AI批评TAG)
    制作索引_路径("category", "分类")

    if len(sys.argv) > 1 and sys.argv[1] == "ONLINE":
        发布全部文件(文档根, True)
        改动文件 = 文件管理(os.path.join(文档根, INDEX文件)).读取yaml内参数(
            "change"
        )
        for i in 改动文件:
            强制发布文件(i)
        额外发布指定量()
    elif len(sys.argv) > 1:
        for i in 获取文件_关键字(sys.argv[1]):
            if 日志路径 not in 相对路径(i):
                发布文件(i)
                强制发布文件(i)
            else:
                发布日志(i)
    else:
        发布全部文件(文档根, True)
