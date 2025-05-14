# coding - utf-8

"""把所有完成作品加入git临时目录"""

import os

from file_status import 文件管理
from utils import 相对路径, 路径名


def go_over(path):
    """新增目录下已完成作品"""
    for i in os.listdir(path):

        if 路径名(i):
            go_over(os.path.join(path, i))
        elif i.endswith(".md") and 文件管理(os.path.join(path, i)).已完结():
            os.system(f"git add {相对路径(os.path.join(path,i))}")


go_over(os.getcwd())
