# -*- encoding: utf-8 -*-
from .Basewoker import BaseWorker

class Memcached(BaseWorker):
    def run(self):
        logs = self.read_from_file(mode=list)
        #print(logs)
        for log in logs:
            t, log = log
            patt=r'Ops/sec'
            pattern = self.re.compile(patt)
            res=[]
            index_list=[i for i,x in enumerate(log) if x.find("Ops/sec")!=-1]
            res.append(log[index_list[0]+2])  
            res.append(log[index_list[0]+3])  
            res.append(log[index_list[0]+4])  
            res.append(log[index_list[0]+5])    
            res.append(log[index_list[1]+2])  
            res.append(log[index_list[1]+3])  
            res.append(log[index_list[1]+4])  
            res.append(log[index_list[1]+5])
            # #print(res)
            s1_list=[]
            s2_list=[]
            s1_list.append(res[0].split()[4])
            s1_list.append(res[0].split()[5])
            s1_list.append(res[1].split()[4])
            s1_list.append(res[1].split()[5])
            s1_list.append(res[3].split()[4])
            s1_list.append(res[3].split()[5])
            s2_list.append(res[4].split()[4])
            s2_list.append(res[4].split()[5])
            s2_list.append(res[5].split()[4])
            s2_list.append(res[5].split()[5])
            s2_list.append(res[7].split()[4])
            s2_list.append(res[7].split()[5])
            self.merge(s1_list)
            self.merge(s2_list)
            self.status(t)
        


            

    def to_excel(self):
        pass
