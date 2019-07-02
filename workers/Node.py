# -*- encoding: utf-8 -*-
"""
@Time    : 7/2/19 1:56 AM
@Author  : xiahaulou
@Email   : 390306467@qq.com
"""
from .Basewoker import BaseWorker


class Node(BaseWorker):
    def run(self):
        logs = self.read_from_file(mode=list)
        for log in logs:
            t, log = log
            scores = []
            for _ in log:
                if _.startswith("Score (version"):
                    scores.append(_.split()[-1])
            self.merge([scores[0]])
            self.merge([scores[1]])
            self.status(t)

    def to_excel(self):
        pass
