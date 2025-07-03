# coding = utf-8

"""功能函数"""

import os
import re
import time

from name_def import names
from personal import (
    AI_PATH,
    COMMIT_TIME,
    DOC_ROOT,
    IGNORE_FILES,
    IGNORE_PATHS,
    TAGS_CP,
    TAGS_优先,
    TAGS_组织,
    TAGS_角色,
    历史文件,
    文件夹名,
    时间格式,
    隐藏区初始值,
    隐藏区开头,
    隐藏区结尾,
)


def 格式化时间(时间戳: float = COMMIT_TIME, 时间格式=时间格式) -> str:
    """格式化某个时间戳，默认为当下"""
    if not 时间戳:
        时间戳 = COMMIT_TIME
    return time.strftime(时间格式, time.localtime(时间戳))


def 获取log时间(log时间: str) -> str:
    """获取log时间"""
    时间结构体 = time.strptime(log时间, "%a %b %d %H:%M:%S %Y")
    本地时间 = time.localtime(time.mktime(时间结构体))
    return time.mktime(本地时间)


def 获取时间戳(时间字符串: str = None) -> float:
    """获取某个时间对应的时间戳"""
    return (
        time.mktime(time.strptime(时间字符串, 时间格式))
        if 时间字符串
        else COMMIT_TIME
    )


def 行长度(s: str) -> int:
    """行长度计算"""
    a = s.strip("#")
    a = a.strip()
    a = a.replace("</br>", "")
    a = a.replace("<br>", "")
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
    yield (" 奥·古", "·奥·古")
    yield ("Mr. 韦恩", "Mr. Wayne")


def 文档根目录():
    """文档根目录"""
    return os.path.join(os.getcwd(), DOC_ROOT)


def 相对路径(path: str, root=os.getcwd()) -> str:
    """文件名缩短至根目录"""
    return (
        path.replace("/", "\\")
        .replace(root.replace("/", "\\"), "")
        .replace("\\", "/")
        .strip("/")
    )


def doc_path(path):
    """文件名缩短至doc文件夹"""
    res = 相对路径(path, 文档根目录())
    res = 相对路径(res, DOC_ROOT)
    return res


def 文件夹路径(path):
    """上级路径"""
    path = path.replace("\\", "/").split("/")
    path.pop()
    return "/".join(path)


def name_of(path):
    """文件名"""
    return path.replace("\\", "/").replace(".md", "").split("/")[-1]


def 路径名(i: str):
    """路径名"""
    return 文件夹名.get(doc_path(i).strip(), None)


class 搜索文件:
    """搜索含有关键词的文件"""

    def __init__(self, key: str, 严格相同=False):
        self.key = key
        self.res = []
        self._严格 = 严格相同
        self.check_dir(文档根目录())
        if not self.res:
            raise FileNotFoundError(
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
            elif i.endswith(".md") and not AI_PATH in 相对路径(i):
                if self._严格:
                    if name_of(i) == self.key:
                        self.res.append(i)
                else:
                    if match_keys([self.key], i):
                        self.res.append(i)

    def result(self):
        """搜索结果"""
        return self.res


def 获取文件_关键字(key):
    """搜索含有关键词的文件"""
    return 搜索文件(key).result()


def 获取文件_文件名(name):
    """根据文件名搜索文件"""
    return 搜索文件(name, True).result()[0]


def 隐藏已完结():
    """自动隐藏已完成的内容"""
    finished = []
    with open(历史文件, "r", encoding="utf8") as f:
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
    {隐藏区开头}
    {隐藏区初始值}
    {隐藏区结尾}
  }}
}}"""
        if not os.path.exists(".vscode"):
            os.mkdir(".vscode")
        with open(".vscode/settings.json", "w", encoding="utf8") as f:
            f.write(ori)
    s0 = re.findall(re.compile(r"\"files.exclude\": {.*?}", re.S), ori)[0]
    s1 = re.findall(re.compile(rf"{隐藏区开头}\n(.*?){隐藏区结尾}", re.S), s0)[
        0
    ]

    s2 = '": true,\n    "'.join(finished)
    s2 = f'    "{s2}": true,\n    '

    if finished:
        ori = ori.replace(s1, s2)
    with open(".vscode/settings.json", "w", encoding="utf8") as f:
        f.write(ori)


def 完结路径(path):
    """路径是否默认为完结"""
    fin_path = {"batlantern": True, "blob": True, "logs": True}
    return fin_path.get(doc_path(path), False)


def tag优先级(tag):
    """标签显示优先级"""
    # 优先级：特殊 -> CP -> AU -> 角色 -> 组织 -> 其他 -> AI -> 完成度
    if tag in TAGS_优先:
        return -1
    if tag in TAGS_CP:
        return 0
    elif "au" in tag or "ABO" in tag:
        return 1
    elif tag in TAGS_角色:
        return 2
    elif tag in TAGS_组织:
        return 3
    else:
        return 4


def ignore_in_format(filename):
    """格式化中忽略此索引文件"""
    for i in IGNORE_FILES:
        if i in filename:
            return True
    for i in IGNORE_PATHS:
        if i in 相对路径(filename):
            return True
    return "_" in filename


def 制作文件夹(路径):
    """建立文件夹"""
    l = 路径.split("/")
    for i in range(len(l) - 1):
        if not os.path.exists("/".join(l[: i + 1])):
            os.mkdir("/".join(l[: i + 1]))
