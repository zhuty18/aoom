# coding = utf-8

"""功能函数"""

import os
import re
import time

from name_def import names
from personal import (
    COMMIT_TIME,
    CP_TAGS,
    DIR_NAMES,
    FILE_ROOT,
    FIN_HEAD,
    FIN_MARKS,
    FIN_TAG,
    FIN_TAIL,
    FIN_TEM,
    FINISH_TAGS,
    HISTORY_PATH,
    IGNORE_FILES,
    IGNORE_PATH,
    INDEX_FULL_NAME,
    INDEX_NAME,
    ORGANIZATION_TAGS,
    PERSON_TAGS,
    PREVIEW_LENGTH,
    PRIORITIZED_TAGS,
    TIME_FORMAT,
    WEB_NAME,
)


def format_time(
    time_stamp: float = COMMIT_TIME, time_format=TIME_FORMAT
) -> str:
    """格式化某个时间戳，默认为当下"""
    if not time_stamp:
        time_stamp = COMMIT_TIME
    t = time.localtime(time_stamp)
    res = time.strftime(time_format, t)
    return res


def format_log_time(time_str: str) -> str:
    """格式化从git log中读取的时间"""
    time_stc = time.strptime(time_str, "%a %b %d %H:%M:%S %Y")
    local_time = time.localtime(time.mktime(time_stc))
    return format_time(time.mktime(local_time))


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
    if FIN_TAG in get_pre_key(get_predefine(filename), "tags"):
        return True
    with open(filename, "r", encoding="utf8") as f:
        text = f.read()
        ends = FIN_MARKS
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

    def __init__(self, key: str, name_match=False):
        self.key = key
        self.res = []
        self.name_match = name_match
        self.check_dir(doc_dir())
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
            else:
                if self.name_match:
                    if (
                        i.endswith(".md")
                        and name_of(i) == self.key
                        and not ignore_in_format(i)
                    ):
                        self.res.append(i)
                else:
                    if match_keys([self.key], i) and i.endswith(".md"):
                        self.res.append(i)

    def result(self):
        """搜索结果"""
        return self.res


def search_by_keyword(key):
    """搜索含有关键词的文件"""
    return SearchForFile(key).result()


def search_by_name(name):
    """根据文件名搜索文件"""
    return SearchForFile(name, True).result()[0]


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
    fin_path = {"batlantern": True, "blob": True, "logs": True}
    return fin_path.get(doc_path(path), False)


def excerpt(filename):
    """获取文件预览"""
    with open(filename, "r", encoding="utf8") as f:
        yaml = False
        pre = ""
        for i in f.readlines():
            if i == "---\n":
                yaml = not yaml
                continue
            if yaml:
                continue
            if i.startswith("#"):
                pre += "<br>\n"
                continue
            pre += i
            if "<br>\n\n" in pre:
                pre = pre.split("<br>")[1].strip()
            if len(pre) > PREVIEW_LENGTH * 0.7:
                pre = pre.strip()
                break
    if len(pre) > PREVIEW_LENGTH * 1.2:
        pre = pre[:PREVIEW_LENGTH] + "……"
    if pre.count("*") % 2 == 1:
        pre += "*"
    return pre


def get_predefine(filename):
    """读取预定义内容"""
    with open(filename, "r", encoding="utf8") as f:
        content = f.read()
        if content.startswith("---"):
            try:
                pre_d_str = re.findall(
                    re.compile(r"---\n(.*)\n---\n", re.S), content
                )[0]
            except IndexError:
                pre_d_str = re.findall(
                    re.compile(r"---\n(.*)\n---$", re.S), content
                )[0]
            pre_d = {}
            current = ""
            for i in pre_d_str.split("\n"):
                if ":" in i:
                    i = i.split(":")
                    key = i[0].strip()
                    current = key
                    value = i[1].strip()
                    if key == "tags" and " " in value:
                        value = value.split(" ")
                    elif key == "tags" and value != "":
                        value = [value]
                    elif key == "tags":
                        value = []
                    elif value == "":
                        value = []
                    pre_d[key] = value
                elif "  - " in i:
                    pre_d[current].append(i.strip(" -"))
            return pre_d
    return None


