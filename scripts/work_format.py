# coding = utf-8

"""格式化文件库"""

import os
import sys

from personal import LOG_PATH
from utils import (
    add_predef,
    doc_dir,
    file_length,
    ignore_in_format,
    mark_fin,
    search_by_keyword,
    short_path,
    sort_predef,
)


def format_file(filename, force=False):
    """格式化文件"""
    f = open(filename, "r", encoding="utf-8")
    content = f.readlines()
    f.close()
    f = open(filename, "w", encoding="utf-8")
    # print(content)
    pre_def = False
    res = ""
    for line in content:
        if filename.endswith(".py"):
            res += line.strip("\n") + "\n"
        elif "---\n" in line:
            pre_def = not pre_def
            res += line.strip("\n") + "\n"
        elif pre_def or LOG_PATH in short_path(filename):
            res += line.strip("\n") + "\n"
        else:
            res += line.strip() + "\n"
    if not filename.endswith(".py"):
        res = res.replace("\n\n\n\n\n\n\n", "\n\n<br>\n\n<br>\n\n<br>\n")
        res = res.replace("\n\n\n", "\n\n<br>\n")
        res = res.replace("------", "---")
    f.write(res.strip("\n") + "\n")
    f.close()
    if filename.endswith(".md"):
        add_predef(
            filename, "word_count", str(file_length(filename)), change=True
        )
        mark_fin(filename)
    if force:
        sort_predef(filename)


def format_blob(filename):
    """格式化短篇"""
    if filename.endswith(".md"):
        return
    with open(filename, "r", encoding="utf8") as f:
        content = f.readlines()
    path = filename.split("\\")
    name = path.pop(-1)
    new_name = name.split(" ")
    date = new_name.pop(0)
    new_name = " ".join(new_name)
    new_name = new_name.replace(".txt", ".md")
    title = new_name.replace(".md", "")
    path.append(new_name)
    new_name = "\\".join(path)
    new = f"---\ndate: {date}\n---\n\n"
    with open(new_name, "w", encoding="utf8") as f:
        new += f"# {title}\n\n"
        for _ in range(6):
            content.pop(0)
        for line in content:
            new += line.strip() + "\n\n"
        f.write(new.strip() + "\n")


def format_all(path):
    """从根目录起格式化所有文件"""
    l = os.listdir(path)
    for item in l:
        subdir = os.path.join(path, item)
        if os.path.isdir(subdir) and not "/." in subdir:
            format_all(subdir)
        # elif "blob" in subdir:
        #     format_blob(subdir)
        elif (
            subdir.endswith(".md")
            or subdir.endswith(".txt")
            or subdir.endswith(".py")
        ) and not ignore_in_format(subdir):
            format_file(subdir)
        elif os.path.isdir(subdir) and "data" in subdir:
            format_all(subdir)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        format_all(doc_dir())
    else:
        for i in search_by_keyword(sys.argv[1]):
            format_file(i, True)
