"""
This is a demo task.

Write a function:

class Solution { public int solution(int[] A); }

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""



def solution(A):
    l = len(A)
    counters = [0] * l
    for number in A:
        if number > 0 and number - 1 < l:
            counters[number-1] += 1
    last_miss = 0
    for idx, value in enumerate(counters):
        last_miss = idx + 1
        if value == 0:
            return last_miss 
    return last_miss + 1



print(solution([1,3,6,4,1,2]))
