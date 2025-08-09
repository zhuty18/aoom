# coding = utf-8

"""
发布文件到POST_PATH文件夹
"""

import os

from file_status import FilePost
from personal import DOC_ROOT, MAXIMUM_POST, POST_PATH
from utils import mk_dirs, name_of_dir

POST_LIST = []


def post_file(filename):
    """发布单个文件"""
    POST_LIST.append(FilePost(filename).post())


def post_extra_until(post_max=MAXIMUM_POST):
    """额外发布指定量"""
    if post_max >= 0:
        POST_LIST.sort(key=lambda x: x[0], reverse=True)

        posted = 0
        for item in POST_LIST:
            posted += FilePost(item[1]).mark_post()
            if posted == post_max:
                break


def post_all_files(path, allow_tbc=False):
    """发布所有文件"""
    others = []
    for item in os.listdir(path):
        file_path = os.path.join(path, item)
        if name_of_dir(file_path):
            if "AI" not in file_path:
                others.append(file_path)
            else:
                post_all_files(file_path, allow_tbc)
        else:
            file_post = FilePost(file_path)
            if file_post.is_post():
                if file_post.is_fin() or allow_tbc:
                    post_file(file_path)
    for item in others:
        post_all_files(item, allow_tbc)


if __name__ == "__main__":
    mk_dirs(POST_PATH)

    post_all_files(DOC_ROOT, True)
    post_extra_until()
