# coding=utf-8
import json
import os
import re
import time

import multiprocessing
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import threading

import requests as requests

from app.error import SubmissionInfoError
from app.models.submission import Submission
from app.decorators.common import timing_function
from app.settings import URL_BASE, LANG_MAPPING, SOLUTION_PATH

# multiprocessing 150s , one process 188s, multi thread 100s
from app.utils import beautiful_soup, mkdir

sub = Submission()


def func(x):
    for i in range(1000):
        tmp = i * i * i
    print x['title']


def gen_submission_url(submission_info):
    """
    :return: url: submission detail url such as 'https://leetcode.com/submissions/#/<id>'
    """
    if 'status_display' in submission_info:
        url = URL_BASE + submission_info['url']
    return url


def gen_source_name(submission_info):
    """
    :return: solution source name such as 'TwoSum.cpp' , 'QuickSort.py', etc
    """
    if 'title' not in submission_info or 'lang' not in submission_info:
        raise SubmissionInfoError()
    title = submission_info['title']
    lang = submission_info['lang']
    return "".join(title.split(' ')) + LANG_MAPPING[lang]


def gen_source_directory(submission_info):
    """
    if submission directory not exist create directory
    """
    if 'title' not in submission_info:
        raise SubmissionInfoError()
    title = submission_info['title']
    dirname = "".join(title.split(' '))
    path = os.path.join(SOLUTION_PATH, dirname)
    mkdir(path)
    return path


def download_specific_solution(info):
    url = gen_submission_url(info)
    print '*', url
    solution_page = sub.do_request(method='get', url=url)
    print solution_page.status_code
    regex = re.compile('submissionCode: \'(.*?)\'', re.MULTILINE | re.UNICODE)

    soup = beautiful_soup(solution_page.text)
    submission_code = regex.search(soup.text)
    json_txt = '"' + submission_code.group(1) + '"'
    code = json.loads(json_txt)
    source_path = os.path.join(gen_source_directory(info), gen_source_name(info))
    print 'Download: ' + source_path
    return {source_path: code}


# TODO select epoll
@timing_function
def get_all_accepted_task():
    submissions = sub.get_accepted_list()
    print submissions
    accepted = []
    for info in submissions:
        if info['status_display'] == u'Accepted':
            # pn = mp.Process(target=sub.download_specific_solution(info))
            # pn.start()
            # sub.download_specific_solution(info)
            # tn = threading.Thread(target=sub.download_specific_solution(info))
            # tn.start()
            accepted.append(info)

            # pool.apply_async(sub.download_specific_solution, args=(info,))
    # pool.map(func, accepted)
    # pool.join()
    # print sub.cookies
    # submissions = sub.get_accepted_list()
    return accepted


# 多进程会失败
# NOTE 这样测试不太好, 需要进行认证
if __name__ == '__main__':
    # pool = Pool(4)
    # 可以设计成为一个经典的生产者消费者模型
    # 多线程池使用了34.53405s
    thread_pool = ThreadPool(20)
    accept_list = get_all_accepted_task()
    download_specific_solution(accept_list[0])
    st1 = time.time()
    results = thread_pool.map(download_specific_solution, accept_list)
    thread_pool.close()
    thread_pool.join()
    st2 = time.time()
    print 'thread_pool using ' + str(st2 - st1) + 's'
    print results

    # 单一线程使用了193.239053s
    st1 = time.time()
    for it in accept_list:
        download_specific_solution(it)
    st2 = time.time()
    print 'single_thread using' + str(st2 - st1) + 's'



    # pool.map(download_specific_solution, accept_list)
    # pool.join()
