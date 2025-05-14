# coding = utf-8
"""计算文件大小与字数的拟合关系"""

import itertools
import os

import numpy as npy
from file_status import 文件属性


def file_count(filename):
    """获取文件字数、大小"""
    文件 = 文件属性(filename)
    acc = 文件.读取yaml内参数("word_count")
    return (int(acc), os.path.getsize(filename)) if acc else (0, 0)


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


def 拟合(data, 断点, p=False):
    """拟合数据"""
    指标 = []
    r2 = []
    fit_y = npy.array([])
    l = len(断点)
    for index in range(l):
        if index == l - 1:
            d = [x for x in data if x[1] >= 断点[index]]
        else:
            d = [x for x in data if 断点[index] <= x[1] <= 断点[index + 1]]
        x = npy.array([a for _, a in d])
        y = npy.array([a for a, _ in d])

        if len(x) > 2:
            s, i = npy.polyfit(x, y, 1)
            指标.append(
                {
                    "s": float(s),
                    "i": float(i),
                    "min": 断点[index],
                    "max": 断点[index + 1] if index != l - 1 else -1,
                }
            )
            fit_y = npy.append(fit_y, s * x + i)

            sst = ((y - y.mean()) ** 2).sum()
            ssr = ((s * x + i - y.mean()) ** 2).sum()
            r2.append(ssr / sst)

    if len(指标) < 2:
        if p:
            print(指标)
        return 0, {}

    if len(指标) != len(断点):
        mins = [x["min"] for x in 指标]
        mins.sort()
        if mins[0] != 断点[0]:
            指标.append(
                {
                    "s": 指标[0]["s"],
                    "i": 指标[0]["i"],
                    "min": 断点[0],
                    "max": 指标[0]["min"],
                }
            )
            指标.sort(key=lambda x: x["min"])
        l = len(指标)
        for i in range(l - 1):
            if 指标[i]["max"] != 指标[i + 1]["min"]:
                指标.append(
                    {
                        "s": (指标[i]["s"] + 指标[i + 1]["s"]) / 2,
                        "i": (指标[i]["i"] + 指标[i + 1]["i"]) / 2,
                        "min": 指标[i]["max"],
                        "max": 指标[i + 1]["min"],
                    }
                )
        指标.sort(key=lambda x: x["min"])
        if 指标[-1]["max"] != -1:
            指标.append(
                {
                    "s": 指标[-1]["s"],
                    "i": 指标[-1]["i"],
                    "min": 指标[-1]["max"],
                    "max": -1,
                }
            )

    y = npy.array([a for a, _ in data])
    sst = ((y - y.mean()) ** 2).sum()
    ssr = ((fit_y - y.mean()) ** 2).sum()

    return float(npy.array(r2).mean()), float(ssr / sst), 指标


if __name__ == "__main__":
    data = count_all(os.path.join(os.getcwd(), "docs"))
    data.discard((0, 0))
    data = list(sorted(data, key=lambda x: x[0]))
    x = [a for _, a in data]
    y = [a for a, _ in data]
    # print(data)

    breaks = []
    breaks.extend(list(range(500, 2000, 100)))
    breaks.extend(list(range(2000, 20000, 2000)))
    breaks.extend(list(range(20000, 50000, 5000)))
    breaks.extend(list(range(50000, 160000, 30000)))

    断点数 = 3
    最短间距 = 10000

    r2_max = 0
    最优解 = None
    真r2 = 0

    for 断点 in itertools.combinations(breaks, 断点数):
        断点 = list(断点)
        p = False
        for i in range(1, len(断点)):
            if 断点[i] - 断点[i - 1] < 最短间距:
                p = True
                break
        if not p:
            断点.insert(0, 0)
            断点.sort()
            r2, 真实值, 指标 = 拟合(data, 断点)
            if r2 > r2_max and 真实值 > 0.995:
                r2_max = r2
                最优解 = 指标
                真r2 = 真实值
    print(r2_max, 真r2)
    print(最优解)
