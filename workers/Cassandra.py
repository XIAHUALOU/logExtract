# -*- encoding: utf-8 -*-
from .Basewoker import BaseWorker


class Cassandra(BaseWorker):
    def run(self):
        logs = self.read_from_file(mode=list)
        # print(logs)
        for log in logs:
            t, log = log
            s1_list = []
            s2_list = []
            patt = r'Op rate|Latency mean'
            pattern = self.re.compile(patt)
            test_list = []
            s1_list = []
            s2_list = []
            for line in log:
                result = self.re.findall(pattern, line)
                if (result):
                    test_list.append(line.split()[3])
                s1_list=test_list[:14]
                s2_list=test_list[16:]
            self.merge(s1_list)
            self.merge(s2_list)
            self.status(t)

    def to_excel(self):
        pass
