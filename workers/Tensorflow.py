# -*- encoding: utf-8 -*-
"""
@Time    : 7/2/19 2:04 AM
@Author  : xiahaulou
@Email   : 390306467@qq.com
"""
from .Basewoker import BaseWorker


class Tensorflow(BaseWorker):
    def run(self):
        logs = self.read_from_file(mode=list)
        for log in logs:
            t, log = log
            try:
                container = []
                for _ in log:
                    if _.strip().startswith("Total duration:"):
                        container.append(_.strip().split()[-2])
                if len(container) != 2:
                    self.failed(t, 'error logfile')
                    self.merge(None)
                    continue
                self.merge([container[0]])
                self.merge([container[1]])
            except Exception as Ex:
                self.failed(t, Ex)
                self.merge(None)
                continue
