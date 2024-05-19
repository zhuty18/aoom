# coding = utf-8

"""线上格式化md"""

import os
from utils import doc_dir, dir_name


def format_md(filename):
    """格式化单文件"""
    with open(filename, "r", encoding="utf8") as f:
        content = f.read()
    with open(filename, "w", encoding="utf8") as f:
        content = content.replace(
            "\n\n\n\n\n\n\n", "\n\n<br>\n\n<br>\n\n<br>\n"
        )
        content = content.replace("\n\n\n", "\n\n<br>\n")
        f.write(content)


def format_dir(path):
    """格式化文件夹"""
    for i in os.listdir(path):
        if dir_name(os.path.join(path, i)):
            format_dir(os.path.join(path, i))
        elif i.endswith(".md"):
            format_md(os.path.join(path, i))


if __name__ == "__main__":
    format_dir(doc_dir())
