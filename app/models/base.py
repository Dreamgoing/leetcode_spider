# coding=utf-8

import requests

from app.settings import URL_BASE, HEADERS_BASE
from app.utils import beautiful_soup


class Model(requests.Session):
    def __init__(self):
        super(Model, self).__init__()

    @property
    def csrfmiddlewaretoken(self):
        this_url = URL_BASE + '/accounts/login/'
        page = self.get(url=this_url, headers=HEADERS_BASE)
        soup = beautiful_soup(page)
        return soup.find('input', attrs={'name': 'csrfmiddlewaretoken'})['value']
    