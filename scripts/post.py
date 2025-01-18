# coding = utf-8
"""
发布文件到POST_PATH文件夹
"""
import os
import sys

from personal import (
    FILE_ROOT,
    INDEX_NAME,
    LOG_PATH,
    POST_DATE,
    POST_MAX,
    POST_PATH,
)
from utils import (
    add_predef,
    dir_name,
    format_time,
    get_pre_key,
    get_predefine,
    get_time,
    make_index,
    make_index_dir,
    mark_post,
    name_of,
    path_of,
    preview,
    search_by_keyword,
    short_path,
)
from work_record import WordCounter

POST_LIST = []


def post(filename, name, default_time=None):
    """发布单个文件"""

    # 获取文件预定义
    pre_d = get_predefine(filename)

    # 获取post日期
    try:
        date = get_pre_key(pre_d, "date")[0]
    except IndexError:
        date = format_time(get_time(default_time), POST_DATE)

    # 生成post名
    post_name = f"{date}-{name}.md"
    post_path = os.path.join(POST_PATH, post_name)

    # 建立post文件
    with open(post_path, "w", encoding="utf8") as f:
        f.write(
            f"""---
{pre_d}
---

{preview(filename)}
"""
        )

    # 添加跳转
    add_predef(post_path, "layout", "forward")
    target = short_path(filename).replace(".md", "")
    if target.endswith("."):
        target = target[:-1] + "/html"
    add_predef(post_path, "target", target)
    # 添加类别路径
    add_predef(post_path, "cat_url", short_path(path_of(filename)))

    # 记录post
    POST_LIST.append(post_name)

    # 建立标签索引
    for x in get_pre_key(pre_d, "tags"):
        make_index("tag", x)
    # 建立类别索引
    if dir_name(path_of(filename)):
        make_index("category", dir_name(path_of(filename)))

    return post_path


def post_work(filename, counter):
    """发布单个文件"""

    # 阅读该文件历史
    his = counter.history[name_of(filename)]

    post_path = post(filename, his.name, his.time)

    pre_d = get_predefine(post_path)
    # 添加完结标
    if "FIN" not in get_pre_key(pre_d, "tags"):
        add_predef(post_path, "tags", "TBC")
        make_index("tag", "TBC")
    # 添加日期和长度
    add_predef(
        post_path, "date", format_time(get_time(his.time), POST_DATE), True
    )
    add_predef(post_path, "length", his.length)


def post_log(filename):
    """post一条日志"""
    post(filename, "日志")


def clear_post(post_max=POST_MAX):
    """控制post上限"""
    if post_max >= 0:
        POST_LIST.sort()
        POST_LIST.reverse()

        posted = 0
        for item in POST_LIST:
            posted += mark_post(os.path.join(POST_PATH, item))
            if posted == post_max:
                break


def mark_as_post(filename, counter):
    """标记本次改动的文件为post"""
    his = counter.history[name_of(filename)]
    for item in POST_LIST:
        if his.name in item:
            mark_post(os.path.join(POST_PATH, item))
            break


def post_all(path, counter, allow_tbc=False):
    """发布所有文件"""
    for item in os.listdir(path):
        if dir_name(os.path.join(path, item)):
            post_all(os.path.join(path, item), counter, allow_tbc)
        elif name_of(item) in counter.history and (
            not os.path.isdir(os.path.join(path, item))
        ):
            if counter.history[name_of(item)].fin or allow_tbc:
                post_work(os.path.join(path, item), counter)
        elif LOG_PATH in path and not os.path.isdir(path):
            post_log(path)


if __name__ == "__main__":
    COUNTER = WordCounter()
    COUNTER.read_history()
    if not os.path.exists(POST_PATH):
        os.mkdir(POST_PATH)
    make_index_dir("tag")
    make_index_dir("category")

    if len(sys.argv) > 1 and sys.argv[1] == "ONLINE":
        post_all(FILE_ROOT, COUNTER, True)
        defs = get_predefine(os.path.join(FILE_ROOT, INDEX_NAME))
        change = get_pre_key(defs, "change")
        for i in change:
            mark_as_post(i, COUNTER)
        clear_post()
    elif len(sys.argv) > 1:
        for i in search_by_keyword(sys.argv[1]):
            if LOG_PATH not in short_path(i):
                post_work(i, COUNTER)
                mark_as_post(i, COUNTER)
            else:
                post_log(i)
    else:
        post_all(FILE_ROOT, COUNTER, True)
