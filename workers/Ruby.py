from .basewoker import BaseWorker


class Ruby(BaseWorker):
    def run(self):
        print("Ruby")

    def to_excel(self):
        pass
