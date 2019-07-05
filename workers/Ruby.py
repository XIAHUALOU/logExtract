# -*- encoding: utf-8 -*-
from .Basewoker import BaseWorker

class Ruby(BaseWorker):
    def run(self):
        logs = self.read_from_file(mode=list) 
        for log in logs:
            t, log = log    
            pattern_r=self.re.compile(r' s -  ')
            test_list=[]
            for line in log:
                target=self.re.findall(pattern_r,line)
                if(target):
                    test_list.append(line)
            list1=[]
            list2=[]
            #print(test_list)
            for each in test_list:
                s1=each.split(' s -')[0]
                list1.append(s1[:-7])
                list2.append(s1[-7:])
            s1=self.pd.Series(self.np.array(list1))
            s2=self.pd.Series(self.np.array(list2))
            df=self.pd.DataFrame({"name":s1,"result":s2})
            miss_list=['so_k_nucleotidepreparing /tmp/fasta.output.100000','so_reverse_complementpreparing /tmp/fasta.output.2500000']
            df['name'][111]=miss_list[0]
            df['name'][124]=miss_list[1]
            df['name'][393]=miss_list[0]
            df['name'][406]=miss_list[1]
            df1=df[:282]
            df2=df[282:]
            df1_copy=df1.drop_duplicates(subset='name', keep='last', inplace=False)
            df2_copy=df2.drop_duplicates(subset='name', keep='last', inplace=False)
            res_ruby=self.pd.DataFrame(columns=["score1","score2"],index=df2["name"].unique())
            list1=list(df1_copy["result"])
            list2=list(df2_copy["result"])
            res_ruby["score1"]=list1
            res_ruby["score2"]=list2
            #print(list1)
            self.merge(list1)
            self.merge(list2)
            self.status(t)   
                
        




            

    def to_excel(self):
        pass
