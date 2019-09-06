# -*- encoding: utf-8 -*-
from .Basewoker import BaseWorker


class Memcached(BaseWorker):
    def run(self):
        logs = self.read_from_file(mode=list)
        # print(logs)
        for log in logs:
            t, log = log
            try:
                res = []
                s1_list = []
                s2_list = []
                index_list = [i for i, x in enumerate(log) if x.find("Ops/sec") != -1]
                list(map(lambda x: res.append(x), [log[index_list[0] + _] for _ in range(2, 6)]))
                list(map(lambda x: res.append(x), [log[index_list[1] + _] for _ in range(2, 6)]))

                list(map(lambda x: s1_list.append(res[x[0]].split()[x[1]]),
                         [(0, 4), (0, 5), (1, 4), (1, 5), (3, 4), (3, 5)]))
                list(map(lambda x: s2_list.append(res[x[0]].split()[x[1]]),
                         [(4, 4), (4, 5), (5, 4), (5, 5), (7, 4), (7, 5)]))
                if len(s1_list) != 6 or len(s2_list) != 6:
                    self.failed(t, 'error logfile')
                    self.merge(None)
                    continue
                self.merge(s1_list)
                self.merge(s2_list)
            except Exception as Ex:
                self.failed(t, Ex)
                self.merge(None)
                continue
