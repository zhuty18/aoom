import os
import re

epName = {}
list = os.listdir(".")


def rename(s2):
    t1 = re.compile(r'E(.*?) ', re.S)
    t2 = re.compile(r'- (.*?) [(]', re.S)
    s = 'E' + re.findall(t1, s2)[0]
    s1 = re.findall(t2, s2)[0] + 'ddd'
    t3 = re.compile(r'- (.*?)ddd', re.S)
    s1 = re.findall(t3, s1)[0]
    s1 = s1.replace(' ', '')
    s1 = s1.replace('\'', '')
    s1 = s1.replace(',', '')
    s = "Justice.League.Action.Shorts.S01" + s + '.' + s1 + ".720p.WEB-DL.H.264"
    return s


def cut(str):
    t = re.compile(r'2019.(.*)1080p', re.S)
    return re.findall(t, str)[0]


def getEpName():
    for i in list:
        if i.__contains__(".ass"):
            k = cut(i)
            epName[k.split('.')[0]] = k
    print(epName)


def rename2(str):
    k = cut(str)
    if k.split('.')[0] in epName.keys():
        m = epName[k.split('.')[0]]
        str = str.replace(k, m)
    return str


def exc(forma):
    for i in list:
        if i.__contains__(forma):
            s = rename2(i)
            print(s)
            m = "ren \"" + i + "\" \"" + s + forma + "\""
            # print(m)
            os.system(m)


def exc2(f, t):
    for i in list:
        if i.__contains__(f):
            s = i.replace(f, t)
            print(s)
            m = "ren \"" + i + "\" \"" + s + "\""
            # print(m)
            os.system(m)


def rename3():
    t1 = re.compile(r"(\d+)-\d+-\d+", re.S)
    t2 = re.compile(r"[(]_(\d+)[)]", re.S)
    t3 = re.compile(r", .*?[)] ", re.S)
    for i in list:
        if i.__contains__("_"):
            try:
                s1 = re.findall(t1, i)[0]
                s2 = re.findall(t2, i)[0]
                s3 = re.findall(t3, i)[0]
                if len(s2) == 2:
                    s2 = "0" + s2
                t = " " + s2 + " (" + s1 + ") "
                s = i.replace(s3, t)
            except IndexError:
                s = i.replace("_", "")
            m = "ren \"" + i + "\" \"" + s + "\""
            print(m)
            # os.system(m)


def rename4():
    t1 = re.compile(r"[(](\d+)-\d+[)]", re.S)
    t2 = re.compile(r" (\d+) ", re.S)
    t3 = re.compile(r" [(].*? \d+ ", re.S)
    for i in list:
        if i.__contains__("-"):
            try:
                s1 = re.findall(t1, i)[0]
                s2 = re.findall(t2, i)[0]
                s3 = re.findall(t3, i)[0]
                if len(s2) == 2:
                    s2 = "0" + s2
                t = " " + s2 + " (" + s1 + ") "
                s = i.replace(s3, t)
            except IndexError:
                s = i.replace("_", "")
            m = "ren \"" + i + "\" \"" + s + "\""
            # print(m)
            os.system(m)


def rename5():
    for i in list:
        if i.__contains__("n-B"):
            s = i.replace("n-B", "n B")
            m = "ren \"" + i + "\" \"" + s + "\""
            # print(m)
            os.system(m)


def rename6(name):
    for i in list:
        if i.__contains__(".ass"):
            s = i.upper()
            s = s.replace(name.upper(), name)
            s = s.replace("BLURAY", "BluRay")
            s = s.replace("X264", "x264")
            s = s.replace("0P", "0p")
            s = s.replace(".ASS", ".ass")
            m = "ren \"" + i + "\" \"" + s + "\""
            # print(m)
            os.system(m)


rename6("Friends")
