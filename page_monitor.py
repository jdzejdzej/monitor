from repeated_monitor import RepeatedTimer
from urllib2 import urlopen, HTTPError
from time import time


class PageMonitor(RepeatedTimer):
    def __init__(self, url, conditions, reference, interval, queue):
        super(PageMonitor, self).__init__(interval, self.logger)
        self.url = url
        self.queue = queue
        self.condition = conditions
        self.reference = reference

    def logger(self):
        response, time_delta, code = self.reader()
        status = "FAIL"
        if not code:
            status, code = self.evaluate_condition(response)
        msg = "{:40} {:20} {:10} {:40}\n".format(self.url, str(time_delta), status, code)
        self.queue.put(msg)

    def evaluate_condition(self, response):
        status, code = "PASS", ""
        try:
            if not self.condition(response, self.reference):
                status = "FAIL"
                code = "operation: {} failed on site with arg: {}".format(self.condition.func_name, self.reference)
        except Exception as ex:
            status = "FAIL"
            code = ex

        return status, code

    def reader(self):
        start = time()
        code, html = "", ""
        try:
            response = urlopen(self.url)
            html = response.read()
            response.close()
        except HTTPError as err:
            html = ""
            code = err
        except:
            code = "something went wrong..."
        stop = time()
        return html, stop - start, code
