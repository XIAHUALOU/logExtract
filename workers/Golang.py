# -*- encoding: utf-8 -*-
from .Basewoker import BaseWorker


class Golang(BaseWorker):
    def run(self):
        logs = self.read_from_file(mode=list)
        for log in logs:
            t, log = log
            try:
                patt = r'BenchmarkBuild|BenchmarkGarbage|BenchmarkHTTP|BenchmarkJSON'
                pattern = self.re.compile(patt)
                test_list = []
                for line in log:
                    result = self.re.findall(pattern, line)
                    if (result):
                        test_list.append(line)
                s1_list = []
                s2_list = []
                list(map(lambda x: s1_list.append(test_list[x].split()[2]), range(0, 4)))
                list(map(lambda x: s2_list.append(test_list[x].split()[2]), range(4, 8)))
                self.merge(s1_list)
                self.merge(s2_list)
                self.status(t)
            except Exception as Ex:
                self.failed(t, Ex)
                continue

    def to_excel(self):
        pass
