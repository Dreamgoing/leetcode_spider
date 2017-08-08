# coding=utf-8
class LeetcodeBaseError(Exception):
    pass


class AccountError(Exception):
    """
    AccountError base
    """


class SubmissionError(Exception):
    """
    SubmissionError base
    """


class SubmissionInfoError(SubmissionError):
    """
    SubmissionInfo not match
    """


class AuthenticationFailed(AccountError):
    """
    Authentication failed
    """
