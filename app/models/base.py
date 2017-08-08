# coding=utf-8
from cookielib import LWPCookieJar

import requests

from app.settings import URL_BASE, HEADERS_BASE, COOKIE_FILENAME, COOKIE_PATH
from app.utils import beautiful_soup


class Model(requests.Session):
    def __init__(self):

        super(Model, self).__init__()

        self.cookies = LWPCookieJar(filename=COOKIE_PATH)
        try:
            """load cookie from Cookiejar"""
            self.cookies.load(ignore_discard=True)
        except Exception as e:
            print e
        self.headers = HEADERS_BASE
        self.post(URL_BASE)

    def do_request(self, method='post', url=None, json=None, data=None, **kwargs):
        return getattr(self, method)(url, json=json, data=data, **kwargs)

    @property
    def csrfmiddlewaretoken(self):
        this_url = URL_BASE + '/accounts/login/'
        page = self.get(url=this_url, headers=HEADERS_BASE)
        soup = beautiful_soup(page.text)
        return soup.find('input', attrs={'name': 'csrfmiddlewaretoken'})['value']
