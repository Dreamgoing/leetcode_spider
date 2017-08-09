# coding: utf-8

import inspect
import collections


def is_generator(obj):
    """Return True if ``obj`` is a generator
    """
    return inspect.isgeneratorfunction(obj) or inspect.isgenerator(obj)


def is_iterable_but_not_string(obj):
    """Return True if ``obj`` is an iterable object that isn't a string."""
    return (
        (isinstance(obj, collections.Iterable) and not hasattr(obj, "strip")) or is_generator(obj)
    )


def get_function(instance, func_name):
    if isinstance(func_name, basestring):
        func = getattr(instance, func_name)
        if not func:
            raise ValueError("`{}` must be method name of class {}".format(func_name, instance.__class__.__name__))
    else:
        func = func_name
    if not callable(func):
        raise ValueError("Parameter {} must be callable".format(func_name))
    return func
