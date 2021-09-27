a = [1, 2, 3, 4, 2]

def solution(A):
    N = len(A)
    bottom_list = {}
    top_list = {}
    for P in range(N):
        bottom_list[P + 1] = A[P] + bottom_list.get(P, 0)
        top_list[P + 1]  = A[N - 1 - P] + top_list.get(P, 0)
    result = None
    for key, value in bottom_list.items():
        if key != N:
            diff = abs(value - top_list[N - key])
            if diff == 0:
                return 0
            elif not result:
                result = diff
            elif diff <= result:
                result = diff
    return result

print(solution(a))
