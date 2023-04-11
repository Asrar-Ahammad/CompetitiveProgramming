def count_smaller_elements(arr, n):
    count = []
    i = 0
    sum = 0
    while i < n:
        num = arr[i]
        for i in range(i + 1, n):
            if i < num:
                sum += 1
            if i == n:
                count.append(sum)
                sum = 0
        i += 1
    return count


arr = [12, 1, 2, 3, 0, 11, 4]
n = len(arr)
print(count_smaller_elements(arr, n))
