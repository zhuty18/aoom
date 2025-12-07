# coding = utf-8

"""格式化文件库"""

import os
import sys

from file_status import FileCount
from utils import doc_root, filenames_of_key


def format_file(filename, force=False):
    """格式化文件"""
    t = FileCount(filename)
    if t.legal():
        t.format(force)
        if force:
            t.sort_yaml()
    else:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        with open(filename, "w", encoding="utf-8", newline="\n") as f:
            f.write(content.strip("\n") + "\n")


def format_all(path):
    """从根目录起格式化所有文件"""
    l = os.listdir(path)
    for item in l:
        sub_dir = os.path.join(path, item)
        if os.path.isdir(sub_dir) and not "/." in sub_dir:
            format_all(sub_dir)
        elif (
            sub_dir.endswith(".md")
            or sub_dir.endswith(".txt")
            or sub_dir.endswith(".py")
        ) and not FileCount(sub_dir).is_ignore():
            format_file(sub_dir)
        elif os.path.isdir(sub_dir) and "data" in sub_dir:
            format_all(sub_dir)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        format_all(doc_root())
    else:
        for i in filenames_of_key(sys.argv[1]):
            format_file(i, True)
