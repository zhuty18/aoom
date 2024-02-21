# coding = utf-8

"""字数记录"""

import os
import re
import markdown
from utils import dir_name, dirs, html_head, short_path


def read_index(path):
    """读取索引下的目录"""
    l = []
    try:
        with open(os.path.join(path, "README.md"), "r", encoding="utf8") as r:
            k = r.read()
            k1 = re.findall(re.compile(r"## Finished(.*?)$", re.S), k)
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


def auto_hide(finished, forced):
    """自动隐藏已完成的内容"""
    with open(".vscode/settings.json", "r", encoding="utf8") as f:
        ori = f.read()
    s0 = re.findall(re.compile(r"\"files.exclude\": {.*?}", re.S), ori)[0]
    s1 = re.findall(re.compile(r"// auto begins\n(.*?)// auto ends", re.S), s0)[0]

    finished.sort()
    finished = [x.replace(".md", ".*") for x in finished]
    s2 = '": true,\n"'.join(finished)
    s2 = f'"{s2}": true,\n'
    if forced:
        ori = ori.replace(s1, s2)
    else:
        ori = ori.replace("// auto ends", s2 + "\n// auto ends")
    with open(".vscode/settings.json", "w", encoding="utf8") as f:
        f.write(ori)


def markdown_to_html(filename, path, text, title):
    """生成markdown内容的html"""
    text = text.replace("\n\n\n\n\n\n\n", "\n\n<br>\n\n<br>\n\n<br>\n")
    text = text.replace("\n\n\n", "\n\n<br>\n")
    html = markdown.markdown(text, extensions=["tables"], output_format="html")
    output_filename = filename.replace(".md", ".html")
    output_filename = output_filename.replace("README", "index")
    with open(os.path.join(path, output_filename), "w", encoding="utf8") as f:
        if "README" in filename:
            html = html.replace(".md", ".html")
        f.write(html_head(title))
        f.write(html)


def to_html(filename: str, path: str):
    """生成markdown文件的html"""
    with open(os.path.join(path, filename), "r", encoding="utf8") as f:
        text = f.read()
    title = filename.replace(".md", "")
    markdown_to_html(filename, path, text, title)


def index_html(path: str):
    """生成索引文件的html"""
    try:
        with open(os.path.join(path, "README.md"), "r", encoding="utf8") as r:
            k = r.read()
            k1 = re.findall(re.compile(r"## Finished(.*?)$", re.S), k)
            if len(k1):
                text = f"# {dir_name(path)}{k1[0]}"
                markdown_to_html("README.md", path, text, dir_name(path))
    except FileNotFoundError:
        text = dirs(path)
        markdown_to_html("README.md", path, text, dir_name(path))


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
                for j in changes:
                    if f"{i[0]}/{i[1]}" == j:
                        to_html(i[1], i[0])
        # 当前目录
        index_html(path)


def all_html(changes: list = None, force: bool = False):
    """自动生成仓库的html"""
    to_html("README.md", os.getcwd())
    path = os.listdir(os.getcwd())
    for i in path:
        if os.path.isdir(i) and dir_name(i):
            dir_html(i, changes, force)
