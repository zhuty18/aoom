import os
import re

epName = {}
list = os.listdir(".")


def link(file):
    s = file.replace(" - ", ".")
    s = s.replace(" ", ".")
    s = s.replace("(", "")
    s = s.replace(")", "")
    return s


def all_link(dic):
    if not os.path.exists(dic):
        os.mkdir(dic)
    for i in list:
        if i.__contains__(".mp4"):
            tar = "梦华录." + i.replace("TJUPT", "HDSWEB")
            tar=tar.replace("1080p.WEB-DL","WEB-DL.1080p")
            m = os.path.join(dic, tar)
            m = "mklink /H \"" + m + "\" \"" + os.path.join(os.getcwd(), i) + "\""
            print(m)
            os.system(m)


# all_link("E:\DC\Batman.the.Brave.and.the.Bold")
all_link("E:\\Ourbits\\梦华录.A.Dream.of.Splendor.S01.2022.WEB-DL.1080p.H264.AAC-HDSWEB")
