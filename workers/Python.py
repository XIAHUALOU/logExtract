# -*- encoding: utf-8 -*-
"""
@Time    : 7/1/19 1:26 AM
@Author  : xiahaulou
@Email   : 390306467@qq.com
"""
from .Basewoker import BaseWorker


class Python(BaseWorker):
    def run(self):
        logs = self.read_from_file(mode=list)
        for log in logs:
            t, log = log
            try:
                for _ in log:
                    v = _.strip()
                    if v.startswith('Totals:'):
                        v = v.split()[1:3]
                        v = [_[:-2] for _ in v]
                        self.merge(v)
                self.status(t)
            except Exception as Ex:
                self.failed(t, Ex)
                continue

    def to_excel(self):
        pass
