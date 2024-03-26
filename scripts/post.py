# coding = utf-8
"""
发布文件到POST_PATH文件夹
"""
import sys
import os
from personal import POST_PATH, POST_TITLE, POST_DATE, FILE_ROOT, POST_MAX
from utils import (
    search_by_keyword,
    name_of,
    format_time,
    get_time,
    short_path,
    preview,
    dir_name,
)
from work_record import WordCounter


def post(filename, wcr):
    """发布单个文件"""
    if wcr is None:
        wcr = WordCounter()
        wcr.read_history()
    his = wcr.history[name_of(filename)]
    for i in os.listdir(POST_PATH):
        if name_of(filename) in i:
            os.remove(os.path.join(POST_PATH, i))
    post_name = format_time(get_time(his.time), POST_TITLE).replace("{title}", his.name)
    target = short_path(filename).replace(".md", "")
    if target.endswith("."):
        target = target[:-1] + "/html"
    with open(os.path.join(POST_PATH, post_name), "w", encoding="utf8") as f:
        f.write(
            f"""---
layout: forward
target: /{target}
title: {name_of(filename)}
date: {format_time(get_time(his.time), POST_DATE)}
tags: 
  - {"FIN" if his.fin else "TBC"}
---

{preview(filename)}
"""
        )


def clear_post(post_max=POST_MAX):
    """控制post上限"""
    l = os.listdir(POST_PATH)
    l.sort()
    l.reverse()
    if len(l) > post_max:
        l = l[post_max:]
        for i in l:
            os.remove(os.path.join(POST_PATH, i))


def post_change(wcr):
    """发布本次改动的文件"""
    for i in wcr.changes:
        post(os.path.join(os.getcwd(), i), wcr)
    clear_post()


def post_all(path, wcr):
    """发布所有文件"""
    if wcr is None:
        wcr = WordCounter()
        wcr.read_history()
    for item in os.listdir(path):
        if dir_name(os.path.join(path, item)):
            post_all(os.path.join(path, item), wcr)
        elif name_of(item) in wcr.history and wcr.history[name_of(item)].fin:
            post(os.path.join(path, item), wcr)
    clear_post()


if __name__ == "__main__":
    wcr = None
    if len(sys.argv) > 1:
        for i in search_by_keyword(sys.argv[1]):
            post(i, wcr)
    else:
        post_all(FILE_ROOT, wcr)
