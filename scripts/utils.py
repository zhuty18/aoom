# coding = utf-8

"""功能函数"""

import os
import time
import re
from personal import (
    COMMIT_TIME,
    TIME_FORMAT,
    WEB_NAME,
    FIN_HEAD,
    FIN_TAIL,
    FIN_TEM,
    HISTORY_PATH,
    FILE_ROOT,
    PREVIEW_LENGTH,
    INDEX_NAME,
    INDEX_FULL_NAME,
    DIR_NAMES,
)
from name_def import names


def format_time(timestamp: float = COMMIT_TIME, time_format=TIME_FORMAT) -> str:
    """格式化某个时间戳，默认为当下"""
    t = time.localtime(timestamp)
    res = time.strftime(time_format, t)
    return res


def format_log_time(time_str) -> str:
    """格式化从git log中读取的时间"""
    tmp = time.strptime(time_str, "%a %b %d %H:%M:%S %Y")
    tmp = time.localtime(time.mktime(tmp))
    return format_time(time.mktime(tmp))


def get_time(time_str: str = None) -> float:
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


def file_length(filename: str) -> int:
    """文件长度计算"""
    res = 0
    with open(filename, "r", encoding="utf8") as f:
        note = False
        for i in f.readlines():
            if i.strip() == "---":
                note = not note
                continue
            if note:
                continue
            res += line_length(i.strip())
    return res


def file_fin(filename: str) -> bool:
    """完成情况检测"""
    if path_fin(path_of(filename)):
        return True
    with open(filename, "r", encoding="utf8") as f:
        text = f.read()
        ends = {"END", "完结", "Q.E.D."}
        for i in ends:
            if f"{i}\n" in text:
                return True
    return False


def match_keys(keys: list, name: str) -> bool:
    """是否含有至少一个关键词"""
    for i in keys:
        if i in name:
            return True
    return False


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
    yield ("布鲁斯 Wayyyne", "布鲁斯·韦——恩")
    yield (" 奥·古", "·奥·古")
    yield ("Mr. 韦恩", "Mr. Wayne")


def doc_dir():
    """文档根目录"""
    return os.path.join(os.getcwd(), FILE_ROOT)


def sub_path(path):
    """对下级文件链接"""
    tmp = path.replace("\\", "/")
    return tmp.split("/")[-1]


def short_path(path: str, root=os.getcwd()) -> str:
    """文件名缩短至根目录"""
    return (
        path.replace("/", "\\")
        .replace(root.replace("/", "\\"), "")
        .replace("\\", "/")
        .strip("/")
    )


def doc_path(path):
    """文件名缩短至doc文件夹"""
    res = short_path(path, doc_dir())
    res = short_path(res, FILE_ROOT)
    return res


def path_of(path):
    """上级路径"""
    path = path.replace("\\", "/").split("/")
    path.pop()
    return "/".join(path)


def name_of(path):
    """文件名"""
    return path.replace("\\", "/").replace(".md", "").split("/")[-1]


def dir_name(i: str):
    """路径名"""
    i = doc_path(i).strip()
    return DIR_NAMES.get(i, None)


def dirs(path: str = doc_dir()):
    """全目录信息"""
    text = f"# {dir_name(path)}\n\n"
    text += "|所有文件夹|\n"
    text += "|:-|\n"
    has = False
    dir_list = os.listdir(path)
    dir_list.sort()
    for i in dir_list:
        full_path = os.path.join(path, i)
        if os.path.isdir(full_path) and dir_name(full_path) is not None:
            name = dir_name(full_path)
            if name:
                text += f"|[{dir_name(full_path)}]({sub_path(full_path)})|\n"
                has = True
    return text if has else None


def html_head(title: str) -> str:
    """网页头数据"""
    if title == name_of(INDEX_FULL_NAME) or title == name_of(INDEX_NAME):
        title = WEB_NAME
    return f"""<!DOCTYPE html>
<head>
    <title>{title}</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
"""


