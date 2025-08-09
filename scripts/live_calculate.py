# coding = utf-8
"""计算文件大小与字数的拟合关系"""

import itertools
import os

import numpy as npy
from file_status import FileStatus


def file_count(filename):
    """获取文件字数、大小"""
    文件 = FileStatus(filename)
    acc = 文件.get_yaml("word_count")
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


def fit(data, points, p=False):
    """拟合数据"""
    sign = []
    r2 = []
    fit_y = npy.array([])
    l = len(points)
    for index in range(l):
        if index == l - 1:
            d = [x for x in data if x[1] >= points[index]]
        else:
            d = [x for x in data if points[index] <= x[1] <= points[index + 1]]
        x = npy.array([a for _, a in d])
        y = npy.array([a for a, _ in d])

        if len(x) > 2:
            s, i = npy.polyfit(x, y, 1)
            sign.append(
                {
                    "s": float(s),
                    "i": float(i),
                    "min": points[index],
                    "max": points[index + 1] if index != l - 1 else -1,
                }
            )
            fit_y = npy.append(fit_y, s * x + i)

            sst = ((y - y.mean()) ** 2).sum()
            ssr = ((s * x + i - y.mean()) ** 2).sum()
            r2.append(ssr / sst)

    if len(sign) < 2 and len(points) > 2:
        if p:
            print(sign)
        return 0, 0, {}

    if len(sign) != len(points):
        mins = [x["min"] for x in sign]
        mins.sort()
        if mins[0] != points[0]:
            sign.append(
                {
                    "s": sign[0]["s"],
                    "i": sign[0]["i"],
                    "min": points[0],
                    "max": sign[0]["min"],
                }
            )
            sign.sort(key=lambda x: x["min"])
        l = len(sign)
        for i in range(l - 1):
            if sign[i]["max"] != sign[i + 1]["min"]:
                sign.append(
                    {
                        "s": (sign[i]["s"] + sign[i + 1]["s"]) / 2,
                        "i": (sign[i]["i"] + sign[i + 1]["i"]) / 2,
                        "min": sign[i]["max"],
                        "max": sign[i + 1]["min"],
                    }
                )
        sign.sort(key=lambda x: x["min"])
        if sign[-1]["max"] != -1:
            sign.append(
                {
                    "s": sign[-1]["s"],
                    "i": sign[-1]["i"],
                    "min": sign[-1]["max"],
                    "max": -1,
                }
            )

    y = npy.array([a for a, _ in data])
    sst = ((y - y.mean()) ** 2).sum()
    ssr = ((fit_y - y.mean()) ** 2).sum()

    return float(npy.array(r2).mean()), float(ssr / sst), sign


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

    breaks = 3
    min_gap = 10000

    r2_max = 0
    best = None
    r2_real = 0

    for breaks in itertools.combinations(breaks, breaks):
        breaks = list(breaks)
        p = False
        for i in range(1, len(breaks)):
            if breaks[i] - breaks[i - 1] < min_gap:
                p = True
                break
        if not p:
            breaks.insert(0, 0)
            breaks.sort()
            r2, real, sign = fit(data, breaks)
            if r2 > r2_max and real > 0.995:
                r2_max = r2
                best = sign
                r2_real = real
    print(r2_max, r2_real)
    print(best)
    print(fit(data, [0]))
