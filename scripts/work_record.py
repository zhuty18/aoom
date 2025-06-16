# coding = utf-8

"""文件记录"""

import os
import re
import subprocess
import sys
import time

from file_status import 文件管理
from personal import (
    AI评论路径,
    INDEX文件,
    INDEX文件_完整,
    POST路径,
    文档库YAML,
    历史文件,
    文档库更新字符串,
    日志路径,
    标题_已完结,
    标题_未完结,
    默认顺序,
)
from utils import 文件夹路径, 文档根目录, 目录信息, 相对路径, 路径名, 隐藏已完结

try:
    from xpinyin import Pinyin
except ModuleNotFoundError:
    if "win" in sys.platform:
        print("请安装xpinyin模块！")
        sys.exit()


class 字数统计器:
    """字数统计器"""

    def __init__(self):
        self.总字数变更 = 0
        self.文件表: dict[str, 文件管理] = {}
        self.变更文件: list[文件管理] = []

    def 运行(self):
        """工作函数"""
        self.读取历史()
        self.读取变更文件()
        self.清理删除文件()
        self.更新统计结果()
        # self.标注更新日期()

    def 读取历史(self):
        """从历史记录中读取已有条目"""
        if os.path.exists(历史文件):
            with open(历史文件, "r", encoding="utf-8") as f:
                for i in f.readlines():
                    文件 = 文件管理.从历史条目(i)
                    self.文件表[文件.文件名()] = 文件

    def 读取变更文件(self):
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
            if 文件管理(i, None).合法():
                if os.path.exists(i) and 路径名(文件夹路径(i)):
                    self.变更文件.append(文件管理.从路径(i))

    def 清理删除文件(self):
        """清除历史记录中消失了的文件"""
        tmp = {}
        for v in self.文件表.values():
            if v.存在():
                tmp[v.文件名()] = v
        self.文件表 = tmp

    def 更新统计结果(self):
        """统计结果写入数据库"""
        总更新内容 = []
        文档库更新 = []
        for i in self.变更文件:
            if i.存在():
                旧字数 = (
                    self.文件表[i.文件名()].历史字数
                    if i.文件名() in self.文件表
                    else 0
                )
                if i.字数() == 旧字数:
                    continue
                else:
                    i.标注更新日期()
                    print(f"{i.文件名()}\t{旧字数} -> {i.字数()}")
                文档库更新.append(i.标题())
                总更新内容.append(
                    f"|[{i.标题()}]({i.链接()})|{旧字数}|{i.字数()}|{i.字数()-旧字数}|"
                )
                self.总字数变更 += i.字数() - 旧字数
                if i.文件名() not in self.文件表:
                    self.文件表[i.文件名()] = i
            else:
                self.文件表.pop(i.文件名())

        文档库字符串 = 文档库YAML
        更新字符串 = ""
        if 文档库更新:
            更新字符串 = "\n  - ".join(文档库更新)
            更新字符串 = f"\n  - {更新字符串}"
        更新字符串 += "\nchange:"
        if self.变更文件:
            更新字符串 += (
                f"\n  - {"\n  - ".join([x.路径()for x in self.变更文件])}"
            )
        文档库字符串 = 文档库字符串.replace(文档库更新字符串, 更新字符串)
        with open(
            os.path.join(文档根目录(), INDEX文件), "w", encoding="utf-8"
        ) as f:
            if 总更新内容:
                文档库字符串 += "## 最近一次更新的内容\n\n"
                文档库字符串 += (
                    "|文件名|上次提交时字数|本次提交字数|字数变化|\n"
                )
                文档库字符串 += "|:-|:-|:-|:-|\n"
                文档库字符串 += "\n".join(总更新内容)
                文档库字符串 += "\n"
                # log_str += "\n"
            # log_str += "#" + dirs().strip()
            f.write(文档库字符串)

    def 更新历史(self):
        """更新历史数据"""
        with open(历史文件, "w", encoding="utf-8") as f:
            for key in sorted(self.文件表.keys()):
                f.write(f"{self.文件表[key].历史信息条目()}\n")

    def 暂存更改(self, path):
        """存储改变文档至临时目录"""
        with open(path, "w", encoding="utf8") as f:
            f.write("\n".join([x.路径() for x in self.变更文件]))

    def 标注更新日期(self):
        """为文件标注更新日期"""
        for value in self.文件表.values():
            value.标注更新日期()


