# coding = utf-8

"""文件管理"""

import os
import re
import shutil
import subprocess
import time

from personal import (
    AI_PATH,
    AI_TAG,
    COMMIT_TIME,
    DATE_FORMAT,
    DOC_ROOT,
    EXCERPT_LENGTH,
    FIN_MARKS,
    FIN_PATHS,
    POST_PATH,
    TIME_FORMAT,
)
from utils import (
    FileBasic,
    doc_path,
    filename_is_key,
    folder_path,
    format_time,
    get_log_time,
    get_time,
    line_length,
    mk_dirs,
    root_path,
    tag_order,
)


class FileStatus(FileBasic):
    """文件状态"""

    def __init__(self, path, update_time=None):
        super().__init__(path)
        self._time_ = update_time if update_time else COMMIT_TIME
        self._yaml_ = None

    def yaml_str(self):
        """读取yaml字符串"""
        with open(self._path_, "r", encoding="utf8") as f:
            content = f.read()
        if content.startswith("---"):
            return content[0 : content.index("---", 3)].strip("-\n")
        return None

    def yaml(self):
        """读取yaml内容"""
        if self._yaml_ is None:
            yaml字符串 = self.yaml_str()
            if not yaml字符串:
                return {}
            yaml内容 = {}
            current = ""
            for i in yaml字符串.split("\n"):
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
                    yaml内容[key] = value
                elif "  - " in i:
                    yaml内容[current].append(i.strip(" -"))
            if "tags" in yaml内容 and "FIN" in yaml内容["tags"]:
                yaml内容["tags"].remove("FIN")
            self._yaml_ = yaml内容
        return self._yaml_

    def __update_yaml__(self):
        """更新yaml区域"""
        res = ""
        if "tags" in self.yaml():
            self.yaml()["tags"] = sorted(self.yaml()["tags"], key=tag_order)
        for k, v in sorted(self.yaml().items()):
            if isinstance(v, list):
                res += f"{k}:\n  - {"\n  - ".join(v)}\n"
            else:
                res += f"{k}: {v}\n"
        res = res.strip()

        yaml字符串 = self.yaml_str()
        with open(self._path_, "r", encoding="utf8") as f:
            content = f.read()
        if yaml字符串:
            with open(self._path_, "w", encoding="utf8") as f:
                f.write(content.replace(yaml字符串, res))
        else:
            with open(self._path_, "w", encoding="utf8") as f:
                f.write(f"---\n{res}\n---\n\n{content}")

    def sort_yaml(self):
        """整理yaml区域"""
        if self.yaml():
            self.__update_yaml__()

    def get_yaml(self, key):
        """读取yaml内参数"""
        if key == "tags":
            return self.yaml().get(key, [])
        return self.yaml().get(key)

    def add_yaml(self, key, value, change=False):
        """添加yaml参数"""
        if key in self.yaml() and not change:
            return 0
        self.yaml()[key] = value
        self.__update_yaml__()
        return 1

    # def copy_yaml(self, yaml):
    #     """复制yaml"""
    #     self._yaml = yaml
    #     self.__update_yaml__()


class FileCount(FileStatus):
    """统计文件"""

    def __init__(self, path, update_time=None, length=0, is_fin=False):
        super().__init__(path, update_time)
        self.his_length = length
        self.his_fin = is_fin

        self._title_ = None
        self._fin_ = None
        self._length_ = None

    @staticmethod
    def from_history(history):
        """从历史条目中获取信息"""
        item = history.strip().split("\t")
        return FileCount(
            filename_is_key(item[0]),
            get_time(item[2]),
            int(item[1]),
            item[3] == "True",
        )

    @staticmethod
    def from_path(path):
        """从路径中获取信息"""
        pipe = subprocess.Popen(["git", "log", path], stdout=subprocess.PIPE)
        output, _ = pipe.communicate()
        output = output.decode("utf8")
        commit = None
        for i in output.split("\n"):
            if i.startswith("Date: "):
                commit = i
                break
        if commit is not None:
            t = re.findall(re.compile(r"Date:\s*(.*?)\s*\+", re.S), commit)[
                0
            ].strip()
            timing = get_log_time(t)
        else:
            timing = None
        return FileCount(path, timing)

    def title(self):
        """文件标题"""
        if self._title_ is None:
            if "title" in self.yaml():
                return self.yaml()["title"]
            res = self.filename()
            with open(self._path_, "r", encoding="utf8") as f:
                content = f.read()
                for i in content.split("\n\n"):
                    if i.startswith("# "):
                        res = i[2:].strip()
                        break
            self._title_ = res.strip("*")
        return self._title_

    def format(self, print_process=False):
        """格式化文件"""
        with open(self._path_, "r", encoding="utf-8") as f:
            content = f.read()
        res = []
        for a in [x if x else "<br>" for x in content.split("\n\n")]:
            if not (a == "<br>" and res[-1] == "<br>"):
                res.append(a)
        res = "\n\n".join(res)
        res.replace("------", "---")
        with open(self._path_, "w", encoding="utf-8") as f:
            f.write(res.strip("\n") + "\n")
        self.add_yaml(
            "word_count", str(self.length(print_process)), change=True
        )
        self.__mark_fin__()

    def legal(self):
        """是否为合法文档"""
        return (
            self._path_.endswith(".md")
            and DOC_ROOT in self._path_
            and (not self.is_ignore())
            and (not POST_PATH in self._path_)
        )

    def is_fin(self):
        """是否完结"""
        if self._fin_ is None:
            # print(self._路径,完结路径(文件夹路径(self._路径)))
            if doc_path(folder_path(self._path_)) in FIN_PATHS:
                self._fin_ = True
            elif self.get_yaml("finished") == "true":
                self._fin_ = True
            else:
                with open(self._path_, "r", encoding="utf8") as f:
                    text = f.read()
                    ends = FIN_MARKS
                    for i in ends:
                        if f"{i}\n" in text:
                            self._fin_ = True
            if self._fin_ is None:
                self._fin_ = False
        return self._fin_

    def length(self, 打印过程=False):
        """文件长度"""
        if self._length_ is None:
            res = 0
            with open(self._path_, "r", encoding="utf8") as f:
                content = f.read().replace(self.yaml_str(), "").strip("-\n")
            heading = ""
            count = 0
            level = 0
            for i in content.split("\n"):
                if i.startswith("#"):
                    if heading:
                        if 打印过程:
                            print("\t" * level + heading + "\t" + str(count))
                        res += count
                        count = 0
                    heading = i.strip("#").strip()
                    level = i.count("#") - 1
                count += line_length(i.strip())
            if 打印过程:
                print("\t" * level + heading + "\t" + str(count))
            res += count
            if heading != self.title() and 打印过程:
                print(self.title() + "\t" + str(res))
            self._length_ = res
        return self._length_

    def __update_time__(self):
        """文件更新时间"""
        return format_time(self._time_)

    def __mark_fin__(self, force=False):
        """标记完成"""
        if self.is_fin():
            self.add_yaml("finished", "true", change=True)
        elif force:
            self.add_yaml("finished", "false")

    def mark_auto_date(self):
        """为文件标注更新日期"""
        self._time_ = COMMIT_TIME
        self.add_yaml(
            "auto_date", format_time(self._time_, DATE_FORMAT), change=True
        )

    def history_entry(self):
        """历史信息条目"""
        return f"{self.filename()}\t{self.length()}\t{self.__update_time__()}\t{self.is_fin()}"

    # def link(self):
    #     """文件链接"""
    #     return root_path(self._path_, DOC_ROOT).replace(" ", "%20")

    # def md信息条目(self):
    #     """Markdown信息条目"""
    #     return f"|[{self.title()}]({self.filename().replace(" ", "%20")}.md)|{self.length()}|{self.__update_time__()}|"


