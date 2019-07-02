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
            package = []
            for _ in log:
                if _.strip("\t").startswith("Average number of seconds to run all queries:"):
                    package.append(_.split()[-2])
                if _.strip("\t").startswith("Minimum number of seconds to run all queries:"):
                    package.append(_.split()[-2])
                if _.strip("\t").startswith("Maximum number of seconds to run all queries:"):
                    package.append(_.split()[-2])
            df = self.pd.DataFrame([package[0:3], package[3:6]]).T
            self.to_csv(t, df)
            self.status(t)

    def to_excel(self):
        pass
