# coding = utf-8

"""检索某个关键词"""

import os
import sys

from utils import ignore_in_format, 文档根目录, 相对路径, 获取文件_关键字


class KeySearcher:
    """关键词检索器"""

    def __init__(self, path, keyword):
        self.key = keyword
        self.pth = path
        self.search_dir(path)

    def search_dir(self, path):
        """检索某目录下所有文档"""
        l = os.listdir(path)
        for i in l:
            subdir = os.path.join(path, i)
            if os.path.isdir(subdir):
                self.search_dir(subdir)
            elif (
                subdir.endswith(".md")
                and "README" not in subdir
                and not ignore_in_format(subdir)
            ):
                self.search_file(subdir)

    def search_file(self, file):
        """在文件内检索"""
        with open(file, "r", encoding="utf-8") as f:
            have = False
            title = 相对路径(file)
            for i in f.readlines():
                if self.key in i:
                    if not have:
                        print(title)
                        have = True
                    print(i.strip())
            if have:
                print()


if __name__ == "__main__":
    key = sys.argv[1]
    print(获取文件_关键字(key))
    KeySearcher(文档根目录(), key)