class FilePost(FileCount):
    """发布文件"""

    def is_post(self):
        """是否应发布"""
        return self._path_.endswith(".md") and (
            not self.is_ignore() or self.__ai_write__()
        )

    def __excerpt__(self):
        """文件预览"""
        with open(self._path_, "r", encoding="utf8") as f:
            yaml = False
            pre = ""
            exp = re.compile(r".*?(\[\^\d+\]).*?", re.S)
            for i in f.readlines():
                if i == "---\n":
                    yaml = not yaml
                    continue
                if yaml:
                    continue
                if i.startswith("#"):
                    pre += "<br>\n"
                    continue
                tmp = re.findall(exp, i)
                if tmp:
                    for j in tmp:
                        i = i.replace(j, "")
                pre += i
                if "<br>\n\n" in pre:
                    pre = pre.split("<br>")[1].strip()
                if len(pre) > EXCERPT_LENGTH * 0.5:
                    pre = pre.strip()
                    break
        if len(pre) > EXCERPT_LENGTH * 1.2:
            pre = pre[:EXCERPT_LENGTH] + "……"
        if pre.count("*") % 2 == 1:
            pre += "*"
        return pre

    def __ai_comment__(self):
        """获取AI评论文件"""
        if self.__ai_write__():
            return None
        ai_comment = os.path.join(POST_PATH, AI_PATH, self.filename()) + ".md"
        return ai_comment if os.path.exists(ai_comment) else None

    def __ai_write__(self):
        """是否为AI创作"""
        if self.get_yaml("tags"):
            return AI_TAG in self.get_yaml("tags")
        return False

    def online_format(self):
        """在线格式化文件"""
        if not self.get_yaml("title"):
            with open(self._path_, "r", encoding="utf8") as f:
                content = f.read()
                if f"\n# {self.title()}\n" in content:
                    new_content = content.replace(f"\n# {self.title()}\n", "")
                else:
                    new_content = content.replace(f"# {self.title()}\n\n", "")
            with open(self._path_, "w", encoding="utf8") as f:
                f.write(new_content)
            self.add_yaml("title", self.title(), change=True)

        ai_comment = self.__ai_comment__()
        if ai_comment:
            self.add_yaml("ai_comment", "true")
            FileStatus(ai_comment).add_yaml(
                "ai_source",
                doc_path(root_path(self.path(), POST_PATH)).replace(".md", ""),
            )

    def mark_post(self, log=False):
        """标记发布"""
        if self.__ai_write__():
            return 0
        return self.add_yaml("post", "false" if log else "true", change=True)

    def post(self):
        """发布文件"""
        date = self.get_yaml("date")
        if not date:
            date = self.get_yaml("auto_date")
        if not date:
            date = time.strftime("%Y-%m-%d", time.localtime(time.time()))

        post_path = os.path.join(POST_PATH, self.path())
        mk_dirs(post_path)
        shutil.copy(self.path(), post_path)

        post_file = FilePost(post_path)
        post_file.online_format()

        post_file.add_yaml(
            "excerpt",
            self.__excerpt__()
            .replace("\n", "\\n")
            .replace("> ", "")
            .replace(" ", "&nbsp;")
            .replace('"', '\\"')
            .replace("'", "\\'")
            .replace("*", ""),
        )

        return date, post_path
