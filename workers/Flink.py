# -*- encoding: utf-8 -*-
from .Basewoker import BaseWorker


class Flink(BaseWorker):
    def run(self):
        logs = self.read_from_file(mode=list)
        for log in logs:
            t, log = log
            try:
                s1_list = []
                s2_list = []
                index_list = [i for i, x in enumerate(log) if x.find("(stateBackend)") != -1]
                for i in range(1, 23):
                    s1_list.append(log[index_list[0] + i].split()[5])
                    s2_list.append(log[index_list[1] + i].split()[5])
                if len(s1_list) != 22 or len(s2_list) != 22:
                    self.failed(t, 'error logfile')
                    self.merge(None)
                    continue
                self.merge(s1_list)
                self.merge(s2_list)
            except Exception:
                self.failed(t, 'error logfile')
                self.merge(None)
                continue