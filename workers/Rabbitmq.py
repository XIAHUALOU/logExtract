# -*- encoding: utf-8 -*-
from .Basewoker import BaseWorker


class Rabbitmq(BaseWorker):
    def run(self):
        logs = self.read_from_file(mode=list)
        for log in logs:
            t, log = log
            try:
                official = []
                clear = []
                index_list = []
                count = 0
                index_list = [i for i, x in enumerate(log) if x.find("sending") != -1]
                official.append(log[index_list[0]].split()[5])
                official.append(log[index_list[0] + 1].split()[5])
                clear.append(log[index_list[1]].split()[5])
                clear.append(log[index_list[1] + 1].split()[5])
                if len(official) != 2 or len(clear) != 2:
                    self.failed(t, 'error logfile')
                    self.merge(None)
                    continue
                self.merge(official)
                self.merge(clear)
            except Exception as Ex:
                self.failed(t, Ex)
                self.merge(None)
                continue
