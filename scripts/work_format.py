# coding = utf-8

"""格式化文件库"""

import os
from utils import doc_dir


def format_file(filename):
    """格式化文件"""
    f = open(filename, "r", encoding="utf-8")
    content = f.readlines()
    f.close()
    f = open(filename, "w", encoding="utf-8")
    # print(content)
    for i in content:
        if filename.endswith(".py"):
            f.write(i.strip("\n") + "\n")
        else:
            f.write(i.strip() + "\n")
    f.close()


def format_blob(filename):
    """格式化短篇"""
    if filename.endswith(".md"):
        return
    with open(filename, "r", encoding="utf8") as f:
        content = f.readlines()
    path = filename.split("\\")
    name = path.pop(-1)
    new_name = name.split(" ")
    date = new_name.pop(0)
    new_name = " ".join(new_name)
    new_name = new_name.replace(".txt", ".md")
    title = new_name.replace(".md", "")
    path.append(new_name)
    new_name = "\\".join(path)
    new = f"---\ntags: blob\ndate: {date}\n---\n\n"
    with open(new_name, "w", encoding="utf8") as f:
        new += f"# {title}\n\n"
        for _ in range(6):
            content.pop(0)
        for line in content:
            new += line.strip() + "\n\n"
        f.write(new.strip() + "\n")


def format_all(path):
    """从根目录起格式化所有文件"""
    l = os.listdir(path)
    for i in l:
        subdir = os.path.join(path, i)
        if os.path.isdir(subdir) and not "/." in subdir:
            format_all(subdir)
        elif "教程" in subdir:
            pass
        elif "blob" in subdir:
            format_blob(subdir)
        elif (
            subdir.endswith(".md")
            or subdir.endswith(".txt")
            or subdir.endswith(".py")
        ):
            format_file(subdir)
        elif os.path.isdir(subdir) and "data" in subdir:
            format_all(subdir)


if __name__ == "__main__":
    format_all(os.path.join(doc_dir(), "blob"))
