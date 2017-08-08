# coding=utf-8
from cookielib import LWPCookieJar

import requests.utils
import requests

from app.models.account import Account
from app.settings import COOKIE_FILENAME

user = Account('786373153@qq.com', 'wrx0831')


def auth():
    tmp = requests.utils.dict_from_cookiejar(user.cookies)
    session = requests.Session()
    cookie = LWPCookieJar()
    cookie.load(filename=COOKIE_FILENAME)
    print type(cookie), cookie
    session.cookies = cookie
    s = session.post('https://www.leetcode.com/dream_going')
    print s.status_code


if __name__ == '__main__':
    user.login()
    print user.is_login
    print user.username
    tmp = requests.utils.dict_from_cookiejar(user.cookies)
    print tmp
    auth()
