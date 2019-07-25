# -*- encoding: utf-8 -*-
"""
@Time    : 7/2/19 1:56 AM
@Author  : xiahaulou
@Email   : 390306467@qq.com
"""
from .Basewoker import BaseWorker


class Mariadb(BaseWorker):
    def run(self):
        logs = self.read_from_file(mode=list)
        for log in logs:
            t, log = log
            try:
                package = []
                for _ in log:
                    if _.strip("\t").startswith("Average number of seconds to run all queries:"):
                        package.append(_.split()[-2])
                    if _.strip("\t").startswith("Minimum number of seconds to run all queries:"):
                        package.append(_.split()[-2])
                    if _.strip("\t").startswith("Maximum number of seconds to run all queries:"):
                        package.append(_.split()[-2])
                if len(package) != 6:
                    self.failed(t,'error log')
                    continue
                self.merge(package[0:3])
                self.merge(package[3:6])
                self.status(t)
            except Exception as Ex:
                self.failed(t, Ex)
                continue

    def to_excel(self):
        pass
