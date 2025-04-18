# coding - utf-8

"""把所有完成作品加入git临时目录"""

import os

from personal import INDEX_NAME, INDEX_NAME_FULL
from utils import dir_name, file_fin, short_path


def go_over(path):
    """新增目录下已完成作品"""
    for i in os.listdir(path):
        if not INDEX_NAME_FULL in i and not INDEX_NAME in i and dir_name(i):
            go_over(os.path.join(path, i))
        elif i.endswith(".md") and file_fin(os.path.join(path, i)):
            os.system(f"git add {short_path(os.path.join(path,i))}")


go_over(os.getcwd())
