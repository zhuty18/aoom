# coding=utf-8
import os
import sys
from utils import match_keys

try:
    import jieba
    import jieba.analyse
    import wordcloud
    import matplotlib
    import matplotlib.pyplot as plt
    import matplotlib.font_manager as fm
except ModuleNotFoundError:
    print("Requirements Not Found!")


class WordPic:
    def __init__(self, path, job="s", file=None):
        if file != None:
            self.font = fm.FontProperties(fname="data/myfont.ttf", size=15)
            self.job = job
            self.keys = file
            jieba.load_userdict("data/mydict")
            self.drawFiles(path)

    def drawFiles(self, path):
        list = os.listdir(path)
        list.sort()
        for i in list:
            subdir = os.path.join(path, i)
            if os.path.isdir(subdir):
                self.drawFiles(subdir)
            else:
                self.drawPic(subdir, i)

    def drawPic(self, path, name):
        if name.endswith(".md") and (not name.__contains__("README")) and match_keys(self.keys, name):
            print("Drawing " + name)
            if self.job == "r":
                os.remove(path.replace(".md", ".png"))
            else:
                f = open(path, "r", encoding="utf-8")
                str = f.read()
                keywords = jieba.analyse.extract_tags(str, withWeight=True, topK=50)
                # print(name.replace('.md',''))
                # print(keywords)
                fre = {keyword[0]: keyword[1] for keyword in keywords}
                wc = wordcloud.WordCloud(font_path="myfont.ttf", width=600, height=400)
                wc.fit_words(fre)
                if self.job.__contains__("s"):
                    wc.to_file(path.replace(".md", ".png"))
                if self.job.__contains__("p"):
                    matplotlib.use("TkAgg")
                    plt.imshow(wc)
                    plt.title(name.replace(".md", ""), fontproperties=self.font)
                    # plt.ion()
                    # plt.pause(1)
                    # plt.close()
                    plt.show()
                if self.job.__contains__("r"):
                    os.remove(path.replace(".md", ".png"))


if __name__ == "__main__":
    fp = sys.argv[1]
    fn = fp.split("\\")[-1]
    path = os.path.join(os.getcwd(), "\\".join(fp.split("\\")[:-1]))
    # fp=fp.replace(".md",'')
    WordPic(path, "p", [fn])
