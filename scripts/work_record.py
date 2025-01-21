# coding = utf-8

"""文件记录"""

import os
import re
import subprocess
import sys

import file_check
import web_make
from personal import (
    ARCHIVE_TITLE,
    ARCHIVE_UPDATE,
    DEFAULT_ORDER,
    FILE_ROOT,
    FIN_TITLE,
    GENERATE_WEB,
    HISTORY_PATH,
    INDEX_FULL_NAME,
    INDEX_NAME,
    POST_PATH,
    TBC_TITLE,
)
from utils import (
    auto_hide,
    dir_name,
    dirs,
    doc_dir,
    doc_path,
    file_fin,
    file_length,
    format_log_time,
    format_time,
    get_time,
    path_of,
    short_path,
    title_of,
)

try:
    from xpinyin import Pinyin
except ModuleNotFoundError:
    if "win" in sys.platform:
        print("请安装xpinyin模块！")
        sys.exit()


class FileRecord:
    """文件记录"""

    def __init__(self, name, length, time, fin):
        self.name = name
        self.length = length
        self.time = time
        self.fin = fin

    def update(self, length=None, fin=None):
        """更新文件信息"""
        self.length = length
        self.fin = fin
        self.time = format_time()

    def __str__(self) -> str:
        return f"{self.name}\t{self.length}\t{self.time}\t{self.fin}"

    def info(self):
        """信息条目"""
        link = self.name.replace(" ", "%20")
        return f"|[{self.name}]({link}.md)|{self.length}|{self.time}|"

    def merge(self, other):
        """数据融合"""
        if self.length == other.length and self.fin == other.fin:
            self.time = (
                self.time
                if get_time(self.time) < get_time(other.time)
                else other.time
            )
        elif get_time(self.time) < get_time(other.time):
            self.length = other.length
            self.time = other.time
            self.fin = other.fin

    @staticmethod
    def from_record(record: str):
        """从历史记录中的信息条目读取"""
        t = record.strip().split("\t")
        return FileRecord(t[0], int(t[1]), t[2], t[3] == "True")

    @staticmethod
    def from_path(name, path):
        """根据路径生成"""
        full_path = os.path.join(path, name)
        pipe = subprocess.Popen(
            ["git", "log", full_path], stdout=subprocess.PIPE
        )
        output, _ = pipe.communicate()
        output = output.decode("utf8")
        commit = None
        for i in output.split("\n"):
            if i.startswith("Date:"):
                commit = i
                break
        if commit is not None:
            t = re.findall(re.compile(r"Date:\s*(.*?)\s*\+", re.S), commit)[
                0
            ].strip()
            time_formatted = format_log_time(t)
        else:
            time_formatted = format_time()
        return FileRecord(
            name[0:-3],
            file_length(full_path),
            time_formatted,
            file_fin(full_path),
        )


class WordCounter:
    """字数统计器"""

    def __init__(self):
        self.total_change = 0
        self.history = {}
        self.changes = []

    def run(self):
        """工作函数"""
        self.read_history()
        self.get_files()
        self.update_result()
        #TODO: 注入时间戳
        # self.

    def read_history(self):
        """从历史记录中读取已有条目"""
        if os.path.exists(HISTORY_PATH):
            with open(HISTORY_PATH, "r", encoding="utf-8") as f:
                for i in f.readlines():
                    t = FileRecord.from_record(i)
                    self.history[t.name] = t

    def get_files(self):
        """读取变更的文件目录"""
        os.environ["PYTHONIOENCODING"] = "utf8"
        os.system("git add .")
        with subprocess.Popen(
            ["git", "status", "-s"], stdout=subprocess.PIPE
        ) as pipe:
            output = pipe.communicate()[0]
        output = output.decode("utf8")
        for i in output.split("\n"):
            if "->" in i:
                i = i.split("->")[-1].strip()
            if i:
                i = i.split("  ")[-1]
                i = i.strip('"')
            if (
                INDEX_NAME not in i
                and INDEX_FULL_NAME not in i
                and i.endswith(".md")
                and FILE_ROOT in i
                and POST_PATH not in i
            ):
                if os.path.exists(i) and dir_name(path_of(i)):
                    self.changes.append(i)

    def update_result(self):
        """统计结果写入数据库"""
        log = []
        info = []
        for i in self.changes:
            name = re.findall(re.compile(r".*/(.*).md$", re.S), i)[0]
            try:
                length_new = file_length(i)
                try:
                    length_old = self.history[name].length
                except KeyError:
                    length_old = 0
                if length_new == length_old:
                    continue
                else:
                    file_check.count_file(i)
                link = doc_path(os.path.join(os.getcwd(), i)).replace(
                    " ", "%20"
                )
                info.append(title_of(i))
                log.append(
                    f"|[{title_of(i)}]({link})|{length_old}|{length_new}|{length_new-length_old}|"
                )
                self.total_change += length_new - length_old
                try:
                    self.history[name].update(
                        length=length_new, fin=file_fin(i)
                    )
                except KeyError:
                    self.history[name] = FileRecord(
                        name, length_new, format_time(), file_fin(i)
                    )
            except FileNotFoundError:
                self.history.pop(name)
                self.total_change -= self.history[name].length

        log_str = ARCHIVE_TITLE
        update_str = ""
        if info:
            update_str = "\n  - ".join(info)
            update_str = f"\n  - {update_str}"
        update_str += "\nchange:"
        if self.changes:
            update_str += f"\n  - {"\n  - ".join(self.changes)}"
        log_str = log_str.replace(ARCHIVE_UPDATE, update_str)
        with open(
            os.path.join(doc_dir(), INDEX_NAME), "w", encoding="utf-8"
        ) as f:
            if log:
                log_str += "## 最近一次更新的内容\n\n"
                log_str += "|文件名|上次提交时字数|本次提交字数|字数变化|\n"
                log_str += "|:-|:-|:-|:-|\n"
                log_str += "\n".join(log)
                log_str += "\n"
                # log_str += "\n"
            # log_str += "#" + dirs().strip()
            f.write(log_str)

    def update_history(self):
        """更新历史数据"""
        with open(HISTORY_PATH, "w", encoding="utf-8") as f:
            for key in sorted(self.history):
                f.write(f"{self.history[key]}\n")

    def save_change(self, path):
        """存储改变文档至临时目录"""
        with open(path, "w", encoding="utf8") as f:
            f.write("\n".join(self.changes))


