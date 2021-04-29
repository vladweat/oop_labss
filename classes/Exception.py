from datetime import *


class CheckingDate(object):
    """Class CheckingDate represent validation check of date"""

    def __init__(self):
        self.maxdate = date.today()

    def __get__(self, instance, cls):
        return instance._date

    def __set__(self, instance, value):
        if self.maxdate < value:
            instance._date = self.maxdate
        else:
            instance._date = value


class CheckingPrice(object):
    """Class CheckingDate represent validation check of positive price"""

    def __init__(self):
        self.min_price = 0

    def __get__(self, instance, cls):
        return instance._price

    def __set__(self, instance, value):
        if self.min_price > value:
            instance._price = self.min_price
        else:
            instance._price = value


class Log(object):
    def __init__(self, func):
        self.func = func
        print('call func {0}'.format(func.__name__))

    def __call__(self, *args, **kwargs):
        print('args {0}'.format(args))
        print('kwargs {0}'.format(kwargs))


class LogTime(object):
    def __init__(self, func):
        self.func = func
        print('call func {0}'.format(func.__name__))

    def __call__(self, *args, **kwargs):
        print(f'call time: {datetime.now()}')