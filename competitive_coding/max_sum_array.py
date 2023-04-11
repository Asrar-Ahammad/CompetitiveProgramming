def max_array_sum(arr):
    start = 0
    end = len(arr)
    l_pos = 0
    r_pos = 0
    while start == end:
        if arr[start] > 0:
            l_pos = start
        if arr[end] > 0:
            r_pos = end
        start += 1
        end -= 1
