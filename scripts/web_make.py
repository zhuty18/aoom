# coding = utf-8

"""字数记录"""

import os
import re

import markdown
from personal import INDEX_NAME, INDEX_NAME_FULL, PATH_CHANGE_SAVE, TITLE_FINS
from utils import dir_name, dirs, doc_dir, html_head, name_of, short_path


def read_index(path):
    """读取索引下的目录"""
    l = []
    try:
        with open(
            os.path.join(path, INDEX_NAME_FULL), "r", encoding="utf8"
        ) as r:
            k = r.read()
            pattern = f"{TITLE_FINS}(.*?)$"
            k1 = re.findall(re.compile(repr(pattern), re.S), k)
            if len(k1):
                k2 = re.findall(re.compile(r"[(](.*?)[)]", re.S), k1[0])
                for j in k2:
                    h: str = os.path.join(path, j)
                    h = short_path(h).split("/")
                    title = h.pop(-1)
                    h = "/".join(h)
                    l.append((h, title))
    except FileNotFoundError:
        pass
    return l


def markdown_to_html(filepath, text, title):
    """生成markdown内容的html"""
    text = text.replace("\n\n\n\n\n\n\n", "\n\n<br>\n\n<br>\n\n<br>\n")
    text = text.replace("\n\n\n", "\n\n<br>\n")
    html = markdown.markdown(text, extensions=["tables"], output_format="html")
    output_filepath = filepath.replace(".md", ".html")
    output_filepath = output_filepath.replace(INDEX_NAME_FULL, INDEX_NAME)
    with open(output_filepath, "w", encoding="utf8") as f:
        if INDEX_NAME_FULL in filepath:
            html = html.replace(".md", ".html")
        f.write(html_head(title))
        f.write(html)


def to_html(filepath: str):
    """生成markdown文件的html"""
    with open(filepath, "r", encoding="utf8") as f:
        text = f.read()
    title = name_of(filepath)
    markdown_to_html(filepath, text, title)


def index_html(path: str):
    """生成索引文件的html"""
    try:
        with open(
            os.path.join(path, INDEX_NAME_FULL), "r", encoding="utf8"
        ) as r:
            k = r.read()
            k1 = re.findall(re.compile(r"## Finished(.*?)$", re.S), k)
            if len(k1):
                text = f"# {dir_name(path)}{k1[0]}"
                markdown_to_html(
                    os.path.join(path, INDEX_NAME_FULL), text, dir_name(path)
                )
    except FileNotFoundError:
        text = dirs(path)
        if text:
            markdown_to_html(
                os.path.join(path, INDEX_NAME_FULL), text, dir_name(path)
            )


def dir_html(path, changes, force):
    """生成目录的html"""
    change = False
    sp = short_path(path)
    if changes:
        for i in changes:
            if sp in i:
                change = True
    if change or force:
        # 子目录
        for i in os.listdir(path):
            t = os.path.join(path, i)
            if os.path.isdir(t) and dir_name(t):
                dir_html(t, changes, force)
        # 当前目录文档
        l = read_index(path)
        if l:
            for i in l:
                if force:
                    to_html(os.path.join(i[1], i[0]))
                if changes:
                    for j in changes:
                        if f"{i[0]}/{i[1]}" == j:
                            to_html(os.path.join(i[1], i[0]))
        # 当前目录
        index_html(path)


def all_html(force: bool):
    """自动生成仓库的html"""

    with open(PATH_CHANGE_SAVE, "r", encoding="utf8") as f:
        changes = f.read().split("\n")

    to_html(os.path.join(INDEX_NAME_FULL, doc_dir()))
    path = os.listdir(doc_dir())
    for i in path:
        i = os.path.join(doc_dir(), i)
        if os.path.isdir(i) and dir_name(i):
            dir_html(i, changes, force)