class IndexBuilder:
    """索引目录建立器"""

    def __init__(self, path, counter: WordCounter, order):
        self.tbc = []
        self.fin = []
        self.build_index(path, counter)
        self.sort_index(self.tbc, order)
        self.sort_index(self.fin, order)
        self.write_index(path)

    def get_info(self, info):
        """获得记录"""
        t = info.split("|")
        name = re.findall(re.compile(r"\[(.*?)\]", re.S), t[1])[0]
        return name, t[3]

    def build_index(self, path, counter: WordCounter):
        """建立索引"""
        for i in os.listdir(path):
            if (
                i.endswith(".md")
                and not i.startswith(INDEX_FULL_NAME)
                and not i.startswith(INDEX_NAME)
            ):
                if not i[0:-3] in counter.history.keys():
                    counter.history[i[0:-3]] = FileRecord.from_path(i, path)
                t = counter.history[i[0:-3]]
                if t.fin:
                    self.fin.append(t)
                else:
                    self.tbc.append(t)

    def sort_index(self, l: list, order):
        """索引排序"""
        if "win" in sys.platform:
            pin = Pinyin()
            l.sort(key=lambda x: pin.get_pinyin(x.name))
        if order == "time":
            l.sort(key=lambda x: get_time(x.time), reverse=True)

    def gen_content(self, l, t):
        """生成列表内容"""
        if l:
            title = "|名称|字数|修改时间|\n"
            title += "|:-|:-|:-|\n"
            content = f"{t}\n\n"
            content += title
            for i in l:
                content += i.info() + "\n"
            return content
        else:
            return ""

    def write_index(self, path):
        """写入索引"""
        if len(self.tbc) + len(self.fin) > 0:
            head = f"# {dir_name(path)}\n\n"
            with open(f"{path}/{INDEX_NAME}", "w", encoding="utf-8") as fi:
                with open(
                    f"{path}/{INDEX_FULL_NAME}", "w", encoding="utf-8"
                ) as fr:
                    fi.write(head)
                    fr.write(head)
                    if self.tbc:
                        fr.write(self.gen_content(self.tbc, TBC_TITLE) + "\n")
                    fi.write(self.gen_content(self.fin, FIN_TITLE))
                    fr.write(self.gen_content(self.fin, FIN_TITLE))
        else:
            with open(f"{path}/{INDEX_NAME}", "w", encoding="utf-8") as fi:
                fi.write(dirs(path).strip() + "\n")


def update_index(counter, path, order, force=False):
    """更新索引"""
    for i in os.listdir(path):
        subdir = os.path.join(path, i)
        if os.path.isdir(subdir) and not i.startswith("."):
            change = False
            for j in counter.changes:
                if short_path(subdir) in j:
                    change = True
                    break
            if change or force:
                update_index(counter, subdir, order, force)
    if path != doc_dir() and dir_name(path):
        IndexBuilder(path, counter, order)


if __name__ == "__main__":
    wcr = WordCounter()
    wcr.run()
    update_index(wcr, doc_dir(), DEFAULT_ORDER, True)
    wcr.update_history()
    if GENERATE_WEB:
        web_make.all_html(force=True)
    auto_hide()
