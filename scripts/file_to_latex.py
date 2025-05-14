# coding = utf-8

"""
将markdown变为latex
"""

import argparse
import os
import re

from utils import name_of, 获取文件_关键字


class LatexConverter:
    """Latex转换器"""

    def __init__(self, key, depth, path, output):
        if os.path.exists(key):
            self.convert(key, depth, path, output)
            return
        self.result = 获取文件_关键字(key)
        if self.result is not None:
            for i in self.result:
                print(name_of(i))
                self.convert(i, depth, path, output)

    def convert(self, i, depth, path, output):
        """转换单个markdown"""
        if output:
            filename = path + "/" + output + ".tex"
        else:
            filename = path + "/" + name_of(i) + ".tex"
        if not os.path.exists(path):
            os.mkdir(path)
        with open(i, "r", encoding="utf8") as f:
            tmp = f.read()
        tmp = tmp.replace("\n\n\n", "\n\nBLANKLINE\n")
        tmp = tmp.replace("\n\n<br>\n", "\n\nBLANKLINE\n")
        tmp = tmp.replace("\n\n</br>\n", "\n\nBLANKLINE\n")
        with open(filename.replace(".tex", ".md"), "w", encoding="utf8") as f:
            f.write(tmp)
        os.system(f"pandoc {filename.replace(".tex", ".md")} -o {filename}")
        os.remove(filename.replace(".tex", ".md"))

        with open(filename, "r", encoding="utf8") as f:
            content = (
                f.read()
                .replace("·", "{\\splitdot}")
                .replace("------", "{\\chsline}")
                .replace("END\n", "\\storyend\n")
                .replace("BLANKLINE", "\\blankline")
                .replace("``", "“")
                .replace("`", "‘")
                .replace("''", "”")
                .replace("'", "’")
                .replace("\\ldots\\ldots ", "\\ldots\\ldots")
                .replace("\\ldots\\ldots{}", "\\ldots\\ldots")
                .replace("\\ldots\\ldots", "……")
                .replace("\\,", "")
                .strip()
            )
        l = re.findall(re.compile(r"\\label\{.[^\n]+\}", re.S), content)
        for j in l:
            content = content.replace(j, "")

        title = {
            -1: "part",
            0: "chapter",
            1: "section",
            2: "subsection",
            3: "subsubsection",
            4: "paragraph",
        }
        res = []
        for j in content.split("\n\n"):
            j = j.replace("\n", " ")
            for k in title.items():
                if j.startswith("\\" + k[1]):
                    j = j.replace("\\" + k[1], "\\" + title[k[0] - 1 + depth])
            res.append(j)
        res.append("")
        res = "\n\n".join(res)

        with open(filename, "w", encoding="utf8") as f:
            f.write("\\documentclass[../main]{subfiles}" + "\n\n")
            f.write("\\begin{document}\n\n\\pagestyle{mystyle}\n\n")
            f.write(res)
            f.write("\\end{document}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_key", type=str)
    parser.add_argument("-d", "--depth", type=int, default=0)
    parser.add_argument("-p", "--path", type=str, default="./latex_output")
    parser.add_argument("-o", "--output_name", type=str)
    args = parser.parse_args()
    LatexConverter(args.input_key, args.depth, args.path, args.output_name)
