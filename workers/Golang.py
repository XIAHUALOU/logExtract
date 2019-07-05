# -*- encoding: utf-8 -*-
from .Basewoker import BaseWorker

class Golang(BaseWorker):
    def run(self):
        logs = self.read_from_file(mode=list)
        for log in logs:
            t, log = log
            patt=r'BenchmarkBuild|BenchmarkGarbage|BenchmarkHTTP|BenchmarkJSON'
            pattern = self.re.compile(patt)
            test_list=[]
            for line in log:
                result = self.re.findall(pattern,line)
                if(result):
                    test_list.append(line)
            s1_list=[]
            s2_list=[]
            s1_list.append(test_list[0].split()[2])
            s1_list.append(test_list[1].split()[2])
            s1_list.append(test_list[2].split()[2])
            s1_list.append(test_list[3].split()[2])
            s2_list.append(test_list[4].split()[2])
            s2_list.append(test_list[5].split()[2])
            s2_list.append(test_list[6].split()[2])
            s2_list.append(test_list[7].split()[2])
            self.merge(s1_list)
            self.merge(s2_list)
            self.status(t)

    def to_excel(self):
        pass
