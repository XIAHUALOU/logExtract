from .Basewoker import BaseWorker


class Postgres(BaseWorker):
    s3_list = []

    def run(self):
        logs = self.read_from_file(mode=list)
        for log in logs:
            container = []
            t, log = log
            try:
                for _ in log:
                    if _.strip().endswith("(excluding connections establishing)"):
                        container.append(_.strip().split()[2])
                if len(container) == 12:
                    self.merge(container[0:4])
                    self.merge(container[4:8])
                else:
                    self.failed(t, 'error logfile')
                    self.merge(None)
                    continue
            except Exception as Ex:
                self.failed(t, Ex)
                self.merge(None)
                continue

    def to_excel(self):
        pass

