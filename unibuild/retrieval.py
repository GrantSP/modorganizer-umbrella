__author__ = 'Tannin'


from task import Task
from config import config


class Retrieval(Task):

    def __init__(self):
        super(Retrieval, self).__init__()
        try:
            os.makedirs(config["paths"]["download"])
        except Exception, e:
            # ignore error, probably means the path already exists
            pass

    def fulfilled(self):
        super(Retrieval, self).fulfilled()

    def applies(self, parameters):
        return True

    def name(self):
        return

    def process(self, progress):
        return
