
from mapper import Task, Item


class BaseWorker:

    def __init__(self, task: Task):
        self.task = task

    def run(self):
        raise NotImplementedError


class ParseWorker(BaseWorker):

    def run(self):
        items = self.task.feed.engine.get_items()
        with self.task.session.begin():
            [Item(**dct) for dct in items]


class GetNewItemsTask(BaseWorker):
    pass