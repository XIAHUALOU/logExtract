# -*- encoding: utf-8 -*-
from .Basewoker import BaseWorker


class Openjdk(BaseWorker):
    s3_list = []

    def run(self):
        logs = self.read_from_file(mode=list)
        for log in logs:
            t, log = log
            try:
                patt = r'Score'
                pattern = self.re.compile(patt)
                test_list = []
                s1_list = []
                s2_list = []
                for line in log:
                    result = self.re.findall(pattern, line)
                    if (result):
                        test_list.append(log[log.index(line) + 1])
                list(map(lambda x: s1_list.append(test_list[0].split()[x]), [3, 5]))
                list(map(lambda x: s2_list.append(test_list[1].split()[x]), [3, 5]))
                if len(test_list) == 3:
                    list(map(lambda x: self.s3_list.append(test_list[2].split()[x]), [3, 5]))
                if len(s1_list) != 2 or len(s2_list) != 2:
                    self.failed(t, 'error logfile')
                    self.merge(None)
                    continue
                self.merge(s1_list)
                self.merge(s2_list)
                self.status(t)
            except Exception as Ex:
                self.failed(t, Ex)
                self.merge(None)
                continue

    def to_excel(self):
        pass