def tag_priority(tag):
    """标签显示优先级"""
    # 优先级：特殊 -> CP -> AU -> 角色 -> 组织 -> 其他 -> 完成度
    if tag in PRIORITIZED_TAGS:
        return -1
    if tag in CP_TAGS:
        return 0
    elif "au" in tag or "ABO" in tag:
        return 1
    elif tag in PERSON_TAGS:
        return 2
    elif tag in ORGANIZATION_TAGS:
        return 3
    elif tag in FINISH_TAGS:
        return 5
    else:
        return 4


def write_predefine(pre_d, filename):
    """预定义头信息写入文件"""
    res = ""
    if "tags" in pre_d:
        pre_d["tags"] = sorted(pre_d["tags"], key=tag_priority)
    tmp = sorted(pre_d.items())
    for k, v in tmp:
        if isinstance(v, list):
            res += f"{k}:\n  - {"\n  - ".join(v)}\n"
        else:
            res += f"{k}: {v}\n"
    res = res.strip()

    with open(filename, "r", encoding="utf8") as f:
        content = f.read()
    try:
        pre_d_str = re.findall(re.compile(r"---\n(.*)\n---\n", re.S), content)[
            0
        ]
        with open(filename, "w", encoding="utf8") as f:
            f.write(content.replace(pre_d_str, res))
    except IndexError:
        with open(filename, "w", encoding="utf8") as f:
            f.write(f"---\n{res}\n---\n\n{content}")


def sort_predef(filename):
    """整理预定义头"""
    pre_d = get_predefine(filename)
    if pre_d:
        write_predefine(pre_d, filename)


def get_pre_key(pre_d, keyword):
    """从预定义头中读取关键字参数"""
    if keyword == "tags":
        return pre_d.get(keyword, [])
    return pre_d.get(keyword)


def add_predef(filename, key, value, no_multi=False, change=False):
    """添加预定义"""
    pre_d = get_predefine(filename)
    if not pre_d:
        # 无预定义头
        with open(filename, "r", encoding="utf8") as f:
            content = f.read()
        with open(filename, "w", encoding="utf8") as f:
            f.write(
                f"""---
{key}: {value}
---

"""
            )
            f.write(content)
            return 1
    tmp = get_pre_key(pre_d, key)
    if not tmp:
        # 预定义头内无key
        pre_d[key] = value
    elif value in tmp:
        # key已有值value
        return 0
    elif no_multi and len(tmp) > 0:
        # key已有值且不许补充
        return 0
    elif change:
        # key已有值且可替换，即auto_date
        pre_d[key] = value
    elif not no_multi:
        # key已有值且可补充，即tags
        pre_d[key].append(value)
    write_predefine(pre_d, filename)
    return 1


def mark_category(filename):
    """在预定义中增加类"""
    add_predef(filename, "category", dir_name(path_of(filename)))


def mark_fin(filename):
    """标注已完成作品"""
    if file_fin(filename):
        add_predef(filename, "tags", FIN_TAG)


def mark_post(filename):
    """将预定义post标注为true"""
    return add_predef(filename, "post", "true", True)


def make_index(kind, name):
    """制作jekyll索引"""
    path = os.path.join(os.getcwd(), kind)
    if not os.path.exists(os.path.join(path, name + ".md")):
        with open(os.path.join(path, name + ".md"), "w", encoding="utf8") as f:
            f.write("---\n")
            f.write(f"layout: {kind}\n")
            f.write(f"title: {name}\n")
            f.write("---\n")


def make_index_dir(kind, name):
    """制作jekyll索引路径"""
    path = os.path.join(os.getcwd(), kind)
    if not os.path.exists(path):
        os.mkdir(path)
        with open(os.path.join(path, INDEX_NAME), "w", encoding="utf8") as f:
            f.write("---\n")
            f.write(f"layout: {kind}_all\n")
            f.write(f"title: 全部{name}\n")
            f.write("---\n")


def title_of(filename):
    """获得文件标题"""
    if get_pre_key(get_predefine(filename), "title"):
        return get_pre_key(get_predefine(filename), "title")
    title = name_of(filename)
    with open(filename, "r", encoding="utf8") as f:
        content = f.read()
        for i in content.split("\n\n"):
            if i.startswith("# "):
                title = i.replace("# ", "")
                break
    return title.strip()


def ignore_in_format(filename):
    """格式化中忽略此索引文件"""
    for i in IGNORE_FILES:
        if i in filename:
            return True
    for i in IGNORE_PATH:
        if i in short_path(filename):
            return True
    return "_" in filename
