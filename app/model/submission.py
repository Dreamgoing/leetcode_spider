# coding=utf-8

import requests

from app.settings import URL_BASE, HEADERS_BASE
from app.model.base import Model

class Submission(Model):
    def __init__(self):
        super(Model, self).__init__()
