# coding=utf-8

import requests
import requests.utils


def authenticated(func):
    """
    user login decorator
    :param func:
    :return:
    """
    def wrapper(self, *args, **kwargs):
        pass
