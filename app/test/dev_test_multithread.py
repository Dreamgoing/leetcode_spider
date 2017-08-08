# coding=utf-8

import requests

from multiprocessing.dummy import Pool as ThreadPool
from app.worker.backbone import down_task

pool = ThreadPool(4)


if __name__ == '__main__':
    down_task()
