# coding=utf-8

import requests

from multiprocessing.dummy import Pool as ThreadPool
from app.worker.backbone import download_all_submission

pool = ThreadPool(4)


if __name__ == '__main__':
    download_all_submission()
