import abc
import pandas as pd
import numpy as np
import re
import time
import os


class BaseWorker(metaclass=abc.ABCMeta):
    def __init__(self):
        self.pd = pd
        self.np = np
        self.re = re

    @abc.abstractclassmethod
    def run(self):
        pass

    @abc.abstractclassmethod
    def read_from_file(self):
        pass

    @abc.abstractclassmethod
    def to_excel(self):
        pass

    @staticmethod
    def swap(*args):
        data, pos_one, pos_two = args
        temp = data[pos_one]
        data[pos_one] = data[pos_two]
        data[pos_two] = temp

    @staticmethod
    def now():
        return time.strftime("%Y%m%d", time.localtime())

    def to_csv(self, df):
        df.to_csv(os.path.join(os.getcwd(), 'data/csv/{}{}.csv'.format(type(self).__name__.lower(), BaseWorker.now())),
                  index=None, header=None, encoding='utf-8')

    def read_from_file(self):
        logs = []
        path = os.listdir(os.path.join(os.getcwd(), 'data/log'))
        path = [os.path.join(os.getcwd(), 'data/log/{}'.format(_)) for _ in path if
                _.startswith(type(self).__name__.lower())]
        try:
            for _ in path:
                with open(_, 'r') as f:
                    logs.append(f.readlines())
        except Exception as Ex:
            print(Ex)
        return logs
