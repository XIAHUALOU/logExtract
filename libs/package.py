# -*- encoding: utf-8 -*-
"""
@Time    : 7/1/19 1:26 AM
@Author  : xiahaulou
@Email   : 390306467@qq.com
"""
import configparser
import os


class ConfigPaser:
    def __init__(self, encoding="utf-8"):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(os.path.dirname(__file__)[:-5], 'config.ini'), encoding=encoding)

    def __getitem__(self, item):
        return self.config.options(item)

    @property
    def workers(self):
        if len(self.config.options("workers")) > 0:
            return self.config.get("workers", "images").split(',')
        return []

    @property
    def sections(self):
        return self.config.sections()

    @property
    def current_thread(self):
        pass
        return
