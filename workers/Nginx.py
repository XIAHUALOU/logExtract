from .basewoker import BaseWorker


class Nginx(BaseWorker):
    def run(self):
        logs = self.read_from_file()
        for log in logs:
            t, log = log
            times = 0
            count = 0
            official = []
            clear = []
            for _ in log:
                v = None
                if _.startswith('Time taken for tests'):
                    v = _.strip('\n').split()[4]
                elif _.startswith('Time per request'):
                    v = _.strip('\n').split()[3]
                elif _.startswith('Requests per second'):
                    v = _.strip('\n').split()[3]
                elif _.startswith('Transfer rate:'):
                    v = _.strip('\n').split()[2]
                if v is not None:
                    count += 1
                    if count > 5:
                        clear.append(v)
                    else:
                        official.append(v)
            times += 1
            self.swap(official, 1, 2)
            self.swap(official, 2, 3)
            self.swap(clear, 1, 2)
            self.swap(clear, 2, 3)
            r = self.pd.DataFrame([official, clear]).T
            print(r)
            self.to_csv(t, r)

    def to_excel(self):
        pass
