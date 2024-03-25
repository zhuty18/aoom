# coding = utf-8

"""格式化文件库"""

import os
from utils import doc_dir


def format_file(filename):
    """格式化文件"""
    f = open(filename, "r", encoding="utf-8")
    content = f.readlines()
    f.close()
    f = open(filename, "w", encoding="utf-8")
    # print(content)
    for i in content:
        if filename.endswith(".py"):
            f.write(i.strip("\n") + "\n")
        else:
            f.write(i.strip() + "\n")
    f.close()


def format_all(path):
    """从根目录起格式化所有文件"""
    l = os.listdir(path)
    for i in l:
        subdir = os.path.join(path, i)
        if os.path.isdir(subdir) and not "/." in subdir:
            format_all(subdir)
        # elif subdir.__contains__("README"):
        #     pass
        elif subdir.endswith(".md") or subdir.endswith(".txt") or subdir.endswith(".py"):
            format_file(subdir)
        elif os.path.isdir(subdir) and "data" in subdir:
            format_all(subdir)


if __name__ == "__main__":
    format_all(doc_dir())
