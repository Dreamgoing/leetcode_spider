# coding=utf-8

import requests

from app.settings import URL_BASE, HEADERS_BASE
from app.models.base import Model
from app.decorators.auth import authenticated


class Submission(Model):
    def __init__(self):
        super(Model, self).__init__()

    def get_accepted_list(self):
        pass

    def download_all_solution(self):
        pass
