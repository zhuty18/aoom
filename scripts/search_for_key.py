# coding = utf-8

"""检索某个关键词"""

import sys

from utils import file_has_key

if __name__ == "__main__":
    key = sys.argv[1]
    file_has_key(key)
