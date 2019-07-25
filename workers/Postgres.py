# -*- encoding: utf-8 -*-
"""
@Time    : 7/2/19 2:05 AM
@Author  : xiahaulou
@Email   : 390306467@qq.com
"""
from .Basewoker import BaseWorker


class Postgres(BaseWorker):
    def run(self):
        logs = self.read_from_file(mode=list)
        container = []
        for log in logs:
            t, log = log
            try:
                for _ in log:
                    if _.strip().endswith("(excluding connections establishing)"):
                        container.append(_.strip().split()[2])
                if len(container) != 12:
                    self.failed(t, 'error logfile')
                    self.merge(None)
                    continue
                self.merge(container[0:6])
                self.merge(container[6:12])
                self.status(t)
            except Exception as Ex:
                self.failed(t, Ex)
                continue

    def to_excel(self):
        pass
