# coding=utf-8

from app.models.account import Account

user = Account('786373153@qq.com', 'wrx0831')

if __name__ == '__main__':
    user.login()
    print user.is_login
    print user.username
