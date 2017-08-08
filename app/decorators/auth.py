# coding=utf-8
import requests
import requests.utils

from app.error import AuthenticationFailed


def authenticated(func):
    """
    user login decorator
    :param func:
    :return:
    """

    def wrapper(self, *args, **kwargs):
        # FIXME , authentication error
        # if 'messages' not in requests.utils.dict_from_cookiejar(self.cookie):
        #     """judge cookie is not existed and valid"""
        #     raise AuthenticationFailed()
        return func(self, *args, **kwargs)

    return wrapper
