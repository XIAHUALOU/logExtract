import threading
import contextlib
from queue import Queue


class ThreadPool(object):
    def __init__(self, max_num):
        self.StopEvent = 0  # stop signal,if get task is StopEvent,Stop current task
        self.q = Queue()
        self.max_num = max_num  # maxiumum threads
        self.terminal = False  #
        self.created_list = []  # existed thread list
        self.free_list = []  # free thread list
        self.Daemon = False  # set daemon thread

    def run(self, func, args, callback=None):
        """
        :param func: task func
        :param args: task func params
        :param callback:
        :return: if thread has terminated,return True or None
        """

        if len(self.free_list) == 0 and len(self.created_list) < self.max_num:
            self.create_thread()
        task = (func, args, callback,)
        self.q.put(task)

    def create_thread(self):
        """
        create thread
        """
        t = threading.Thread(target=self.call)
        t.setDaemon(self.Daemon)
        t.start()
        self.created_list.append(t)  # append current thread to list

    def call(self):
        """
        get task in a loop and execute it
        """
        current_thread = threading.current_thread()  # get current thread·
        event = self.q.get()  # get task from queue
        while event != self.StopEvent:  # Determine whether task is a terminator

            func, arguments, callback = event  # get funcname,params,callback name
            try:
                result = func(*arguments)
                func_excute_status = True  # set func executed status success
            except Exception as e:
                func_excute_status = False  # set func executed status failure
                result = None
                print('{} executed error:'.format(func.__name__), e)

            if func_excute_status:  #
                if callback is not None:  # determine whetherif callback is None
                    try:
                        callback(result)
                    except Exception as e:
                        print(callback.__name__, e)

            with self.worker_state(self.free_list, current_thread):
                if self.terminal:
                    event = self.StopEvent
                else:
                    event = self.q.get()

        else:
            self.created_list.remove(current_thread)

    def close(self):
        """
        when all task finished,close all threads
        """
        full_size = len(self.created_list)  # put terminal event to task queue
        while full_size:
            self.q.put(self.StopEvent)
            full_size -= 1

    def terminate(self):
        """
        terminate thread
        """
        self.terminal = True
        while self.created_list:
            self.q.put(self.StopEvent)

        self.q.empty()  # empty task queue

    def join(self):
        """
        Blocking the thread pool context so that all threads can continue after execution
        """
        for t in self.created_list:
            t.join()

    @contextlib.contextmanager
    def worker_state(self, state_list, worker_thread):
        """
        record the number of threads waiting in a thread
        """
        state_list.append(worker_thread)
        try:
            yield
        finally:
            state_list.remove(worker_thread)

    def alive_thread_num(self):
        return threading.activeCount()
