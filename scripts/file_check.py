# coding = utf-8

"""
检阅文件
自动翻译并进行字数统计

使用personal里默认的翻译方式
支持-n,-t,-b进行单次翻译方法设定
"""

import sys
import os
from utils import line_length, search_by_keyword
from name_translate import name_tsl
from web_make import to_html


def count_file(filename):
    """对文件进行字数统计"""
    if filename.endswith(".txt"):
        f = open(filename, "r", encoding="utf-8")
        print(filename + "\t" + str(line_length(f.read())))
        f.close()
    elif not filename.endswith(".md"):
        print("only support plain text and MarkDown files!")
    else:
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
                    print("\t" * last + chapter + "\t" + str(num))
                    total += num
                    num = 0
                last = i.count("#") - 1
                chapter = i.strip("#").strip()
            num += line_length(i.strip())
        print("\t" * last + chapter + "\t" + str(num))
        total += num
        if chapter != filename:
            print(filename + "\t" + str(total))


class FileChecker:
    """文件检阅器"""

    def __init__(self, key, mode, html=True):
        self.result = search_by_keyword(key)
        if self.result is not None:
            self.tsl_result(mode)
            self.count_result()
            if html:
                self.html_result()

    def tsl_result(self, mode):
        """翻译找到的文件"""
        for i in self.result:
            if mode is not None:
                name_tsl(i, mode)

    def count_result(self):
        """对找到的文件进行字数统计"""
        for i in self.result:
            count_file(i)

    def html_result(self):
        """生成文件的网页"""
        for i in self.result:
            to_html(i[0], i[1])


if __name__ == "__main__":
    from personal import DEFAULT_TRANSLATE, TRANSLATE_MODE, BACKWARD_MODE

    MODE = DEFAULT_TRANSLATE
    if len(sys.argv) > 2:
        if "-n" in sys.argv[2:]:
            MODE = None
        elif "-t" in sys.argv[2:]:
            MODE = TRANSLATE_MODE
        elif "-b" in sys.argv[2:]:
            MODE = BACKWARD_MODE
    fc = FileChecker(sys.argv[1], MODE, not "-h" in sys.argv)
