def check(A, B):
    # A.sort()
    # B.sort()
    flag = 1
    # for i in A:
    #     if i != B[A.index(i)]:
    #         flag = 0
    #         break
    # return flag
    if sorted(A) != sorted(B):
            flag = False
    return flag
A = [1,2,5]
B = [2,4,15]
print(check(A,B))