# coding=utf-8

import logging
import re

from app.settings import URL_BASE
from app.models.base import Model
from app.decorators.auth import authenticated
from app.settings import COOKIE_FILENAME


class Account(Model):
    login_url = URL_BASE + '/accounts/login/'

    def __init__(self, account, password):
        super(Account, self).__init__()
        self.account = account
        self.password = password

    def login(self):
        login_data = {'login': self.account,
                      'password': self.password,
                      'csrfmiddlewaretoken': self.csrfmiddlewaretoken}

        page = self.do_request(url=self.login_url, data=login_data)
        print page
        # FIXME Try save cookies
        self.cookies.save(filename=COOKIE_FILENAME, ignore_discard=True)

    @property
    def is_login(self):
        return True

    # to find out the difference between decorators order
    @authenticated
    @property
    def username(self):
        """
        get leetcode username
        :return:
        """
        return None
