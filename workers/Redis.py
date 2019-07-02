# -*- encoding: utf-8 -*-
"""
@Time    : 7/1/19 1:26 AM
@Author  : xiahaulou
@Email   : 390306467@qq.com
"""
from .Basewoker import BaseWorker


class Redis(BaseWorker):
    def run(self):
        logs = self.read_from_file(mode=list)
        for log in logs:
            t, log = log
            official = []
            clear = []
            count = 0
            for _ in log:
                _r = _.strip()
                if _r.endswith("requests per second"):
                    if count < 18:
                        official.append(_r.split()[0])
                        count += 1
                    else:
                        clear.append(_r.split()[0])
                        count += 1
            self.merge(official)
            self.merge(clear)
            self.status(t)

    def to_excel(self):
        pass
