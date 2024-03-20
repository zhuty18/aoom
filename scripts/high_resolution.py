# coding = utf-8

"""根据md生成高清版本"""

import sys

file_path = sys.argv[1]
with open(file_path, "r", encoding="utf8") as f:
    con = f.read()
con = con.replace("comic/", "comic-origin/")
with open(file_path.replace(".md", "-高清.md"), "w", encoding="utf8") as f:
    f.write(con)
