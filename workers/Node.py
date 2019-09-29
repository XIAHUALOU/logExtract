# -*- encoding: utf-8 -*-
from .Basewoker import BaseWorker


class Node(BaseWorker):
    def run(self):
        logs = self.read_from_file(mode=list)
        for log in logs:
            t, log = log
            try:
                scores = []
                for _ in log:
                    if _.startswith("Score (version"):
                        scores.append(_.split()[-1])
                if len(scores) != 2:
                    self.failed(t, 'error logfile')
                    self.merge(None)
                    continue
                self.merge([scores[0]])
                self.merge([scores[1]])
            except Exception as Ex:
                self.failed(t, Ex)
                self.merge(None)
                continue
