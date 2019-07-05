# -*- encoding: utf-8 -*-
from .Basewoker import BaseWorker

class Perl(BaseWorker):
    def run(self):
        logs = self.read_from_file(mode=list)
        for log in logs:
            t, log = log
            patt=r'Avg'
            pattern = self.re.compile(patt)
            test_list=[]
            for line in log:
                result = self.re.findall(pattern,line)
                if(result):
                    test_list.append(line) 
            s1_list=[]
            s2_list=[]
            s1_list.append(test_list[0].split()[1])
            s1_list.append(test_list[1].split()[1])
            s2_list.append(test_list[2].split()[1])
            s2_list.append(test_list[3].split()[1])
            self.merge(s1_list)
            self.merge(s2_list)
            self.status(t)
        




            

    def to_excel(self):
        pass
