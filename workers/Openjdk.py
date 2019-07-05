# -*- encoding: utf-8 -*-
from .Basewoker import BaseWorker

class Openjdk(BaseWorker):
    def run(self):
        logs = self.read_from_file(mode=list)
        for log in logs:
            t, log = log
            patt=r'Score'
            pattern = self.re.compile(patt)
            test_list=[]
            for line in log:
                result = self.re.findall(pattern,line)
                if(result):
                    test_list.append(log[log.index(line)+1])
            s1_list=[]
            s2_list=[]
            s1_list.append(test_list[0].split()[3])
            s1_list.append(test_list[0].split()[5])
            s2_list.append(test_list[1].split()[3])
            s2_list.append(test_list[1].split()[5])
            self.merge(s1_list)
            self.merge(s2_list)
            self.status(t)
        




            

    def to_excel(self):
        pass
