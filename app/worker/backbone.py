# coding=utf-8
import time

import multiprocessing as mp
import threading

from app.models.submission import Submission


# multiprocessing 150s , one process 188s, multi thread 100s

def download_all_submission():
    sub = Submission()
    print sub.cookies
    submissions = sub.get_accepted_list()
    # print submissions, type(submissions)

    t1 = time.time()
    for info in submissions:
        if info['status_display'] == 'Accepted':
            pn = mp.Process(target=sub.download_specific_solution(info))
            pn.start()
            # sub.download_specific_solution(info)
            # tn = threading.Thread(target=sub.download_specific_solution(info))
            # tn.start()
    t2 = time.time()
    print t2 - t1
    # print sub.cookies
    # submissions = sub.get_accepted_list()
