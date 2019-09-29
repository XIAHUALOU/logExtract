# -*- encoding: utf-8 -*-
import workers
from libs import config
from openpyxl import load_workbook
import threading
import abc
import pandas as pd
import numpy as np
import re
import time
import os
import sys


class BaseWorker(metaclass=abc.ABCMeta):
    def __init__(self):
        self.pd = pd
        self.np = np
        self.re = re
        self.lock = threading.Lock()
        self.times = config.config.getint('test_times', 'times')
        self.containers = []

    @abc.abstractclassmethod
    def run(self):
        '''
        need each work rewrite this function
        :return:
        '''
        pass

    @staticmethod
    def swap(*args):
        '''
        :param args:list, index, index
        :return:
        '''
        data, pos_one, pos_two = args
        temp = data[pos_one]
        data[pos_one] = data[pos_two]
        data[pos_two] = temp


    @staticmethod
    def now():
        '''
        :return: return localtime
        '''
        return time.strftime("%Y%m%d", time.localtime())

    def to_csv(self, t, df):
        '''
        :param t: logfile name
        :param df: a dataframe
        :return:
        '''
        micro = type(self).__name__.lower()
        micro_path = os.path.join(os.getcwd(), 'data/csv/{}'.format(micro))
        if not os.path.exists(micro_path):
            os.mkdir(micro_path)
        df.to_csv(os.path.join(micro_path, '{}.csv'.format(t)),
                  index=None, header=None, encoding='utf-8')

    def __ajust_index(self, path):
        if len(path) < self.times:
            setattr(self, '{}_times'.format(type(self).__name__), len(path))
            return path[:len(path)]
        else:
            setattr(self, '{}_times'.format(type(self).__name__), self.times)
            return path[:self.times]

    @property
    def datest_logs(self):
        '''
        :return: if u set times = 5 in config.ini,it will return 5 datest logs for each worker,
        '''
        path = self.get_logfiles(os.path.join(os.getcwd(), 'data/log'), [])
        if sys.platform in ['win32', 'win64', 'cygwin']:
            path = [_ for _ in path if _.split('\\')[-1].startswith(type(self).__name__.lower()) and _.endswith(".log")]
            path = sorted(path, key=lambda s: s.split('\\')[-1], reverse=True)
            path = self.__ajust_index(path)
        else:
            path = [_ for _ in path if _.split('/')[-1].startswith(type(self).__name__.lower()) and _.endswith(".log")]
            path = sorted(path, key=lambda s: s.split('/')[-1], reverse=True)
            path = self.__ajust_index(path)
        return path

    def read_from_file(self, mode=list):
        '''
        :param mode: default return log content as f.readlines,if accept str,or strbytes return log content as f.read()
        :return:
        '''
        logs = []
        files = self.datest_logs
        try:
            for _ in files:
                with open(_, 'r', encoding='utf8') as f:
                    if sys.platform in ['win32', 'win64', 'cygwin']:
                        if mode is list:
                            logs.append((_, f.readlines()))
                        elif mode is str:
                            logs.append((_, f.read()))
                    else:
                        if mode is list:
                            logs.append((_, f.readlines()))
                        elif mode is str or isinstance(mode, str):
                            logs.append((_, f.read()))
        except Exception as Ex:
            print(Ex)
        return logs

    @classmethod
    def get_logfiles(cls, dir, fileList):
        '''
        :param dir: logfiles's path
        :param fileList: a empty list []
        :return:
        '''
        if os.path.isfile(dir):
            fileList.append(dir)
        elif os.path.isdir(dir):
            for s in os.listdir(dir):
                new_dir = os.path.join(dir, s)
                cls.get_logfiles(new_dir, fileList)
        return fileList

    def status(self, t):
        print('task {} done, Status:Success'.format(t))

    def failed(self, t, error):
        workers.task_status[t.lower()] = False
        _c = getattr(self, '{}_times'.format(type(self).__name__)) - 1
        setattr(self, '{}_times'.format(type(self).__name__), _c)
        print("task {}.log done Status: extract failed,Error: {}\n".format(t, error))

    def merge(self, data):
        '''
        generate csv files named by microservice name
        :param data: type list,docker official data or clear data
        :return:
        '''
        container_name = '{}_container'.format(type(self).__name__.lower())
        _container = getattr(self, container_name)
        _container.append(data)
        if _container[-1] is None:
            _container.pop()
        if len(_container) == getattr(self, '{}_times'.format(type(self).__name__)) * 2:
            ret_index_odd = []
            ret_index_even = []
            for _ in range(len(_container)):
                if _ % 2 == 0:
                    ret_index_even.append(_container[_])
                else:
                    ret_index_odd.append(_container[_])
            ret_index_even.extend(ret_index_odd)
            _container.clear()
            if ret_index_even:
                df = self.pd.DataFrame(ret_index_even).T
                self.D = df
                self.to_csv(type(self).__name__.lower(), df)
