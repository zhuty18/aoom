# coding = utf-8
"""
发布文件到POST_PATH文件夹
"""
import os
import sys

from personal import (
    FILE_ROOT,
    FORMAT_POST_DATE,
    INDEX_NAME,
    MAX_POST,
    PATH_LOG,
    PATH_POST,
    TAG_AI_COMMENT,
    TAG_FIN,
    TAG_TBC,
)
from utils import (
    add_predef,
    dir_name,
    excerpt,
    format_time,
    get_pre_key,
    get_predef,
    get_time,
    is_ai,
    make_index,
    make_index_dir,
    mark_fin,
    mark_post,
    name_of,
    path_of,
    search_by_keyword,
    short_path,
    write_predef,
)
from work_record import WordCounter

POST_LIST = []


def post(filename, name, default_time=None):
    """发布单个文件"""

    # 获取文件预定义
    pre_d = get_predef(filename)

    # 获取post日期
    date = get_pre_key(pre_d, "date")
    if not date:
        date = get_pre_key(pre_d, "auto_date")
    if not date:
        date = format_time(get_time(default_time), FORMAT_POST_DATE)

    # 生成post名
    post_name = f"{date}-{name}.md"
    post_path = os.path.join(PATH_POST, post_name)

    # 建立post文件
    with open(post_path, "w", encoding="utf8") as f:
        f.write(
            f"""{excerpt(filename)}

<!--more-->
"""
        )
    write_predef(pre_d, post_path)

    # 添加跳转
    add_predef(post_path, "layout", "forward")
    target = short_path(filename).replace(".md", "")
    if target.endswith("."):
        target = target[:-1] + "/html"
    add_predef(post_path, "target", target)
    # 添加类别路径
    add_predef(post_path, "cat_url", short_path(path_of(filename)))
    # 添加摘要
    add_predef(post_path, "excerpt_separator", "<!--more-->")

    # 记录post
    POST_LIST.append(post_name)

    # 建立标签索引
    for x in get_pre_key(pre_d, "tags"):
        make_index("tags", x)
    # 建立类别索引
    if dir_name(path_of(filename)):
        make_index("category", dir_name(path_of(filename)))

    return post_path


def post_work(filename, counter):
    """发布单个文件"""

    # 阅读该文件历史
    his = counter.history[name_of(filename)]

    post_path = post(filename, his.name, his.time)

    pre_d = get_predef(post_path)
    # 添加完结标
    if not get_pre_key(pre_d, "finished"):
        mark_fin(post_path, True)
    # 添加日期
    add_predef(post_path, "date", get_pre_key(pre_d, "auto_date"))


def post_log(filename):
    """post一条日志"""
    add_predef(post(filename, "日志"), "post", "false", True)


def clear_post(post_max=MAX_POST):
    """控制post上限"""
    if post_max >= 0:
        POST_LIST.sort()
        POST_LIST.reverse()

        posted = 0
        for item in POST_LIST:
            posted += mark_post(os.path.join(PATH_POST, item))
            if posted == post_max:
                break


def mark_as_post(filename, counter):
    """标记本次改动的文件为post"""
    his = counter.history[name_of(filename)]
    for item in POST_LIST:
        if his.name in item:
            mark_post(os.path.join(PATH_POST, item))
            break


def post_all(path, counter, allow_tbc=False):
    """发布所有文件"""
    for item in os.listdir(path):
        subdir = os.path.join(path, item)
        if dir_name(subdir):
            post_all(subdir, counter, allow_tbc)
        elif PATH_LOG in short_path(path) and name_of(item) in counter.history:
            post_log(subdir)
        elif (
            name_of(item) in counter.history
            and (not os.path.isdir(subdir))
            and (not is_ai(subdir))
        ):
            if counter.history[name_of(item)].fin or allow_tbc:
                post_work(subdir, counter)


if __name__ == "__main__":
    COUNTER = WordCounter()
    COUNTER.read_history()
    if not os.path.exists(PATH_POST):
        os.mkdir(PATH_POST)
    make_index_dir("tags", "标签")
    make_index("tags", TAG_TBC)
    make_index("tags", TAG_FIN)
    make_index("tags", TAG_AI_COMMENT)
    make_index_dir("category", "分类")

    if len(sys.argv) > 1 and sys.argv[1] == "ONLINE":
        post_all(FILE_ROOT, COUNTER, True)
        defs = get_predef(os.path.join(FILE_ROOT, INDEX_NAME))
        change = get_pre_key(defs, "change")
        for i in change:
            mark_as_post(i, COUNTER)
        clear_post()
    elif len(sys.argv) > 1:
        for i in search_by_keyword(sys.argv[1]):
            if PATH_LOG not in short_path(i):
                post_work(i, COUNTER)
                mark_as_post(i, COUNTER)
            else:
                post_log(i)
    else:
        post_all(FILE_ROOT, COUNTER, True)
