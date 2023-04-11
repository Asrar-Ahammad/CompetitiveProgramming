# Solve it again
def countSubarray(N, A, M):
    count = 0
    i = 0
    sub_array = []
    median = 0
    # A = sorted(A)
    while i < N:
        if A[i] == M:
            count+=1
        sub_array = A[i:N]
        sub_array = sorted(sub_array)
        size = len(sub_array)
        if size%2 == 0:
            median = sub_array[(size//2)-1]
            if median == M:
                count+=1
        else:
            median = sub_array[size//2]
            if median == M:
                count+=1
        i+=1

    return count
A = [10,8, 8, 4, 9, 1, 6, 3, 5]
N = 9
M = 8
print(countSubarray(N, A, M))