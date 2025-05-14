# coding = utf-8

"""
提交至git
"""

import argparse
import os
import sys
import time

if __name__ == "__main__":
    sys.path.append("./scripts")
    os.system("git config --global core.quotepath false")

    from personal import (
        GIT推送,
        GIT提交,
        GIT添加,
        GIT署名,
        GIT邮箱,
        GIT默认信息,
        其他顺序,
        文档根,
        更改文件,
        词云工作,
        词云范围,
        进行统计,
        默认顺序,
    )

    COMMIT_TIME = time.time()
    FILE_DIR = os.path.join(os.getcwd(), 文档根)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--autocommit",
        type=bool,
        default=GIT提交,
        nargs="?",
        const=not GIT提交,
    )
    parser.add_argument("-m", "--message", default=GIT默认信息)
    parser.add_argument(
        "-s",
        "--statistic",
        type=bool,
        default=进行统计,
        nargs="?",
        const=not 进行统计,
    )
    parser.add_argument("-word", "--word_cloud", type=str, default=词云范围)
    parser.add_argument(
        "-o",
        "--sort_order",
        type=str,
        default=默认顺序,
        nargs="?",
        const=其他顺序,
    )
    parser.add_argument(
        "-push",
        "--push",
        type=bool,
        default=GIT推送,
        nargs="?",
        const=not GIT推送,
    )
    parser.add_argument(
        "-a", "--add", type=bool, default=GIT添加, nargs="?", const=not GIT添加
    )
    args = parser.parse_args()

    # 解决obsidian换行符
    from win4obsidian import touch_obsidian

    touch_obsidian()

    # 格式化所有文档
    import work_format

    work_format.format_all(FILE_DIR)

    # 字数统计
    if args.statistic:
        import work_record

        work_record.进行字数统计(FILE_DIR, args.sort_order).暂存更改(更改文件)

    # 提交文件
    if args.autocommit:
        if args.add:
            os.system("git add .")
        os.system(f"git config user.name {GIT署名}")
        os.system(f"git config user.email {GIT邮箱}")

        # mes = format_time() + " "
        mes = args.message
        try:
            mes += " 更新了" + str(统计器.total_change) + "字"
        except NameError:
            pass
        mes = 'git commit -m "' + mes + '"'
        os.system(mes)

        if args.push:
            os.popen("git pull").close()
            os.popen("git push").close()

    if args.word_cloud != "none":
        import word_cloud_make

        word_cloud_make.WordPic(
            path=FILE_DIR, job=词云工作, file=[args.word_cloud]
        )
