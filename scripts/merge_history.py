# coding = utf-8

"""重构仓库后融合过往历史"""

import os

from work_record import FileRecord, WordCounter

old_history = "data/old_history.txt"
new_history = "data/history.txt"


class LoadHistory(WordCounter):
    """历史记录自定义加载器"""

    def __init__(self, history_path):
        self.path = history_path
        super().__init__()

    def run_load(self, other):
        """运行"""
        self.read_history()
        other.read_history()
        self.merge_history(other)
        self.update_history()

    def read_history(self):
        """从历史记录中读取已有条目"""
        if os.path.exists(self.path):
            with open(self.path, "r", encoding="utf-8") as f:
                for i in f.readlines():
                    t = FileRecord.from_record(i)
                    self.history[t.name] = t

    def merge_history(self, other):
        """融合数据"""
        for k, v in other.history.items():
            if k in self.history:
                self.history[k].merge(v)
            else:
                self.history[k] = v

    def update_history(self):
        """更新历史数据"""
        with open(self.path, "w", encoding="utf-8") as f:
            for _, value in self.history.items():
                f.write(f"{value}\n")


old = LoadHistory(old_history)
new = LoadHistory(new_history)
new.run_load(old)
