import numpy as np


def build_list(size: int, range_values: tuple, distinct_values: bool = False):
    """
    :param size: size of the resulting list
    :param range_values: range of values that make up the resulting list
    :param distinct_values: defines whether the function returns a list of distinct elements
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

    return result_list
