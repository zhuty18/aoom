# coding = utf-8
"""
发布文件到POST_PATH文件夹
"""
import os
import sys

from personal import FILE_ROOT, INDEX_NAME, POST_DATE, POST_MAX, POST_PATH
from utils import (
    dir_name,
    format_time,
    get_pre_key,
    get_predefine,
    get_time,
    make_index,
    make_index_dir,
    name_of,
    path_of,
    preview,
    search_by_keyword,
    short_path,
)
from work_record import WordCounter

LOG_POST = False


def post(filename, counter, marked=False):
    """发布单个文件"""
    if counter is None:
        counter = WordCounter()
        counter.read_history()
    his = counter.history[name_of(filename)]
    for it in os.listdir(POST_PATH):
        if name_of(filename) in it:
            os.remove(os.path.join(POST_PATH, it))

    pre_d = get_predefine(filename)
    if not marked:
        if "false" in get_pre_key(pre_d, "post"):
            return
    else:
        if "true" not in get_pre_key(pre_d, "post"):
            return
    tags = get_pre_key(pre_d, "tags")
    if "FIN" not in tags:
        tags.insert(0, "FIN" if his.fin else "TBC")
    for x in tags:
        make_index("tag", x)
    tags = "\n  - " + "\n  - ".join(tags)
    if dir_name(path_of(filename)):
        make_index("category", dir_name(path_of(filename)))

    try:
        date = get_pre_key(pre_d, "date")[0]
    except IndexError:
        date = format_time(get_time(his.time), POST_DATE)

    target = short_path(filename).replace(".md", "")
    if target.endswith("."):
        target = target[:-1] + "/html"

    post_name = f"{date}-{his.name}.md"

    with open(os.path.join(POST_PATH, post_name), "w", encoding="utf8") as f:
        f.write(
            f"""---
layout: forward
target: /{target}
title: {" ".join(get_pre_key(pre_d,"title"))}
date: {date}
category: {dir_name(path_of(filename))}
cat_url: /{short_path(path_of(filename))}
tags: {tags if tags else ""}
length: {his.length}
---

{preview(filename)}
"""
        )


def clear_post(post_max=POST_MAX):
    """控制post上限"""
    if post_max >= 0:
        l = os.listdir(POST_PATH)
        l.sort()
        l.reverse()
        if len(l) > post_max:
            l = l[post_max:]
            for item in l:
                os.remove(os.path.join(POST_PATH, item))
        if LOG_POST:
            l = os.listdir(POST_PATH)
            l.sort()
            # print("\n".join(l))


def post_change(counter):
    """发布本次改动的文件"""
    for it in counter.changes:
        post(os.path.join(os.getcwd(), it), counter)
    clear_post()


def post_all(path, counter, allow_tbc=False, clear=True):
    """发布所有文件"""
    if counter is None:
        counter = WordCounter()
        counter.read_history()
    for item in os.listdir(path):
        if dir_name(os.path.join(path, item)):
            post_all(os.path.join(path, item), counter, allow_tbc, False)
        elif name_of(item) in counter.history and (
            not os.path.isdir(os.path.join(path, item))
        ):
            if counter.history[name_of(item)].fin or allow_tbc:
                post(os.path.join(path, item), counter)
    if clear:
        clear_post()


def post_marked(path, counter):
    """发布被标记post的"""
    if counter is None:
        counter = WordCounter()
        counter.read_history()
    for item in os.listdir(path):
        if dir_name(os.path.join(path, item)):
            post_marked(os.path.join(path, item), counter)
        elif name_of(item) in counter.history and (
            not os.path.isdir(os.path.join(path, item))
        ):
            post(os.path.join(path, item), counter, True)


if __name__ == "__main__":
    COUNTER = None
    if not os.path.exists(POST_PATH):
        os.mkdir(POST_PATH)
    make_index_dir("tag")
    make_index_dir("category")

    if len(sys.argv) > 1 and sys.argv[1] == "ONLINE":
        LOG_POST = True
        post_all(FILE_ROOT, COUNTER, True)
        post_marked(FILE_ROOT, COUNTER)
        defs = get_predefine(os.path.join(FILE_ROOT, INDEX_NAME))
        change = get_pre_key(defs, "change")
        for i in change:
            post(i, COUNTER)
    elif len(sys.argv) > 1:
        for i in search_by_keyword(sys.argv[1]):
            post(i, COUNTER)
    else:
        post_all(FILE_ROOT, COUNTER, True)
