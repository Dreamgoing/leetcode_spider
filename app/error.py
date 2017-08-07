# coding=utf-8
class LeetcodeBaseError(Exception):
    pass


class LoginError(Exception):
    """
    LoginError base
    """


class SubmissionError(Exception):
    """
    SubmissionError base
    """


class SubmissionInfoError(SubmissionError):
    """
    SubmissionInfo not match
    """
