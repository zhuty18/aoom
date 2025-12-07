# coding = utf-8

"""文件记录"""

import os
import subprocess
import time

from file_status import FileCount
from personal import PATH_HISTORY
from utils import folder_path, hide_fin, name_of_dir


class WordCounter:
    """字数统计器"""

    def __init__(self):
        self.total_change = 0
        self.file_map: dict[str, FileCount] = {}
        self.change_files: list[FileCount] = []

    def run(self):
        """工作函数"""
        self.read_history()
        self.get_changes()
        self.clean_deleted()
        self.update_files()

    def read_history(self):
        """从历史记录中读取已有条目"""
        if os.path.exists(PATH_HISTORY):
            with open(PATH_HISTORY, "r", encoding="utf-8") as f:
                for i in f.readlines():
                    f = FileCount.from_history(i)
                    if f:
                        self.file_map[f.filename()] = f

    def get_changes(self):
        """读取变更的文件目录"""
        os.environ["PYTHONIOENCODING"] = "utf8"
        os.system("git add .")
        with subprocess.Popen(
            ["git", "status", "-s"], stdout=subprocess.PIPE
        ) as pipe:
            output = pipe.communicate()[0]
        output = output.decode("utf8")
        for i in output.split("\n"):
            if "->" in i:
                i = i.split("->")[-1].strip()
            if i:
                i = i.split("  ")[-1]
                i = i.strip('"')
            if FileCount(i, None).legal():
                if os.path.exists(i) and name_of_dir(folder_path(i)):
                    self.change_files.append(FileCount.from_path(i))

    def clean_deleted(self):
        """清除历史记录中消失了的文件"""
        tmp = {}
        for v in self.file_map.values():
            if v.is_exist():
                tmp[v.filename()] = v
        self.file_map = tmp

    def update_files(self):
        """变更记录进原文件"""
        for i in self.change_files:
            if i.is_exist():
                old_length = (
                    self.file_map[i.filename()].his_length
                    if i.filename() in self.file_map
                    else 0
                )
                if i.length() == old_length:
                    continue
                else:
                    i.mark_auto_date()
                    print(f"{i.filename()}\t{old_length} -> {i.length()}")
                self.total_change += i.length() - old_length
                self.file_map[i.filename()] = i
            else:
                self.file_map.pop(i.filename())

    def update_history(self):
        """更新历史数据"""
        with open(PATH_HISTORY, "w", encoding="utf-8", newline="\n") as f:
            for key in sorted(self.file_map.keys()):
                f.write(f"{self.file_map[key].history_entry()}\n")


def run():
    """进行字数统计"""
    counter = WordCounter()
    counter.run()
    counter.update_history()
    hide_fin()
    return counter


if __name__ == "__main__":
    t = time.time()
    run()
    print(time.time() - t)
