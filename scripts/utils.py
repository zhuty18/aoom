# coding = utf-8

"""功能函数"""

import os
import re
import time

from name_def import names
from personal import (
    COMMIT_TIME,
    DOC_ROOT,
    HIDE_DEFAULT,
    HIDE_HEAD,
    HIDE_TAIL,
    IGNORE_FILES,
    IGNORE_PATHS,
    NAME_OF_DIR,
    PATH_HISTORY,
    TAGS_CHARACTER,
    TAGS_CP,
    TAGS_ORGANIZATION,
    TAGS_PRIORITY,
    TIME_FORMAT,
)


def format_time(timestamp: float = COMMIT_TIME, time_format=TIME_FORMAT) -> str:
    """格式化某个时间戳，默认为当下"""
    if not timestamp:
        timestamp = COMMIT_TIME
    return time.strftime(time_format, time.localtime(timestamp))


def get_log_time(log_time: str) -> float:
    """获取log时间"""
    time_struct = time.strptime(log_time, "%a %b %d %H:%M:%S %Y")
    local_time = time.localtime(time.mktime(time_struct))
    return time.mktime(local_time)


def get_time(time_str: str | None = None) -> float:
    """获取某个时间对应的时间戳"""
    return (
        time.mktime(time.strptime(time_str, TIME_FORMAT))
        if time_str
        else COMMIT_TIME
    )


def line_length(s: str) -> int:
    """行长度计算"""
    a = s.strip("#")
    a = a.strip()
    a = a.replace("</br>", "")
    a = a.replace("<br>", "")
    # if a.startswith("[^"):
    #     return 0
    res = 0
    t = False
    for i in a:
        if i.isascii():
            t = True
            if i == " ":
                res += 1
        else:
            res += 1
            if t:
                res += 1
                t = False
    if t:
        res += 1
    return res


class FileBasic:
    """基础文件"""

    def __init__(self, path):
        self._path_ = root_path(path)

        self._filename_ = None

    def is_exist(self):
        """文件是否存在"""
        return os.path.exists(self._path_)

    def path(self):
        """文件路径"""
        return self._path_

    def filename(self):
        """文件名"""
        if self._filename_ is None:
            self._filename_ = (
                self._path_.replace("\\", "/").replace(".md", "").split("/")[-1]
            )
        return self._filename_

    def is_ignore(self):
        """忽略"""
        for i in IGNORE_FILES:
            if i in self._path_:
                return True
        for i in IGNORE_PATHS:
            if i in self._path_:
                return True
        return "_" in self._path_ or (not self._path_.endswith(".md"))


def cut_name(name: str, index: list[int], cutter: str) -> str:
    """名字切分"""
    tmp = name.split(cutter)
    res = []
    for i in index:
        res.append(tmp[i])
    return cutter.join(res)


def full_names():
    """全名"""
    for i in names:
        if len(i[0].split(" ")) == 3:
            yield (cut_name(i[0], [0, 2], " "), cut_name(i[1], [0, 2], "·"))
        else:
            yield i


def short_names():
    """昵称"""
    for i in names:
        if len(i[0].split(" ")) == 3:
            yield (cut_name(i[0], [1, 2], " "), cut_name(i[1], [1, 2], "·"))


def name_pieces():
    """名字切片"""
    for i in names:
        t0 = i[0].split(" ")
        t1 = i[1].split("·")
        for i, _ in enumerate(t0):
            yield (t0[i], t1[i])
    yield ("Bar", "小巴")
    yield ("Alf", "阿福")


def wrong_translates():
    """自动校正"""
    yield ("韦斯特 Side", "West Side")
    yield ("Jay森", "Jason")
    yield ("膝Guy", "膝盖")
    yield ("覆Guy", "覆盖")
    yield ("舱Guy", "舱盖")
    yield ("Jay西卡", "杰西卡")
    yield ("Jo 马龙", "Jo Malone")
    yield ("马龙（马龙）", "马龙（Malone）")
    yield ("迈彻斯（迈彻斯）", "迈彻斯（Matches）")
    yield (" 奥·古", "·奥·古")
    yield ("Mr. 韦恩", "Mr. Wayne")


