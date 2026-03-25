# coding = utf-8

"""API-Key加密"""

import os
import sys

D = ""
for i in range(10):
    D += str(i)
for i in range(26):
    D += chr(i + ord("a"))


def decrypt(key):
    with open("encrypt_key.txt", "r", encoding="utf-8") as f:
        encrypted = f.read().strip()

    res = ""
    for index, v in enumerate(encrypted):
        if index <= 2:
            res += v
        else:
            p = key[index % len(key)]
            res += D[(D.index(v) - D.index(p)) % len(D)]
    print(res)
    with open("api_key.txt", "w", encoding="utf-8") as f:
        f.write(res)


def api_key():
    if os.path.exists("api_key.txt"):
        with open("api_key.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    else:
        raise FileNotFoundError("本地没有api-key！")


def encrypt(plain, key):
    res = ""
    for index, v in enumerate(plain):
        if index <= 2:
            res += v
        else:
            e = key[index % len(key)]
            res += D[(D.index(e) + D.index(v)) % len(D)]
    with open("encrypt_key.txt", "w", encoding="utf-8") as f:
        f.write(res)


if __name__ == "__main__":
    if len(sys.argv) > 2:
        encrypt(api_key(), sys.argv[1])
    else:
        decrypt(sys.argv[1])
