# coding = utf8

"""解决windows上obsidian换行的问题"""

import os
import platform


def touch_one(path):
    """处理单个文件"""
    with open(path, "r", encoding="utf8") as f:
        content = f.read()
    with open(path, "w", encoding="utf8") as f:
        f.write("\n".join(content.split("\n")))


def touch_sub(path):
    """路径循环"""
    for i in os.listdir(path):
        subpath = os.path.join(path, i)
        if os.path.isdir(subpath):
            touch_sub(subpath)
        else:
            touch_one(subpath)


def touch_obsidian():
    """将obsidian内文件换行符处理掉"""
    OBSIDIAN_PATH = "docs/.obsidian"
    if "Windows" in platform.system():
        touch_sub(OBSIDIAN_PATH)


if __name__ == "__main__":
    touch_obsidian()
