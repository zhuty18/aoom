# coding = utf-8

"""用astro发布"""

import os
import sys

from file_status import 文件管理
from utils import 文档根目录, 获取文件_关键字, 路径名


def 在线格式化文件夹(path):
    """格式化文件夹"""
    for item in os.listdir(path):
        if 路径名(os.path.join(path, item)):
            在线格式化文件夹(os.path.join(path, item))
        elif item.endswith(".md"):
            文件管理(os.path.join(path, item)).在线格式化()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        在线格式化文件夹(文档根目录())
    else:
        for i in 获取文件_关键字(sys.argv[1]):
            文件管理(i).在线格式化()
