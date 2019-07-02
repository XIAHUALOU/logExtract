# -*- encoding: utf-8 -*-
"""
@Time    : 7/1/19 1:26 AM
@Author  : xiahaulou
@Email   : 390306467@qq.com
"""
from .basewoker import BaseWorker


class Python(BaseWorker):
    def run(self):
        print("Python")

    def to_excel(self):
        pass
