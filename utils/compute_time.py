from datetime import datetime


class ComputeTime:
    """
    This class is used to calculate the execution time of the program
    """
    def __init__(self):
        self.start_date = datetime.now()

    def stop_time(self):
        print(self.compute_time())

    def compute_time(self):
        return f'Duration: {(datetime.now() - self.start_date).microseconds} microseconds'
