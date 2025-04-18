# coding = utf-8

"""线上格式化md"""

import os
import sys

from personal import PATH_LOG
from utils import (
    add_predef,
    dir_name,
    doc_dir,
    get_ai_comment,
    get_ai_source,
    ignore_in_format,
    mark_category,
    name_of,
    search_by_keyword,
    short_path,
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
            for line in content.split("\n\n"):
                if line.startswith("# ") and not title_set:
                    title = line.replace("# ", "").strip()
                    title = title.strip("*")
                    title_set = True
                else:
                    cont.append(line)
            content = "\n\n".join(cont)
        f.write(content)
    add_predef(filename, "title", title, True)
    if not ignore_in_format(filename):
        mark_category(filename)
    elif PATH_LOG in short_path(filename):
        mark_category(filename)
    if get_ai_comment(filename):
        add_predef(
            filename,
            "ai-comment",
            get_ai_comment(filename).replace(".md", ".html"),
        )
    elif get_ai_source(filename):
        add_predef(
            filename,
            "ai-back",
            get_ai_source(filename).replace(".md", ".html"),
        )


def format_dir(path):
    """格式化文件夹"""
    for item in os.listdir(path):
        if dir_name(os.path.join(path, item)):
            format_dir(os.path.join(path, item))
        elif item.endswith(".md"):
            format_md(os.path.join(path, item))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        format_dir(doc_dir())
    else:
        for i in search_by_keyword(sys.argv[1]):
            format_md(i)
