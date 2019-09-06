# -*- encoding: utf-8 -*-
from .Basewoker import BaseWorker


class Perl(BaseWorker):
    def run(self):
        logs = self.read_from_file(mode=list)
        for log in logs:
            t, log = log
            try:
                patt = r'Avg'
                pattern = self.re.compile(patt)
                test_list = []
                s1_list = []
                s2_list = []
                for line in log:
                    result = self.re.findall(pattern, line)
                    if result:
                        test_list.append(line)
                if len(test_list) != 4:
                    self.failed(t, 'error logfile')
                    self.merge(None)
                    continue
                list(map(lambda x: s1_list.append(test_list[x].split()[1]), [0, 1]))
                list(map(lambda x: s2_list.append(test_list[x].split()[1]), [2, 3]))
                self.merge(s1_list)
                self.merge(s2_list)
            except Exception as Ex:
                self.failed(t, Ex)
                self.merge(None)
                continue
