# coding = utf-8

"""文件内专有名词翻译"""

import os
from sys import argv

from name_def import nick_names
from utils import (
    doc_path,
    full_names,
    name_pieces,
    short_names,
    wrong_translates,
    获取文件_关键字,
)


def translation_dir(mode):
    """翻译方向"""
    return (0, 1) if mode == "eng2chs" else (1, 0)


def name_tsl(filename, mode):
    """翻译单个文件"""
    if filename.endswith(".md"):
        tsl = translation_dir(mode)
        with open(filename, "r", encoding="utf8") as f:
            content = f.read()
        for i in full_names():
            content = content.replace(i[tsl[0]], i[tsl[1]])
        for i in short_names():
            content = content.replace(i[tsl[0]], i[tsl[1]])
        for i in name_pieces():
            content = content.replace(i[tsl[0]], i[tsl[1]])
        for i in nick_names:
            content = content.replace(i[tsl[0]], i[tsl[1]])
        for i in wrong_translates():
            content = content.replace(i[0], i[1])

        with open(filename, "w", encoding="utf8") as f:
            f.write(content)
    else:
        print(filename, "error!")


def tsl_all(path, mode):
    """翻译所有文件"""
    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path, i)):
            tsl_all(os.path.join(path, i), mode)
        else:
            name_tsl(os.path.join(path, i), mode)


def tsl_one(key, mode):
    """翻译单个文件"""
    for i in 获取文件_关键字(key):
        print(i[0])
        name_tsl(os.path.join(i[1], i[0]), mode)


if __name__ == "__main__":
    FILE_NAME = argv[1]
    from personal import 翻译模式

    if FILE_NAME == "all":
        tsl_all(doc_dir(), 翻译模式)
    elif os.path.isdir(FILE_NAME):
        tsl_all(os.path.join(doc_dir(), FILE_NAME), 翻译模式)
    else:
        name = 获取文件_关键字(FILE_NAME)
        name_tsl(name[0], 翻译模式)
