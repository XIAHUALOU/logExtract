# -*- encoding: utf-8 -*-
from .Basewoker import BaseWorker


class Openjdk(BaseWorker):
    s3_list = []

    def run(self):
        logs = self.read_from_file(mode=list)
        for log in logs:
            t, log = log
            try:
                test_list = []
                s1_list = []
                s2_list = []
                index_list = [i for i, x in enumerate(log) if x.find("Score error") != -1]
                list(map(lambda x: s1_list.append(log[index_list[0] + 1].split()[x]), [3, 4]))
                list(map(lambda x: s2_list.append(log[index_list[1] + 1].split()[x]), [3, 4]))
                if len(test_list) == 3:
                    list(map(lambda x: self.s3_list.append(test_list[2].split()[x]), [3, 4]))
                if len(s1_list) != 2 or len(s2_list) != 2:
                    self.failed(t, 'error logfile')
                    self.merge(None)
                    continue
                self.merge(s1_list)
                self.merge(s2_list)
            except Exception as Ex:
                self.failed(t, Ex)
                self.merge(None)
                continue

    def to_excel(self):
        pass

