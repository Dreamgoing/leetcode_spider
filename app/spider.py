# coding=utf-8
import os
import json
import requests
import re
import io
import sys

from bs4 import BeautifulSoup

# 继续完善该项目 read the docs.io, to add multiprocessing
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "https://leetcode.com"

session = requests.session()
headers_base = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
    'Connection': 'keep-alive',
    'Host': 'leetcode.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Referer': 'https://leetcode.com/accounts/login/',
}
login_data = {}

LANG_MAPPING = {
    'python': '.py',
    'c++': '.cpp',
    'cpp': '.cpp',
    'golang': '.go',
    'mysql': '.sql'
}


def bs(html_doc):
    return BeautifulSoup(html_doc, "html.parser", from_encoding='uft-8')


def login():
    url = "https://leetcode.com/accounts/login/"
    res = session.get(url=url, headers=headers_base)
    soup = bs(res.text)

    print(soup.find('input', attrs={'name': 'csrfmiddlewaretoken'})['value'])
    csrfmiddlewaretoken = soup.find('input', attrs={'name': 'csrfmiddlewaretoken'})['value']

    print(res.cookies['csrftoken'])

    # csrfmiddlewaretoken 和 cookie都能正常工作
    login_data['csrfmiddlewaretoken'] = csrfmiddlewaretoken
    login_data['login'] = "786373153@qq.com"
    login_data['password'] = "wrx0831"
    res = session.post(url, headers=headers_base, data=login_data)


def is_login():
    url = "https://leetcode.com/profile/"
    headers_base['Referer'] = 'https://leetcode.com/dream_going/'
    res = session.get(url, headers=headers_base)
    return res.status_code == 200


def get_submissions():
    url = "https://leetcode.com/submissions/#/"
    page_num = 1
    page_url = url + str(page_num)


# python 3 均为unicode编码, 使用unicode-escape 将`\u000A转换正常`
def get_specific_solution(filename, url):
    page = session.get(url)
    soup = bs(page.text)
    regex = re.compile('submissionCode: \'(.*?)\'', re.MULTILINE | re.UNICODE)
    tmp = regex.search(soup.text)
    json_txt = '"' + tmp.group(1) + '"'
    j = json.loads(json_txt)
    print j
    with io.open(filename, 'w', encoding='utf8') as f:
        f.write(j)
        f.close()


def get_encoding_type(s):
    if isinstance(s, str):
        return 'ordinary string'
    elif isinstance(s, unicode):
        return 'unicode'
    else:
        return type(s)


def use_encoding():
    s = u'"蛋疼\\u000A egg烦"'
    print s.encode('ascii', 'ignore')
    print json.loads(s)
    j = json.loads(s)

    print type(s)
    b = s.replace('\\u000A', '\uOOOA')
    print b

    print s.encode('utf-8').decode('unicode-escape')
    print s


def get_problem_list():
    url = "https://leetcode.com/problemset/all/"
    page = session.get(url, headers=headers_base)
    # XHR json 所有提交题目的信息
    url = "https://leetcode.com/api/submissions/?offset=0&limit=1000"
    submission_page = session.get(url)
    submissions = json.loads(submission_page.text)['submissions_dump']
    return submissions
    # print soup.prettify()


def mkdir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def download_all_accept(submissions):
    directory = os.path.join(BASE_PATH, 'solution')
    mkdir(directory)
    for solution in submissions:
        if 'status_display' in solution:
            if solution['status_display'] == 'Accepted':
                accept_url = BASE_URL + solution['url']
                print accept_url
                title = gen_title(solution['title'], LANG_MAPPING[solution['lang']])
                filename = gen_filename(directory, title)
                get_specific_solution(filename, accept_url)


def gen_title(title, lang):
    return "".join(title.split(' ')) + lang


def gen_filename(directory, title):
    return os.path.join(directory, title)


if __name__ == '__main__':
    # print 'base', BASE_PATH
    print 'welcome!'
    login()
    print(is_login())
    s = get_problem_list()
    download_all_accept(s)
    # get_submissions()
    # get_specific_solution(112140249, 'test.cpp')
    # get_specific_solution(111855773, 'MergeTwoSortedLists.cpp')
    # use_encode()
    # use_encoding()
