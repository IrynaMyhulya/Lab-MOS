class Task(object):
    def __init__(self, time_arrive, time_process):
        self.time_arrive = time_arrive
        self.time_process = time_process
        self.time_start_process = None
        self.time_processed = 0
        self.time_exit = None
        self.time_in_queue = None


    def calc_time_in_queue(self):
        if self.time_exit:
            self.time_in_queue = self.time_exit - self.time_arrive - self.time_process


class Processor(object):
    def __init__(self, task=None):
        self.task = task

    def is_free(self):
        return bool(self.task) is False


class Queue(object):
    def __init__(self):
        self.queue = list()

    def add_element(self, task):
        self.queue.append(task)

    def get_element(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None

    def is_exist(self):
        return len(self.queue) > 0
