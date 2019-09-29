# -*- encoding: utf-8 -*-
from .Basewoker import BaseWorker


class Redis(BaseWorker):
    def run(self):
        logs = self.read_from_file(mode=list)
        for log in logs:
            t, log = log
            try:
                official = []
                clear = []
                index_list = []
                count = 0
                for _ in log:
                    _r = _.strip()
                    if _r.endswith("requests per second"):
                        if count < 18:
                            official.append(_r.split()[0])
                            count += 1
                        else:
                            clear.append(_r.split()[0])
                            count += 1
                index_list = [i for i, x in enumerate(log) if x.find("Sets") != -1]
                official.append(log[index_list[0]].split()[4])
                official.append(log[index_list[0]].split()[5])
                official.append(log[index_list[0] + 1].split()[4])
                official.append(log[index_list[0] + 1].split()[5])
                official.append(log[index_list[0] + 3].split()[4])
                official.append(log[index_list[0] + 3].split()[5])
                clear.append(log[index_list[1]].split()[4])
                clear.append(log[index_list[1]].split()[5])
                clear.append(log[index_list[1] + 1].split()[4])
                clear.append(log[index_list[1] + 1].split()[5])
                clear.append(log[index_list[1] + 3].split()[4])
                clear.append(log[index_list[1] + 3].split()[5])
                if len(official) != 24 or len(clear) != 24:
                    self.failed(t, 'error logfile')
                    self.merge(None)
                    continue
                self.merge(official)
                self.merge(clear)
            except Exception as Ex:
                self.failed(t, Ex)
                self.merge(None)
                continue
