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
        GIT_ADD,
        GIT_COMMIT,
        GIT_DEFAULT_MESSAGE,
        GIT_EMAIL,
        GIT_NAME,
        GIT_PUSH,
        RUN_STAT,
    )

    COMMIT_TIME = time.time()
    WORK_PATH = os.path.join(os.getcwd(), DOC_ROOT)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--autocommit",
        type=bool,
        default=GIT_COMMIT,
        nargs="?",
        const=not GIT_COMMIT,
    )
    parser.add_argument("-m", "--message", default=GIT_DEFAULT_MESSAGE)
    parser.add_argument(
        "-s",
        "--statistic",
        type=bool,
        default=RUN_STAT,
        nargs="?",
        const=not RUN_STAT,
    )
    parser.add_argument(
        "-p",
        "--push",
        type=bool,
        default=GIT_PUSH,
        nargs="?",
        const=not GIT_PUSH,
    )
    parser.add_argument(
        "-a", "--add", type=bool, default=GIT_ADD, nargs="?", const=not GIT_ADD
    )
    args = parser.parse_args()

    # 格式化所有文档
    import work_format

    work_format.format_all(WORK_PATH)

    # 字数统计
    counter = None
    if args.statistic:
        import work_record

        counter = work_record.run()

    # 提交文件
    if args.autocommit:
        if args.add:
            os.system("git add .")
        os.system(f"git config user.name {GIT_NAME}")
        os.system(f"git config user.email {GIT_EMAIL}")

        # mes = format_time() + " "
        mes = args.message
        if counter:
            mes += " 更新了" + str(counter.total_change) + "字"

        mes = 'git commit -m "' + mes + '"'
        os.system(mes)

        if args.push:
            os.popen("git pull").close()
            os.popen("git push").close()
