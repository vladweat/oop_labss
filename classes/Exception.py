from datetime import date


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
