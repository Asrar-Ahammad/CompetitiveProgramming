def uncommon_sum(arr1: list, arr2: list) -> int:
    sum = 0

    # Using for loop

    # for i in arr1:
    #     if i in arr2:
    #         continue
    #     else:
    #         sum+=i
    #
    # for i in arr2:
    #     if i in arr1:
    #         continue
    #     else:
    #         sum+=i

    # Using sets
    arr1 = set(arr1)
    arr2 = set(arr2)

    a = arr1-arr2
    b = arr2-arr1

    a = list(a)
    b = list(b)

    a.append(b)
    sum
    return sum

arr1 = [1,2,3,4,5,6,7]
arr2 = [1,2,3,4,9,10,11,12]

print(uncommon_sum(arr1,arr2))