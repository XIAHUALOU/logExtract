from .Basewoker import BaseWorker


class Php(BaseWorker):
    def run(self):
        logs = self.read_from_file(mode=list)
        for log in logs:
            t, log = log
            patt = r'Score'
            pattern = self.re.compile(patt)
            test_list = []
            for line in log:
                result = self.re.findall(pattern, line)
                if (result):
                    test_list.append(self.re.findall("\d+", line)[0])
            self.merge([test_list[0]])
            self.merge([test_list[1]])
            self.status(t)

    def to_excel(self):
        pass
