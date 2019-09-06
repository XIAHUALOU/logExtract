from .Basewoker import BaseWorker


class Php(BaseWorker):
    def run(self):
        logs = self.read_from_file(mode=list)
        for log in logs:
            t, log = log
            try:
                patt = r'Score'
                pattern = self.re.compile(patt)
                test_list = []
                for line in log:
                    result = self.re.findall(pattern, line)
                    if (result):
                        test_list.append(self.re.findall("\d+", line)[0])
                if len(test_list) != 2:
                    self.failed(t, 'error logfile')
                    self.merge(None)
                    continue
                self.merge([test_list[0]])
                self.merge([test_list[1]])
            except Exception as Ex:
                self.failed(t, Ex)
                self.merge(None)
                continue