class SearchForFile:
    """搜索含有关键词的文件"""

    def __init__(self, key: str):
        self.key = key
        self.res = []
        self.check_dir(doc_dir())
        if not self.res:
            print(
                "没有找到"
                + self.key
                + "！请确认是否存在含有该字符串的文件名（不含路径）！"
            )

    def check_dir(self, path: str):
        """检查目录下的文件"""
        for i in os.listdir(path):
            i = os.path.join(path, i)
            if os.path.isdir(i):
                self.check_dir(i)
            else:
                if match_keys([self.key], i) and i.endswith(".md"):
                    self.res.append(i)

    def result(self):
        """搜索结果"""
        return self.res


def search_by_keyword(key):
    """搜索含有关键词的文件"""
    return SearchForFile(key).result()


def auto_hide():
    """自动隐藏已完成的内容"""
    finished = []
    with open(HISTORY_PATH, "r", encoding="utf8") as f:
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
        {FIN_HEAD}
        {FIN_TEM}
        {FIN_TAIL}
    }}
}}"""
        if not os.path.exists(".vscode"):
            os.mkdir(".vscode")
        with open(".vscode/settings.json", "w", encoding="utf8") as f:
            f.write(ori)
    s0 = re.findall(re.compile(r"\"files.exclude\": {.*?}", re.S), ori)[0]
    s1 = re.findall(re.compile(rf"{FIN_HEAD}\n(.*?){FIN_TAIL}", re.S), s0)[0]

    s2 = '": true,\n        "'.join(finished)
    s2 = f'        "{s2}": true,\n        '

    if finished:
        ori = ori.replace(s1, s2)
    with open(".vscode/settings.json", "w", encoding="utf8") as f:
        f.write(ori)


def path_fin(path):
    """路径是否默认为完结"""
    fin_path = {"batlantern": True, "blob": True}
    return fin_path.get(doc_path(path), False)


def preview(filename):
    """获取文件预览"""
    pre = ""
    with open(filename, "r", encoding="utf8") as f:
        yaml = False
        for i in f.readlines():
            if i == "---\n":
                yaml = not yaml
                continue
            if yaml:
                continue
            if i.startswith("#"):
                continue
            pre += i
            if len(pre) > PREVIEW_LENGTH:
                break
            if "\n\n\n" in pre:
                pre = pre.split("\n\n\n")[-1]
    return pre.strip().split("\n")[0]


def get_predefine(filename):
    """读取预定义内容"""
    with open(filename, "r", encoding="utf8") as f:
        content = f.read()
        if content.startswith("---"):
            pre_d = re.findall(re.compile(r"---\n(.*)\n---\n", re.S), content)[
                0
            ]
            return pre_d
    return None


def get_pre_key(pre_d, keyword):
    """从预定义头中读取关键字参数"""
    l = []
    if pre_d and keyword in pre_d:
        for item in pre_d.split("\n"):
            if keyword in item:
                item = item.strip()
                l = item.split(" ")
                l.pop(0)
            elif item.startswith("  - "):
                l.append(item.strip("  - "))
    return l


def make_index(kind, name):
    """制作jekyll索引"""
    path = os.path.join(os.getcwd(), kind)
    if not os.path.exists(os.path.join(path, name + ".md")):
        with open(os.path.join(path, name + ".md"), "w", encoding="utf8") as f:
            f.write("---\n")
            f.write(f"layout: {kind}\n")
            f.write(f"{kind}: {name}\n")
            f.write("---\n")


def make_index_dir(kind):
    """制作jekyll索引路径"""
    path = os.path.join(os.getcwd(), kind)
    if not os.path.exists(path):
        os.mkdir(path)
        with open(os.path.join(path, INDEX_NAME), "w", encoding="utf8") as f:
            f.write("---\n")
            f.write(f"layout: {kind}_all\n")
            f.write("---\n")


def title_of(filename):
    """获得文件标题"""
    title = name_of(filename)
    with open(filename, "r", encoding="utf8") as f:
        content = f.read()
        for i in content.split("\n\n"):
            if i.startswith("# "):
                title = i.replace("# ", "")
                break
    return title
