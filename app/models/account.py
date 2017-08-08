# coding=utf-8
import json

import requests
import logging
import re

from app.settings import URL_BASE
from app.models.base import Model
from app.decorators.auth import authenticated
from app.decorators.common import timing_function
from app.settings import COOKIE_FILENAME


# TODO think the design pattern
class Account(Model):
    def __init__(self, account, password):
        super(Account, self).__init__()
        self.account = account
        self.password = password

    @timing_function
    def login(self):
        # TODO exception handing
        login_url = URL_BASE + '/accounts/login/'
        login_data = {'login': self.account,
                      'password': self.password,
                      'csrfmiddlewaretoken': self.csrfmiddlewaretoken}

        self.do_request(url=login_url, data=login_data)
        self.post(url=login_url, data=login_data)
        self.cookies.save(filename=COOKIE_FILENAME, ignore_discard=True)

    def login_with_cookie(self):
        pass

    @property
    def is_login(self):
        profile_url = URL_BASE + '/profile/'
        page = self.do_request(method='get', url=profile_url)
        return page.status_code == 200

    # TODO to find out the difference between decorators order, add decorator
    @property
    def username(self):
        """
        get leetcode username from local cookie
        :return:
        """
        cookie = requests.utils.dict_from_cookiejar(self.cookies)
        msg = cookie['messages']
        regex = re.compile('as (.*?)\.')
        user_name = regex.search(msg)
        return user_name.group(1)