def doc_root():
    """文档根目录"""
    return os.path.join(os.getcwd(), DOC_ROOT)


def root_path(path: str, root=os.getcwd()) -> str:
    """文件名缩短至根目录"""
    return (
        path.replace("/", "\\")
        .replace(root.replace("/", "\\"), "")
        .replace("\\", "/")
        .strip("/")
    )


def doc_path(path):
    """文件名缩短至doc文件夹"""
    res = root_path(path, doc_root())
    res = root_path(res, DOC_ROOT)
    return res


def folder_path(path):
    """上级路径"""
    path = path.replace("\\", "/").split("/")
    path.pop()
    return "/".join(path)


def name_of_dir(i: str):
    """路径名"""
    return NAME_OF_DIR.get(doc_path(i).strip(), None)


def search_file(filepath, key, strict, content):
    """在文件中搜索关键字"""
    f = FileBasic(filepath)
    if not f.is_ignore():
        if strict:
            if f.filename() == key:
                return True
        elif not content:
            if key in f.filename():
                return True
        else:
            with open(f.path(), "r", encoding="utf-8") as file:
                have = False
                for i in file.readlines():
                    if key in i:
                        if not have:
                            print(f.path())
                            have = True
                        print(i.strip())
                if have:
                    print()
                    return True
    return False


def search_dir(path: str, key: str, strict=False, content=False):
    """在目录下搜索关键字"""
    res = []
    for i in os.listdir(path):
        i = os.path.join(path, i)
        if os.path.isdir(i):
            res.extend(search_dir(i, key, strict, content))
        elif search_file(i, key, strict, content):
            res.append(i)
    return res


def filenames_of_key(key):
    """搜索文件名含有关键词的文件"""
    return search_dir(doc_root(), key)


def filename_is_key(name):
    """根据文件名搜索文件"""
    tmp = search_dir(doc_root(), name, strict=True)
    return tmp[0] if tmp else None


def file_has_key(name):
    """搜索内容含有关键字的文件名"""
    return search_dir(doc_root(), name, content=True)


def hide_fin():
    """自动隐藏已完成的内容"""
    finished = []
    with open(PATH_HISTORY, "r", encoding="utf8") as f:
        for l in f.readlines():
            l = l.strip().split("\t")
            if l[-1] == "True":
                finished.append(f"**/{l[0]}.md")

    try:
        with open(".vscode/settings.json", "r", encoding="utf8") as f:
            ori = f.read()
    except FileNotFoundError:
        ori = f"""{{
  "files.exclude": {{
    {HIDE_HEAD}
    {HIDE_DEFAULT}
    {HIDE_TAIL}
  }}
}}"""
        if not os.path.exists(".vscode"):
            os.mkdir(".vscode")
        with open(
            ".vscode/settings.json", "w", encoding="utf8", newline="\n"
        ) as f:
            f.write(ori)
    s0 = re.findall(re.compile(r"\"files.exclude\": {.*?}", re.S), ori)[0]
    s1 = re.findall(re.compile(rf"{HIDE_HEAD}\n(.*?){HIDE_TAIL}", re.S), s0)[0]

    s2 = '": true,\n    "'.join(finished)
    s2 = f'    "{s2}": true,\n    '

    if finished:
        ori = ori.replace(s1, s2)
    with open(".vscode/settings.json", "w", encoding="utf8", newline="\n") as f:
        f.write(ori)


def tag_order(tag):
    """标签显示优先级"""
    # 优先级：特殊 -> CP -> AU -> 角色 -> 组织 -> 其他 -> AI -> 完成度
    if tag in TAGS_PRIORITY:
        return -1
    if tag in TAGS_CP:
        return 0
    elif "au" in tag or "ABO" in tag:
        return 1
    elif tag in TAGS_CHARACTER:
        return 2
    elif tag in TAGS_ORGANIZATION:
        return 3
    else:
        return 4


def mk_dirs(path):
    """建立文件夹"""
    l = root_path(path).split("/")
    for i in range(len(l) - 1):
        if not os.path.exists("/".join(l[: i + 1])):
            os.mkdir("/".join(l[: i + 1]))
