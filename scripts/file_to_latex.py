# coding = utf-8

"""
将markdown变为latex
"""

import sys
import os
from utils import search_by_keyword, name_of


class LatexConverter:
    """Latex转换器"""

    def __init__(self, key, depth):
        self.result = search_by_keyword(key)
        if self.result is not None:
            self.depth = depth
            self.to_latex()

    def title(self, line):
        """标题替换"""
        t = line.split(" ")[-1]
        title = {-1: "part", 0: "chapter", 1: "section", 2: "subsection"}
        i = line.count("#") - 1 + self.depth
        return f"\\{title[i]}{{{t}}}"

    def to_latex(self):
        """将目标文件转换为latex"""
        for i in self.result:
            with open(i, "r", encoding="utf8") as f:
                content = f.read()
            filename = "latex/" + name_of(i) + ".tex"
            if not os.path.exists("latex"):
                os.mkdir("latex")
            with open(filename, "w", encoding="utf8") as f:
                f.write("\\documentclass[../main]{subfiles}" + "\n\n")
                f.write("\\begin{document}" + "\n\n")
                for line in content.split("\n\n"):
                    if line.startswith("#"):
                        f.write(self.title(line) + "\n\n")
                    elif line == "":
                        f.write("\\blankline" + "\n\n")
                    elif line.startswith("------"):
                        pass
                    elif line.startswith("[^"):
                        pass
                    elif line.startswith("---"):
                        pass
                    else:
                        f.write(
                            line.replace("·", "{\\splitdot}").replace(
                                "——", "{\\chsline}"
                            )
                            + "\n\n"
                        )
                f.write("\\end{document}")


if __name__ == "__main__":
    DEPTH = 0
    if len(sys.argv) > 2:
        DEPTH = int(sys.argv[2])
    LatexConverter(sys.argv[1], DEPTH)
