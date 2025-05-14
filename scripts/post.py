# coding = utf-8
"""
发布文件到POST_PATH文件夹
"""
import os
import sys

from personal import (
    AI批评TAG,
    INDEX文件,
    POST日期格式,
    POST路径,
    完结TAG,
    未完TAG,
    首页POST上限,
    文档根,
    日志路径,
)
from utils import (
    add_predef,
    excerpt,
    get_pre_key,
    get_predef,
    is_ai,
    make_index,
    make_index_dir,
    mark_fin,
    mark_post,
    name_of,
    search_by_keyword,
    write_predef,
    文件夹路径,
    格式化时间,
    相对路径,
    获取时间戳,
    路径名,
)
from work_record import 字数统计器

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
        date = 格式化时间(获取时间戳(default_time), POST日期格式)

    # 生成post名
    post_name = f"{date}-{name}.md"
    post_path = os.path.join(POST路径, post_name)

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
    target = 相对路径(filename).replace(".md", "")
    if target.endswith("."):
        target = target[:-1] + "/html"
    add_predef(post_path, "target", target)
    # 添加类别路径
    add_predef(post_path, "cat_url", 相对路径(文件夹路径(filename)))
    # 添加摘要
    add_predef(post_path, "excerpt_separator", "<!--more-->")

    # 记录post
    POST_LIST.append(post_name)

    # 建立标签索引
    for x in get_pre_key(pre_d, "tags"):
        make_index("tags", x)
    # 建立类别索引
    if 路径名(文件夹路径(filename)):
        make_index("category", 路径名(文件夹路径(filename)))

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


def clear_post(post_max=首页POST上限):
    """控制post上限"""
    if post_max >= 0:
        POST_LIST.sort()
        POST_LIST.reverse()

        posted = 0
        for item in POST_LIST:
            posted += mark_post(os.path.join(POST路径, item))
            if posted == post_max:
                break


def mark_as_post(filename, counter):
    """标记本次改动的文件为post"""
    his = counter.history[name_of(filename)]
    for item in POST_LIST:
        if his.name in item:
            mark_post(os.path.join(POST路径, item))
            break


def post_all(path, counter, allow_tbc=False):
    """发布所有文件"""
    for item in os.listdir(path):
        subdir = os.path.join(path, item)
        if 路径名(subdir):
            post_all(subdir, counter, allow_tbc)
        elif 日志路径 in 相对路径(path) and name_of(item) in counter.history:
            post_log(subdir)
        elif (
            name_of(item) in counter.history
            and (not os.path.isdir(subdir))
            and (not is_ai(subdir))
        ):
            if counter.history[name_of(item)].fin or allow_tbc:
                post_work(subdir, counter)


if __name__ == "__main__":
    COUNTER = 字数统计器()
    COUNTER.读取历史()
    if not os.path.exists(POST路径):
        os.mkdir(POST路径)
    make_index_dir("tags", "标签")
    make_index("tags", 未完TAG)
    make_index("tags", 完结TAG)
    make_index("tags", AI批评TAG)
    make_index_dir("category", "分类")

    if len(sys.argv) > 1 and sys.argv[1] == "ONLINE":
        post_all(文档根, COUNTER, True)
        defs = get_predef(os.path.join(文档根, INDEX文件))
        change = get_pre_key(defs, "change")
        for i in change:
            mark_as_post(i, COUNTER)
        clear_post()
    elif len(sys.argv) > 1:
        for i in search_by_keyword(sys.argv[1]):
            if 日志路径 not in 相对路径(i):
                post_work(i, COUNTER)
                mark_as_post(i, COUNTER)
            else:
                post_log(i)
    else:
        post_all(文档根, COUNTER, True)
