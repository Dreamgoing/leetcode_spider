# coding=utf-8
import json
import os
import re
import requests

from config import BASE_PATH
from app.settings import URL_SUBMISSION_HISTORY, SOLUTION_DIRNAME, URL_BASE
from app.models.base import Model
from app.decorators.auth import authenticated
from app.utils import beautiful_soup, write_file, mkdir
from app.error import SubmissionInfoError
from app.settings import SOLUTION_PATH, LANG_MAPPING


# TODO to support args validator
class Submission(Model):
    def __init__(self):
        super(Submission, self).__init__()

    @authenticated
    def get_accepted_list(self):
        """
        :return: list(dict): each submission info
        """
        url = URL_SUBMISSION_HISTORY
        submissions_page = self.do_request(method='get', url=url)
        submissions = json.loads(submissions_page.text)['submissions_dump']
        return submissions

    @authenticated
    def download_all_solution(self, accepted=True):
        """

        :param accepted: True is to download all accepted solution
        :return:
        """
        submissions = self.get_accepted_list()
        directory = os.path.join(BASE_PATH, SOLUTION_DIRNAME)

    @authenticated
    def download_specific_solution(self, submission_info):
        """
        download one submission
        :param submission_info: Dict contains one submission info
        :return:
        """
        url = self.gen_submission_url(submission_info)
        solution_page = self.do_request(method='get', url=url)
        soup = beautiful_soup(solution_page.text)

        # hard code
        regex = re.compile('submissionCode: \'(.*?)\'', re.MULTILINE | re.UNICODE)

        submission_code = regex.search(soup.text)
        json_txt = '"' + submission_code.group(1) + '"'
        code = json.loads(json_txt)
        source_path = os.path.join(self.gen_source_directory(submission_info), self.gen_source_name(submission_info))
        print '[Download...] ' + self.gen_source_name(submission_info)
        write_file(source_path, code)

    @staticmethod
    def gen_submission_url(submission_info):
        """
        :return: url: submission detail url such as 'https://leetcode.com/submissions/#/<id>'
        """
        if 'status_display' in submission_info:
            url = URL_BASE + submission_info['url']
        else:
            raise SubmissionInfoError()
        return url

    @staticmethod
    def gen_source_name(submission_info):
        """
        :return: solution source name such as 'TwoSum.cpp' , 'QuickSort.py', etc
        """
        if 'title' not in submission_info or 'lang' not in submission_info:
            raise SubmissionInfoError()
        title = submission_info['title']
        lang = submission_info['lang']
        return "".join(title.split(' ')) + LANG_MAPPING[lang]

    @staticmethod
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

    @staticmethod
    def write_source_file(directory, name, content):
        write_file(os.path.join(directory, name), content)
