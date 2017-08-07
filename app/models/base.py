# coding=utf-8
from cookielib import LWPCookieJar

import requests

from app.settings import URL_BASE, HEADERS_BASE, COOKIE_FILENAME
from app.utils import beautiful_soup


class Model(requests.Session):
    def __init__(self):
        super(Model, self).__init__()
        self.cookies = LWPCookieJar(filename=COOKIE_FILENAME)
        self.headers = HEADERS_BASE

    def do_request(self, method='post', url=None, parms=None, json=None, data=None, **kwargs):
        return getattr(self, method)(url, parms=parms, json=json, data=data, **kwargs)

    @property
    def csrfmiddlewaretoken(self):
        this_url = URL_BASE + '/accounts/login/'
        page = self.get(url=this_url, headers=HEADERS_BASE)
        soup = beautiful_soup(page)
        return soup.find('input', attrs={'name': 'csrfmiddlewaretoken'})['value']