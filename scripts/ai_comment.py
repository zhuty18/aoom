# coding = utf-8

"""AI评论"""

import os
import sys

from encrypt import api_key
from openai import OpenAI
from personal import AI_PATH, AI_PROMPTS, AI_SYSTEM_PROMPT, AI_TEMPLATE
from utils import FileBasic, filenames_of_key

AI_PROMPT = "评论"


def comment(filename, print_res):
    """AI评论文章"""
    client = OpenAI(
        api_key=api_key(),
        base_url="https://api.deepseek.com",
    )
    with open(filename, "r", encoding="utf-8") as f:
        file_content = f.read()

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": AI_SYSTEM_PROMPT},
            {
                "role": "user",
                "content": AI_PROMPTS[AI_PROMPT].replace(
                    "{file_content}", file_content
                ),
            },
        ],
        temperature=1.3,
        stream=False,
    )
    res = response.choices[0].message.content

    with open(AI_TEMPLATE, "r", encoding="utf-8") as f:
        template_content = f.read()
    ai_path = os.path.join(AI_PATH, FileBasic(filename).filename()) + ".md"

    with open(ai_path, "w", encoding="utf-8") as f:
        f.write(template_content + res.strip() + "\n")

    if print_res:
        print(res)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("丢失文件名参数")
    else:
        for i in filenames_of_key(sys.argv[1]):
            if not FileBasic(i).__ai_write__():
                comment(i, True)
