# coding = utf-8
"""
发布文件到POST_PATH文件夹
"""
import sys
import os
from personal import POST_PATH, POST_TITLE, POST_DATE, FILE_ROOT
from utils import search_by_keyword, name_of, format_time, get_time, short_path
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
    with open(filename, "r", encoding="utf8") as f:
        preview = f.read()[0:200]
    with open(os.path.join(POST_PATH, post_name), "w", encoding="utf8") as f:
        f.write(
            f"""---
layout: forward
redirect: /{short_path(filename).replace(".md","")}
title: {name_of(filename)}
date: {format_time(get_time(his.time), POST_DATE)}
---
{preview}
"""
        )


def post_all(path):
    """发布所有文件"""
    pass


if __name__ == "__main__":
    wcr = None
    if len(sys.argv) > 1:
        for i in search_by_keyword(sys.argv[1]):
            post(i, wcr)
    else:
        post_all(FILE_ROOT)
