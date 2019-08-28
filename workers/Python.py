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
            _b = 0
            try:
                official = []
                clear = []
                for _ in log:
                    v = _.strip()
                    if v.startswith('Totals:'):
                        _b += 1
                        v = v.split()[1:3]
                        v = [_[:-2] for _ in v]
                        if len(official) == 0 and len(clear) == 0 and len(v) == 2:
                            official = v
                        if len(official) == 2 and len(clear) == 0 and len(v) == 2:
                            clear = v
                if len(official) == len(clear) == 2:
                    self.merge(official)
                    self.merge(clear)
                else:
                    self.failed(t, 'error logfile')
                    self.merge(None)
                    continue
                if _b != 2:
                    self.failed(t, 'error logfile')
                    self.merge(None)
                    continue
                else:
                    self.status(t)
            except Exception as Ex:
                self.failed(t, Ex)
                self.merge(None)
                continue
