# -*- encoding: utf-8 -*-
from .Basewoker import BaseWorker


class Ruby(BaseWorker):
    def run(self):
        logs = self.read_from_file(mode=list)
        for log in logs:
            t, log = log
            pattern_r = self.re.compile(r' s -  ')
            test_list = []
            list1 = []
            list2 = []
            for line in log:
                target = self.re.findall(pattern_r, line)
                if (target):
                    test_list.append(line)
            for each in test_list:
                s1 = each.split(' s -')[0]
                list1.append(s1[:-7])
                list2.append(s1[-7:])
            s1 = self.pd.Series(self.np.array(list1))
            s2 = self.pd.Series(self.np.array(list2))
            df = self.pd.DataFrame({"name": s1, "result": s2})
            miss_list = ['so_k_nucleotidepreparing /tmp/fasta.output.100000',
                         'so_reverse_complementpreparing /tmp/fasta.output.2500000']
            for tup in [(111, 0), (124, 1), (393, 0), (406, 1)]:
                df['name'][tup[0]] = miss_list[tup[1]]
            df1, df2 = df[:282], df[282:]
            df1_copy = df1.drop_duplicates(subset='name', keep='last', inplace=False)
            df2_copy = df2.drop_duplicates(subset='name', keep='last', inplace=False)
            list1 = list(df1_copy["result"])
            list2 = list(df2_copy["result"])
            self.merge(list1)
            self.merge(list2)
            self.status(t)

    def to_excel(self):
        pass
