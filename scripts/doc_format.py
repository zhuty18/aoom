# coding=utf-8

"""将doc文件变为markdown"""

import os
import platform
import argparse
import sys


try:
    from win32com import client as wc
except ImportError:
    print("This script is only runnable on Windows OS.")
    print("Your are on " + platform.system() + " OS!")

try:
    import docx
except ModuleNotFoundError:
    print("Requirements not found!")
    sys.exit()


def to_markdown(path, name, rm):
    """变为markdown"""
    if name.startswith("~"):
        pass
    elif name.endswith(".docx"):
        print(name)
        file = docx.Document(path)
        outfile = open(path.replace(".docx", ".md"), "w", encoding="utf-8")
        outfile.write("# ")
        for p in file.paragraphs:
            outfile.write(p.text + "\n\n")
        outfile.close()
    elif name.endswith(".doc"):
        word = wc.Dispatch("Word.Application")
        doc = word.Documents.Open(path)  # 目标路径下的文件
        doc.SaveAs(path + "x", 12, False, "", True, "", False, False, False, False)  # 转化后路径下的文件
        doc.Close()
        word.Quit()
        to_markdown(path + "x", name + "x", rm)
    elif name.endswith(".txt"):
        print(name)
        fi = open(path, "r", encoding="utf-8")
        fo = open(path.replace(".txt", ".md"), "w", encoding="utf-8")
        for i in fi.readlines():
            fo.write(i + "\n")
        fi.close()
        fo.close()
    if rm:
        os.remove(path)


def get_all_files(path, rm):
    """获得所有文件"""
    l = os.listdir(path)
    l.sort()
    for i in l:
        subdir = os.path.join(path, i)
        if os.path.isdir(subdir) and not ".git" in subdir:
            get_all_files(subdir, rm)
        else:
            to_markdown(subdir, i, rm)


parser = argparse.ArgumentParser()
parser.add_argument("-r", "--remove", type=bool, default=False, nargs="?", const=True)
args = parser.parse_args()
get_all_files(os.getcwd(), args.remove)
