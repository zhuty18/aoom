# coding = utf-8

"""线上格式化md"""

import os
import sys

from personal import INDEX_FULL_NAME, INDEX_NAME
from utils import (
    add_predef,
    dir_name,
    doc_dir,
    mark_category,
    mark_fin,
    name_of,
    search_by_keyword,
)


def format_md(filename):
    """格式化单文件"""
    with open(filename, "r", encoding="utf8") as f:
        content = f.read()
    title = name_of(filename)
    with open(filename, "w", encoding="utf8") as f:
        if "title: " not in content:
            cont = []
            title_set = False
            for i in content.split("\n\n"):
                if i.startswith("# ") and not title_set:
                    title = i.replace("# ", "")
                    title = title.strip("*")
                    title_set = True
                else:
                    cont.append(i)
            content = "\n\n".join(cont)
        content = content.replace(
            "\n\n\n\n\n\n\n", "\n\n<br>\n\n<br>\n\n<br>\n"
        )
        content = content.replace("\n\n\n", "\n\n<br>\n")
        f.write(content)
    add_predef(filename, "title", title, "")
    if INDEX_NAME not in filename and INDEX_FULL_NAME not in filename:
        mark_category(filename)
        mark_fin(filename)


def format_dir(path):
    """格式化文件夹"""
    for i in os.listdir(path):
        if dir_name(os.path.join(path, i)):
            format_dir(os.path.join(path, i))
        elif i.endswith(".md"):
            format_md(os.path.join(path, i))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        format_dir(doc_dir())
    else:
        for i in search_by_keyword(sys.argv[1]):
            format_md(i)
