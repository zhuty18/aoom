# coding = utf-8

"""
检阅文件
自动翻译并进行字数统计

使用personal里默认的翻译方式
支持-n,-t,-b进行单次翻译方法设定
"""

import sys

from name_translate import name_tsl
from utils import 获取文件_关键字, 行长度


def count_file(filename, p=True):
    """对文件进行字数统计"""
    if filename.endswith(".txt"):
        f = open(filename, "r", encoding="utf-8")
        if p:
            print(filename + "\t" + str(行长度(f.read())))
        f.close()
    elif not filename.endswith(".md") and p:
        print("only support plain text and MarkDown files!")
    elif not "_templates" in filename:
        f = open(filename, "r", encoding="utf-8")
        filename = filename.replace("\\", "/")
        filename = filename.split("/")
        filename = filename[-1]
        filename = filename.replace(".md", "")
        chapter = ""
        total = 0
        num = 0
        last = 0
        for i in f.readlines():
            if i.startswith("#"):
                if chapter != "":
                    if p:
                        print("\t" * last + chapter + "\t" + str(num))
                    total += num
                    num = 0
                last = i.count("#") - 1
                chapter = i.strip("#").strip()
            num += 行长度(i.strip())
        if p:
            print("\t" * last + chapter + "\t" + str(num))
        total += num
        if chapter != filename and p:
            print(filename + "\t" + str(total))


class FileChecker:
    """文件检阅器"""

    def __init__(self, key, mode, html=True):
        self.result = 获取文件_关键字(key)
        if self.result is not None:
            self.tsl_result(mode)
            self.count_result()

    def tsl_result(self, mode):
        """翻译找到的文件"""
        for i in self.result:
            if mode is not None:
                name_tsl(i, mode)

    def count_result(self):
        """对找到的文件进行字数统计"""
        for i in self.result:
            count_file(i)


if __name__ == "__main__":
    from personal import 反向翻译, 翻译模式, 翻译行为

    MODE = 翻译行为
    if len(sys.argv) > 2:
        if "-n" in sys.argv[2:]:
            MODE = None
        elif "-t" in sys.argv[2:]:
            MODE = 翻译模式
        elif "-b" in sys.argv[2:]:
            MODE = 反向翻译
    fc = FileChecker(sys.argv[1], MODE, not "-h" in sys.argv)
