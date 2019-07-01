from .basewoker import BaseWorker


class Python(BaseWorker):
    def run(self):
        print("Python")

    def to_excel(self):
        pass
