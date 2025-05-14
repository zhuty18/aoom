# coding = utf-8

"""文件管理"""

import os
import re
import subprocess

from personal import (
    AI评论路径,
    完结标志,
    忽略文件,
    忽略路径,
    提交时间,
    摘要长度,
    文档根,
    日期格式,
)
from utils import (
    tag优先级,
    完结路径,
    文件夹路径,
    格式化时间,
    相对路径,
    获取log时间,
    获取文件_文件名,
    获取时间戳,
    行长度,
    路径名,
)


class 文件属性:
    """文件记录"""

    def __init__(self, 路径, 时间, 历史长度=0, 历史完结=False):
        self._路径 = 相对路径(路径)
        self._时间 = 时间 if 时间 else 提交时间
        self.历史字数 = 历史长度
        self.历史完结 = 历史完结

        self._文件名 = None
        self._标题 = None
        self._完结 = None
        self._字数 = None
        self._yaml = None

    @staticmethod
    def 从历史条目(历史):
        """从历史条目中获取信息"""
        条目 = 历史.strip().split("\t")
        return 文件属性(
            获取文件_文件名(条目[0]),
            获取时间戳(条目[2]),
            int(条目[1]),
            条目[3] == "True",
        )

    @staticmethod
    def 从路径(路径):
        """从路径中获取信息"""
        pipe = subprocess.Popen(["git", "log", 路径], stdout=subprocess.PIPE)
        output, _ = pipe.communicate()
        output = output.decode("utf8")
        commit = None
        for i in output.split("\n"):
            if i.startswith("Date: "):
                commit = i
                break
        if commit is not None:
            t = re.findall(re.compile(r"Date:\s*(.*?)\s*\+", re.S), commit)[
                0
            ].strip()
            时间 = 获取log时间(t)
        else:
            时间 = None
        return 文件属性(路径, 时间)

    def 存在(self):
        """文件是否存在"""
        return os.path.exists(self._路径)

    def 路径(self):
        """文件路径"""
        return self._路径

    def 文件名(self):
        """文件名"""
        if self._文件名 is None:
            self._文件名 = (
                self._路径.replace("\\", "/").replace(".md", "").split("/")[-1]
            )
        return self._文件名

    def 标题(self):
        """文件标题"""
        if self._标题 is None:
            if "title" in self.__yaml内容():
                return self.__yaml内容()["title"]
            标题 = self.文件名()
            with open(self._路径, "r", encoding="utf8") as f:
                content = f.read()
                for i in content.split("\n\n"):
                    if i.startswith("# "):
                        标题 = i[2:].strip()
                        break
            self._标题 = 标题
        return self._标题

    def 已完结(self):
        """是否完结"""
        if self._完结 is None:
            # print(self._路径,完结路径(文件夹路径(self._路径)))
            if 完结路径(文件夹路径(self._路径)):
                self._完结 = True
            elif self.读取yaml内参数("finished") == "true":
                self._完结 = True
            else:
                with open(self._路径, "r", encoding="utf8") as f:
                    text = f.read()
                    ends = 完结标志
                    for i in ends:
                        if f"{i}\n" in text:
                            self._完结 = True
            if self._完结 is None:
                self._完结 = False
        return self._完结

    def 字数(self, 打印过程=False):
        """文件长度"""
        if self._字数 is None:
            res = 0
            with open(self._路径, "r", encoding="utf8") as f:
                content = f.read().replace(self.__yaml字符串(), "").strip("-\n")
            heading = ""
            count = 0
            level = 0
            for i in content.split("\n"):
                if i.startswith("#"):
                    if heading:
                        if 打印过程:
                            print("\t" * level + heading + "\t" + str(count))
                        res += count
                        count = 0
                    heading = i.strip("#").strip()
                    level = i.count("#") - 1
                count += 行长度(i.strip())
            if 打印过程:
                print("\t" * level + heading + "\t" + str(count))
            res += count
            if heading != self.标题() and 打印过程:
                print(self.标题() + "\t" + str(res))
            self._字数 = res
        return self._字数

    def 更新时间(self):
        """文件更新时间"""
        return 格式化时间(self._时间)

    def 历史信息条目(self):
        """历史信息条目"""
        return f"{self.文件名()}\t{self.字数()}\t{self.更新时间()}\t{self.已完结()}"

    def 链接(self):
        """文件链接"""
        return 相对路径(self._路径, 文档根).replace(" ", "%20")

    def md信息条目(self):
        """Markdown信息条目"""
        return f"|[{self.文件名()}]({self.文件名().replace(" ", "%20")}.md)|{self.字数()}|{self.更新时间()}|"

    def 预览(self):
        """文件预览"""
        with open(self._路径, "r", encoding="utf8") as f:
            yaml = False
            pre = ""
            exp = re.compile(r".*?(\[\^\d+\]).*?", re.S)
            for i in f.readlines():
                if i == "---\n":
                    yaml = not yaml
                    continue
                if yaml:
                    continue
                if i.startswith("#"):
                    pre += "<br>\n"
                    continue
                tmp = re.findall(exp, i)
                if tmp:
                    for j in tmp:
                        i = i.replace(j, "")
                pre += i
                if "<br>\n\n" in pre:
                    pre = pre.split("<br>")[1].strip()
                if len(pre) > 摘要长度 * 0.7:
                    pre = pre.strip()
                    break
        if len(pre) > 摘要长度 * 1.2:
            pre = pre[:摘要长度] + "……"
        if pre.count("*") % 2 == 1:
            pre += "*"
        return pre

    def 格式化中忽略(self):
        """忽略格式化"""
        for i in 忽略文件:
            if i in self._路径:
                return True
        for i in 忽略路径:
            if i in self._路径:
                return True
        return "_" in self._路径

    def ai评论(self):
        """获取AI评论文件"""
        if self.ai创作():
            return None
        ai评论 = os.path.join(AI评论路径, self.文件名()) + ".md"
        return ai评论 if os.path.exists(ai评论) else None

    def ai创作(self):
        """是否为AI创作"""
        return AI评论路径 in self._路径

    def ai源文件(self):
        """获取AI对应的源文件"""
        return 获取文件_文件名(self.文件名())[0] if self.ai创作() else None

    def __yaml字符串(self):
        """读取yaml字符串"""
        with open(self._路径, "r", encoding="utf8") as f:
            content = f.read()
        if content.startswith("---"):
            return content[0 : content.index("---", 3)].strip("-\n")
        return None

    def __yaml内容(self):
        """读取yaml内容"""
        if self._yaml is None:
            yaml字符串 = self.__yaml字符串()
            if not yaml字符串:
                return {}
            yaml内容 = {}
            current = ""
            for i in yaml字符串.split("\n"):
                if ":" in i:
                    i = i.split(":")
                    key = i[0].strip()
                    current = key
                    value = i[1].strip()
                    if key == "tags" and " " in value:
                        value = value.split(" ")
                    elif key == "tags" and value != "":
                        value = [value]
                    elif key == "tags":
                        value = []
                    elif value == "":
                        value = []
                    yaml内容[key] = value
                elif "  - " in i:
                    yaml内容[current].append(i.strip(" -"))
            if "tags" in yaml内容 and "FIN" in yaml内容["tags"]:
                yaml内容["tags"].remove("FIN")
            self._yaml = yaml内容
        return self._yaml

    def __更新yaml(self):
        """更新yaml区域"""
        res = ""
        if "tags" in self.__yaml内容():
            self.__yaml内容()["tags"] = sorted(
                self.__yaml内容()["tags"], key=tag优先级
            )
        for k, v in sorted(self.__yaml内容().items()):
            if isinstance(v, list):
                res += f"{k}:\n  - {"\n  - ".join(v)}\n"
            else:
                res += f"{k}: {v}\n"
        res = res.strip()

        yaml字符串 = self.__yaml字符串()
        with open(self._路径, "r", encoding="utf8") as f:
            content = f.read()
        if yaml字符串:
            with open(self._路径, "w", encoding="utf8") as f:
                f.write(content.replace(yaml字符串, res))
        else:
            with open(self._路径, "w", encoding="utf8") as f:
                f.write(f"---\n{res}\n---\n\n{content}")

    def 整理yaml(self):
        """整理yaml区域"""
        if self.__yaml内容():
            self.__更新yaml()

    def 读取yaml内参数(self, 关键字):
        """读取yaml内参数"""
        if 关键字 == "tags":
            return self.__yaml内容().get(关键字, [])
        return self.__yaml内容().get(关键字)

    def __添加yaml参数(self, 关键字, 值, 修改=False):
        """添加yaml参数"""
        if 关键字 in self.__yaml内容() and not 修改:
            return
        self.__yaml内容()[关键字] = 值
        self.__更新yaml()

    def 在yaml增加类(self):
        """在yaml增加类"""
        self.__添加yaml参数("category", 路径名(文件夹路径(self._路径)))

    def 标记完成(self, 强制=False):
        """标记完成"""
        if self.已完结():
            self.__添加yaml参数("finished", "true", 修改=True)
        elif 强制:
            self.__添加yaml参数("finished", "false")

    def 标记发布(self):
        """标记发布"""
        self.__添加yaml参数("post", "true", 修改=True)

    def 标注更新日期(self):
        """为文件标注更新日期"""
        self.__添加yaml参数(
            "auto_date", 格式化时间(self._时间, 日期格式), 修改=True
        )
