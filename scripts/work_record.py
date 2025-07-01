# coding = utf-8

"""文件记录"""

import os
import subprocess
import time

from file_status import 文件管理
from personal import 历史文件
from utils import 文件夹路径, 路径名, 隐藏已完结


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
        self.update_files()

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

    def update_files(self):
        """变更记录进原文件"""
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
                self.总字数变更 += i.字数() - 旧字数
                self.文件表[i.文件名()] = i
            else:
                self.文件表.pop(i.文件名())

    def 更新历史(self):
        """更新历史数据"""
        with open(历史文件, "w", encoding="utf-8") as f:
            for key in sorted(self.文件表.keys()):
                f.write(f"{self.文件表[key].历史信息条目()}\n")


def 进行字数统计():
    """进行字数统计"""
    字数统计 = 字数统计器()
    字数统计.运行()
    字数统计.更新历史()
    隐藏已完结()
    return 字数统计


if __name__ == "__main__":
    t = time.time()
    进行字数统计()
    print(time.time() - t)
