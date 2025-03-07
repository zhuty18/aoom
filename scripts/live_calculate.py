# coding = utf-8
"""计算文件大小与字数的拟合关系"""

import os

import numpy as npy
from utils import get_pre_key, get_predefine


def file_count(filename):
    """获取文件字数、大小"""
    pre_d = get_predefine(filename)
    if pre_d:
        acc = get_pre_key(pre_d, "word_count")
        if acc:
            return (int(acc), os.path.getsize(filename))
    return (0, 0)


def count_all(path):
    """获取文件夹字数、大小"""
    l = os.listdir(path)
    res = {(0, 0)}
    for item in l:
        subdir = os.path.join(path, item)
        if os.path.isdir(subdir) and not "/." in subdir:
            res.update(count_all(subdir))
        elif subdir.endswith(".md"):
            res.add(file_count(subdir))
        elif os.path.isdir(subdir) and "data" in subdir:
            res.update(count_all(subdir))
    return res


if __name__ == "__main__":
    data = count_all(os.path.join(os.getcwd(), "docs"))
    data.discard((0, 0))
    data = list(sorted(data, key=lambda x: x[0]))
    data = [x for x in data if x[1] < 800]
    # print(data)

    x = npy.array([x for _, x in data])
    y = npy.array([y for y, _ in data])
    # print(x,y)

    s, i = npy.polyfit(x, y, 1)
    print(s, i)
    # plt.scatter(x, y)
    # plt.plot(x, s * x + i, color="red")
    # plt.show()

    sst = ((y - y.mean()) ** 2).sum()
    ssr = ((s * x + i - y.mean()) ** 2).sum()
    print(ssr / sst)
