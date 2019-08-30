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
            box = []
            try:
                for _ in log:
                    v = _.strip()
                    if v.startswith('Totals:'):
                        v = v.split()[1:3]
                        v = [_[:-2] for _ in v]
                        box.extend(v)
                if len(box) != 4:
                    self.failed(t, 'error logfile')
                    self.merge(None)
                    continue
                else:
                    self.merge(box[0:2])
                    self.merge(box[2:4])
                    self.status(t)
            except Exception as Ex:
                self.failed(t, Ex)
                self.merge(None)
                continue

    def to_excel(self):
        pass
