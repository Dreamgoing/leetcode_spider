# coding=utf-8
import os

from bs4 import BeautifulSoup


def beautiful_soup(html_doc):
    return BeautifulSoup(html_doc, "html.parser")


def get_encoding_type(txt):
    if isinstance(txt, str):
        return 'ordinary string'
    elif isinstance(txt, unicode):
        return 'unicode'
    else:
        return type(txt)


def mkdir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def gen_code_name(title, lang):
    return "".join(title.split(' ')) + lang


def gen_file_path(directory, code_name):
    return os.path.join(directory, code_name)


def get_user_info():
    username = input('please input your username:')
    password = input('please input your password')
    return username, password
