from Queue import Queue
from logger import Logger
from page_monitor import PageMonitor


class Monitor(object):
    def __init__(self, urls, conditions, references, intervals):
        self.queue = Queue()
        self.threads = map(PageMonitor, urls, conditions, references, intervals, [self.queue] * len(urls))
        self.logger = Logger(self.queue)

    def start(self):
        for thread in self.threads:
            thread.start()
        self.logger.start()

    def cancel(self):
        for thread in self.threads:
            thread.cancel()
        self.logger.cancel()
