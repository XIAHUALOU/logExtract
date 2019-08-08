# -*- encoding: utf-8 -*-
"""
@Time    : 7/1/19 1:26 AM
@Author  : xiahaulou
@Email   : 390306467@qq.com
"""
from libs import config
from threadsPool.t_pool import ThreadPool
import os
import workers



class Startor:
    def __init__(self):
        if len(config.workers) == 0:
            workers = os.listdir(os.path.join(os.path.dirname(__file__), 'workers'))
            try:
                on_remove = ["__init__.py", 'Basewoker.py', '__pycache__']
                [workers.remove(_) for _ in on_remove]
            except Exception as Ex:
                pass
            self.workers = [worker.split('.')[0] for worker in workers]
        else:
            self.workers = config.workers
        self.pool = ThreadPool(config.config.getint('threads', 'maximum'))
    def run(self):
        for work in self.workers:
            if not hasattr(workers, work):
                continue
            try:
                runner = getattr(getattr(workers, work), work)()
                setattr(runner, '{}_container'.format(work.lower()), [])
            except Exception as Ex:
                print("task {} done Status: Failed {}".format(work, Ex))
                continue
            else:
                self.pool.run(runner.run,())
        self.pool.close()
        self.pool.join()

if __name__ == '__main__':
    Startor().run()

