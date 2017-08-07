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
        success = False
        if 'cookie' in requests.utils.dict_from_cookiejar(self.cookie):
            """judge cookie is existed and valid"""

        """输入account代码"""

