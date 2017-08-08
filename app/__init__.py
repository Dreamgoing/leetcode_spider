# coding=utf-8
from flask import Flask
from .crawler import Crawler

# TODO 设置合理的代码结构, 可以参考zhihu api或者 requests库, 进行设计, 添加manager.py
crawler = Crawler()


def configure_foundations(app):
    """app foundation configuration"""


def configure_blueprint(app):
    app.register_blueprint()


def configure_middleware(app):
    app.wsgi_app = None


def create_app(config_name='config'):
    app = Flask(__name__, template_folder='templates', static_folder='static')
    """do app configuration"""
    return app
