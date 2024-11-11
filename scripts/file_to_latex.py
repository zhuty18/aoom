# coding = utf-8

"""
将markdown变为latex
"""

import os
import re
import sys

from utils import name_of, search_by_keyword

TARGET = "D:\\MyResositories\\fanfiction-sample"


class LatexConverter:
    """Latex转换器"""

    def __init__(self, key, depth):
        self.result = search_by_keyword(key)
        if self.result is not None:
            for i in self.result:
                print(name_of(i))
            self.depth = depth
            self.to_latex()

    def to_latex(self):
        """将目标文件转换为latex"""
        for i in self.result:
            filename = TARGET + "/" + name_of(i) + ".tex"
            if not os.path.exists(TARGET):
                os.mkdir(TARGET)
            with open(i, "r", encoding="utf8") as f:
                tmp = f.read()
            tmp = tmp.replace("\n\n\n", "\n\nBLANKLINE\n")
            with open(
                filename.replace(".tex", ".md"), "w", encoding="utf8"
            ) as f:
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
                    .replace("''", "”")
                    .replace("\\ldots\\ldots ", "\\ldots\\ldots")
                    .replace("\\ldots\\ldots{}", "\\ldots\\ldots")
                    .replace("\\ldots\\ldots", "……")
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
            }
            res = []
            for j in content.split("\n\n"):
                j = j.replace("\n", " ")
                for k in title.items():
                    if j.startswith("\\" + k[1]):
                        j = j.replace(
                            "\\" + k[1], "\\" + title[k[0] - 1 + self.depth]
                        )
                res.append(j)
            res.append("")
            res = "\n\n".join(res)

            with open(filename, "w", encoding="utf8") as f:
                f.write("\\documentclass[../main]{subfiles}" + "\n\n")
                f.write("\\begin{document}\n\n\\pagestyle{mystyle}\n\n")
                f.write(res)
                f.write("\\end{document}")


if __name__ == "__main__":
    DEPTH = 0
    if len(sys.argv) > 2:
        DEPTH = int(sys.argv[2])
    LatexConverter(sys.argv[1], DEPTH)
