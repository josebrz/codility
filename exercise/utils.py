import numpy as np
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


def build_list(size: int, range_values: tuple, distinct_values: bool = False, ordered: bool = False):
    """
    :param size: size of the resulting list
    :param range_values: range of values that make up the resulting list
    :param distinct_values: defines whether the function returns a list of distinct elements
    :param ordered: define if the result matrix is ordered
    """
    if range_values[1] < range_values[0]:
        raise ValueError("The range of values provided must be in the format (minimum, maximum)")

    if range_values[1] == range_values[0]:
        raise ValueError("The maximum and minimum values must not be the same")

    if distinct_values and range_values[1] < size:
        raise ValueError("The size of the requested list must be less than or equal to the upper range of values")

    result_list = []
    for i in range(size):
        value = np.random.randint(range_values[0], range_values[1] + 1)
        if distinct_values:
            if value not in result_list:
                result_list.append(value)
        else:
            result_list.append(value)
    if ordered:
        result_list = sorted(result_list)

    return result_list
