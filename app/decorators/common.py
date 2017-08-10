# coding=utf-8
import time


def timing_function(some_function):
    """
    Outputs the time a function takes to execute
    :param some_function:
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        res = some_function(*args, **kwargs)
        end = time.time()
        """worker runtime log """
        print "[" + some_function.__name__ + "] Time it took to run the function: " + str((end - start)) + "\n"
        return res

    return wrapper


def sleep_decorator(function):
    """
    Limits how fast the function is called.
    :param function:
    """

    def wrapper(self, *args, **kwargs):
        time.sleep(2)
        return function(self, *args, **kwargs)

    return wrapper
