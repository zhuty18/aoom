# coding = utf-8

"""格式化文件库"""

import os
import sys

from file_status import 文件管理
from utils import 文档根目录, 获取文件_关键字


def 格式化文件(filename, force=False):
    """格式化文件"""
    t = 文件管理(filename)
    if t.合法():
        t.格式化()
        if force:
            t.整理yaml()
    else:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content.strip("\n") + "\n")


def 全部格式化(path):
    """从根目录起格式化所有文件"""
    l = os.listdir(path)
    for item in l:
        子路径 = os.path.join(path, item)
        if os.path.isdir(子路径) and not "/." in 子路径:
            全部格式化(子路径)
        elif (
            子路径.endswith(".md")
            or 子路径.endswith(".txt")
            or 子路径.endswith(".py")
        ) and not 文件管理(子路径).格式化中忽略():
            格式化文件(子路径)
        elif os.path.isdir(子路径) and "data" in 子路径:
            全部格式化(子路径)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        全部格式化(文档根目录())
    else:
        for i in 获取文件_关键字(sys.argv[1]):
            格式化文件(i, True)
