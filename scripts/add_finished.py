# coding - utf-8

"""把所有完成作品加入git临时目录"""

import os

from personal import INDEX文件, INDEX文件_完整
from utils import file_fin, 相对路径, 路径名


def go_over(path):
    """新增目录下已完成作品"""
    for i in os.listdir(path):
        if not INDEX文件_完整 in i and not INDEX文件 in i and 路径名(i):
            go_over(os.path.join(path, i))
        elif i.endswith(".md") and file_fin(os.path.join(path, i)):
            os.system(f"git add {相对路径(os.path.join(path,i))}")


go_over(os.getcwd())
