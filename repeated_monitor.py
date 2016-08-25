from threading import Thread, Event, Timer


class RepeatedTimer(Thread):
    def __init__(self, interval, function, *args, **kwargs):
        super(RepeatedTimer, self).__init__()
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.event = Event()
        self.event.set()

    def run(self):
        while self.event.is_set():
            t = Timer(self.interval, self.function, self.args, self.kwargs)
            t.start()
            t.join()

    def cancel(self):
        self.event.clear()
