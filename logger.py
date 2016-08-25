from threading import Thread, Event


class Logger(Thread):
    def __init__(self, queue, filename='log.txt'):
        super(Logger, self).__init__()
        self.queue = queue
        self.event = Event()
        self.event.set()
        self.filename = filename

    def run(self):
        with open(self.filename, 'w') as f:
            f.write("{:40} {:20} {:10} {:40}\n".format("URL", 'TIME', "STATUS", "ERROR"))
            while self.event.is_set():
                x = self.queue.get()
                print x
                f.write(x)

    def cancel(self):
        self.event.clear()
