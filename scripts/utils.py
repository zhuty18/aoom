# coding = utf-8

"""功能函数"""

import os
import time
import re
from personal import COMMIT_TIME, TIME_FORMAT, WEB_NAME, FIN_HEAD, FIN_TAIL, FIN_TEM, HISTORY_PATH


def format_time(timestamp: float = COMMIT_TIME) -> str:
    """格式化某个时间戳，默认为当下"""
    t = time.localtime(timestamp)
    res = time.strftime(TIME_FORMAT, t)
    return res


def format_log_time(time_str) -> str:
    """格式化从git log中读取的时间"""
    tmp = time.strptime(time_str, "%a %b %d %H:%M:%S %Y")
    tmp = time.localtime(time.mktime(tmp))
    return format_time(time.mktime(tmp))


def get_time(time_str: str = None) -> float:
    """获取某个时间对应的时间戳"""
    return time.mktime(time.strptime(time_str, TIME_FORMAT)) if time_str else COMMIT_TIME


def line_length(s: str) -> int:
    """行长度计算"""
    a: str = s.strip("#")
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
        for i in f.readlines():
            res += line_length(i.strip())
    return res


def file_fin(filename: str) -> bool:
    """完成情况检测"""
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


nick_names: list[tuple[str, str]] = [
    # nick names
    ("Dickie-bird", "迪基鸟"),
    ("Diana", "戴安娜"),
    ("Jay", "杰"),
    ("Babs", "芭布斯"),
    ("Dante", "但丁"),
]

names: list[tuple[str, str]] = [
    # all people names
    ("Richard Dick Grayson", "理查德·迪克·格雷森"),
    ("Stephanie Steph Brown", "史蒂芬妮·史蒂·布朗"),
    ("Roy Harper", "罗伊·哈珀"),
    ("Cassandra Cassie Sandsmark", "卡珊德拉·凯西·珊德马克"),
    ("Damian Wayne", "达米安·韦恩"),
    ("Bruce Wayne", "布鲁斯·韦恩"),
    ("Cassandra Cass Cain", "卡珊德拉·卡珊·该隐"),
    ("Jason Todd", "杰森·陶德"),
    ("Clark Kent", "克拉克·肯特"),
    ("Alfred Pennyworth", "阿尔弗雷德·潘尼沃斯"),
    ("Harold Hal Jordan", "哈罗德·哈尔·乔丹"),
    ("Timothy Tim Drake", "提摩西·提姆·德雷克"),
    ("Barry Allen", "巴里·艾伦"),
    ("Bart Allen", "巴特·艾伦"),
    ("Jessica Jess Cruz", "杰西卡·杰西·克鲁兹"),
    ("John Stewart", "约翰·斯图尔特"),
    ("Oliver Ollie Queen", "奥利弗·奥利·奎恩"),
    ("Dinah Lance", "戴娜·兰斯"),
    ("Lian Harper", "莉安·哈珀"),
    ("Lucius Fox", "卢修斯·福克斯"),
    ("Kyle Rayner", "凯尔·雷纳"),
    ("Guy Gardner", "盖·加德纳"),
    ("Simon Baz", "西蒙·巴兹"),
    ("Conner Kent", "康纳·肯特"),
    ("Connor Hawke", "康纳·霍克"),
    ("Perry White", "佩里·怀特"),
    ("Lois Lane", "露易丝·莲恩"),
    ("Matches Malone", "火柴·马龙"),
    ("Carmine Falcone", "卡迈恩·法尔科内"),
]


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


def short_path(path: str) -> str:
    """文件名缩短"""
    return path.replace(os.getcwd(), "").replace("\\", "/").strip("/")


def dir_name(i: str):
    """路径名"""
    dir_names = {
        "DC": "DC",
        "DM": "数码宝贝",
        "GTM": "银魂",
        "FT": "童话系列（欧美）",
        "DMC": "鬼泣",
        "M": "漫威",
        "O": "原创",
        "Others": "其他",
        "QZ": "全职",
        "SC": "影评",
        "SWY": "食物语",
        "translation": "翻译",
        "X": "X战警",
        "XJ": "仙剑",
        "YYS": "阴阳师",
        "YWJ": "曳尾记",
        "O/ON": "原创小说",
        "translation/batfamily": "蝙家",
        "translation/BruceHal": "蝙绿蝙",
        "": "all categories",
        "batlantern": "蝙绿官糖",
    }
    i = short_path(i)
    return dir_names.get(i, None)


def dirs(path: str = os.getcwd()):
    """全目录信息"""
    text = f"# {dir_name(path)}\n\n"
    text += "|所有文件夹|\n"
    text += "|:-|\n"
    has = False
    dir_list = os.listdir(path)
    dir_list.sort()
    for i in dir_list:
        if path != os.getcwd():
            i = os.path.join(path, i)
        if os.path.isdir(i) and dir_name(i) is not None:
            name = dir_name(i)
            if name:
                text += f"|[{dir_name(i)}](/{i})|\n"
                has = True
    return text if has else None


def html_head(title: str) -> str:
    """网页头数据"""
    if title == "README":
        title = WEB_NAME
    style = "/theme/dracula.css"
    return f"""<!DOCTYPE html>
<head>
    <title>{title}</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
"""
    # <style type="text/css">
    #     @import"/data{style}";
    # </style>


class SearchForFile:
    """搜索含有关键词的文件"""

    def __init__(self, key: str):
        self.key = key
        self.res = []
        self.check_dir(os.getcwd())
        if not self.res:
            print("没有找到" + self.key + "！请确认是否存在含有该字符串的文件名（不含路径）！")

    def check_dir(self, path: str):
        """检查目录下的文件"""
        for i in os.listdir(path):
            if os.path.isdir(i):
                self.check_dir(i)
            else:
                if match_keys([self.key], i) and i.endswith(".md"):
                    self.res.append((i, path))

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
            if bool(l[-1]):
                finished.append(f"**/{l[0]}*")

    try:
        with open(".vscode/settings.json", "r", encoding="utf8") as f:
            ori = f.read()
    except FileNotFoundError:
        ori = f"""{{
    "files.exclude":{{
        {FIN_HEAD}
        {FIN_TEM}
        {FIN_TAIL}
    }}
}}"""
        with open(".vscode/settings.json", "w", encoding="utf8") as f:
            f.write(ori)
    s0 = re.findall(re.compile(r"\"files.exclude\": {.*?}", re.S), ori)[0]
    s1 = re.findall(re.compile(rf"{FIN_HEAD}\n(.*?){FIN_TAIL}", re.S), s0)[0]

    s2 = '": true,\n"'.join(finished)
    s2 = f'"{s2}": true,\n'

    if finished:
        ori = ori.replace(s1, s2)
    with open(".vscode/settings.json", "w", encoding="utf8") as f:
        f.write(ori)


def path_fin(path):
    """路径是否默认为完结"""
    fin_path = {"batlantern": True}
    return fin_path.get(short_path(path), False)
