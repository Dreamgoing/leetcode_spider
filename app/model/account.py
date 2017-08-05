import logging
import re

from app.settings import URL_BASE, HEADERS_BASE
from app.model.base import Model


class Account(Model):
    login_url = URL_BASE + '/accounts/login/'

    def __init__(self, account, password):
        super(Account, self).__init__()
        self.account = account
        self.password = password

    def login(self):
        """
        user login
        :param account: email
        :param password:
        :return:
        """
        login_data = {'login': self.account,
                      'password': self.password,
                      'csrfmiddlewaretoken': self.csrfmiddlewaretoken}

        self.post(self.login_url, headers=HEADERS_BASE, data=login_data)

    @property
    def username(self):
        """
        get leetcode username
        :return:
        """
        return None
