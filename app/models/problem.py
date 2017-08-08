# coding=utf-8

from app.models.base import Model


# TODO to support crawler other interview problem and answer into markdown or pdf
class Problem(Model):
    """
    Problem model
    """

    def __init__(self):
        super(Model, self).__init__()

    @staticmethod
    def download_problem_description(self):
        """url: `https://leetcode.com/problems/multiply-strings/description` """
