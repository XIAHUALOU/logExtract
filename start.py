from libs import config
import os
import workers


class Startor:
    def __init__(self):
        if len(config.workers) == 0:
            workers = os.listdir(os.path.join(os.path.dirname(__file__), 'workers'))[:-2]
            workers.remove('basewoker.py')
            self.workers = [worker.split('.')[0] for worker in workers]
        else:
            self.workers = config.workers

    def run(self):
        for work in self.workers:
            if not hasattr(workers, work):
                continue
            runner = getattr(getattr(workers, work), work)()
            runner.run()
            runner.to_excel()


if __name__ == '__main__':
    Startor().run()
