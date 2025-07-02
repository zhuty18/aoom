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
        DOC_ROOT,
        GIT推送,
        GIT提交,
        GIT添加,
        GIT署名,
        GIT邮箱,
        GIT默认信息,
        进行统计,
    )

    COMMIT_TIME = time.time()
    工作路径 = os.path.join(os.getcwd(), DOC_ROOT)

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
    parser.add_argument(
        "-p",
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

    # 格式化所有文档
    import work_format

    work_format.全部格式化(工作路径)

    # 字数统计
    统计器 = None
    if args.statistic:
        import work_record

        统计器 = work_record.进行字数统计()

    # 提交文件
    if args.autocommit:
        if args.add:
            os.system("git add .")
        os.system(f"git config user.name {GIT署名}")
        os.system(f"git config user.email {GIT邮箱}")

        # mes = format_time() + " "
        mes = args.message
        if 统计器:
            mes += " 更新了" + str(统计器.总字数变更) + "字"

        mes = 'git commit -m "' + mes + '"'
        os.system(mes)

        if args.push:
            os.popen("git pull").close()
            os.popen("git push").close()
