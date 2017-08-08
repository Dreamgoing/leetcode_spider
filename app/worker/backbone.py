# coding=utf-8
import time

import multiprocessing as mp

from app.models.submission import Submission


def down_task():
    sub = Submission()
    print sub.cookies
    submissions = sub.get_accepted_list()
    # print submissions, type(submissions)

    t1 = time.time()
    for info in submissions:
        if info['status_display'] == 'Accepted':
            # pn = mp.Process(target=sub.download_specific_solution(info))
            # pn.start()
            sub.download_specific_solution(info)
    t2 = time.time()
    print t2-t1
            # print sub.cookies
            # submissions = sub.get_accepted_list()