class 索引构建器:
    """索引目录建立器"""

    def __init__(self, path, 统计器: 字数统计器, order):
        self.未完成: list[文件管理] = []
        self.已完成: list[文件管理] = []
        self.建立索引(path, 统计器)
        self.索引排序(self.未完成, order)
        self.索引排序(self.已完成, order)
        self.写入索引(path)

    def get_info(self, info):
        """获得记录"""
        t = info.split("|")
        name = re.findall(re.compile(r"\[(.*?)\]", re.S), t[1])[0]
        return name, t[3]

    def 建立索引(self, path, 统计器: 字数统计器):
        """建立索引"""
        for i in os.listdir(path):
            文件路径 = os.path.join(path, i)
            文件 = 文件管理(文件路径)
            if 文件.合法():
                if 文件.文件名() not in 统计器.文件表.keys():
                    文件 = 文件管理.从路径(文件路径)
                    统计器.文件表[文件.文件名()] = 文件
                else:
                    文件 = 统计器.文件表[文件.文件名()]
                if 文件.已完结():
                    self.已完成.append(文件)
                else:
                    self.未完成.append(文件)

    def 索引排序(self, l: list[文件管理], order):
        """索引排序"""
        if "win" in sys.platform:
            pin = Pinyin()
            l.sort(key=lambda x: pin.get_pinyin(x.文件名()))
        if order == "time":
            l.sort(key=lambda x: x.更新时间(), reverse=True)

    def 列表内容(self, l, t):
        """生成列表内容"""
        if l:
            title = "|名称|字数|修改时间|\n"
            title += "|:-|:-|:-|\n"
            content = f"{t}\n\n"
            content += title
            for i in l:
                content += i.md信息条目() + "\n"
            return content
        else:
            return ""

    def 写入索引(self, path):
        """写入索引"""
        if len(self.未完成) + len(self.已完成) > 0:
            head = f"# {路径名(path)}\n\n"
            full_index = head
            index = head
            if self.未完成:
                full_index += self.列表内容(self.未完成, 标题_未完结) + "\n"
            index += self.列表内容(self.已完成, 标题_已完结) + "\n"
            full_index += self.列表内容(self.已完成, 标题_已完结) + "\n"
            with open(f"{path}/{INDEX文件}", "w", encoding="utf-8") as fi:
                fi.write(index.strip("\n") + "\n")
            with open(f"{path}/{INDEX文件_完整}", "w", encoding="utf-8") as fr:
                fr.write(full_index.strip("\n") + "\n")
        else:
            with open(f"{path}/{INDEX文件}", "w", encoding="utf-8") as fi:
                fi.write(目录信息(path).strip() + "\n")


def 更新索引(统计器: 字数统计器, 索引路径, 顺序, 强制=False):
    """更新索引"""
    索引路径 = 相对路径(索引路径)
    for i in os.listdir(索引路径):
        子目录 = os.path.join(索引路径, i)
        if os.path.isdir(子目录) and not i.startswith("."):
            有内容变更 = False
            for j in 统计器.变更文件:
                if 相对路径(子目录) in j.路径():
                    有内容变更 = True
                    break
            if 有内容变更 or 强制:
                更新索引(统计器, 子目录, 顺序, 强制)
    if (
        索引路径 != 相对路径(文档根目录())
        and 路径名(索引路径)
        and 日志路径 not in 索引路径
        and AI评论路径 not in 索引路径
        and POST路径 not in 索引路径
    ):
        索引构建器(索引路径, 统计器, 顺序)


def 进行字数统计(路径=文档根目录(), 顺序=默认顺序, 强制=False):
    """进行字数统计"""
    字数统计 = 字数统计器()
    字数统计.运行()
    更新索引(字数统计, 路径, 顺序, 强制)
    字数统计.更新历史()
    隐藏已完结()
    return 字数统计


if __name__ == "__main__":
    t = time.time()
    进行字数统计(强制=True)
    print(time.time() - t)
