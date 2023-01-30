"""
# PyCharm Account
# 2023.01.29
# TanBQ.
"""

from datetime import datetime
from hashlib import *


def encipherment(email, password) -> str:
    """
    对输入的密码加密
     - 加密方法md5
     - 把邮箱和密码拼接加密
    """
    md5_password = md5()
    md5_password.update(bytes(email + password, encoding='utf-8'))
    md5_password = md5_password.hexdigest()
    return str(md5_password)

class Account:
    def __init__(self, name, email, password, brith, location):
        self.name = name
        self.email = email
        self.password = encipherment(email, password)
        self.birth = brith
        self.location = location

        today = datetime.now()
        self.age = int(today.year) - int(brith[:4])

    def __str__(self) -> str:
        return f"{self.name}-{self.email}-{self.password}-{self.birth}-{self.age}-{self.location}"

    def printInfo(self):
        print(f"""
    ===================================
        用户姓名: {self.name}
        用户密码: {self.password}
    -----------------------------------
        注册邮箱: {self.email}
        生日: {self.birth}
        年龄: {self.age}
        位置: {self.location}
    ===================================\n\n""")


def Register():
    # item = {'姓名': 'name', '邮箱': 'email', '密码': 'password', '生日': 'brith', '位置': 'location'}
    # user = {value: input(f"请输入{key}: ") for key, value in item.items()}
    # value = list(user.values())
    # print(value)

    name, email, password, birth, location = iter(
        [input(f"请输入{each}: ") for each in ['姓名', '邮箱', '密码', '生日', '位置']])
    return Account(name, email, password, birth, location)
