import math
a = [[1,2,10],
    [4,5,6],
    [7,8,9]]

l_sum = 0
r_sum = 0
row = 0
for i in range(len(a)):
    l_sum = l_sum+a[row][row]
    row+=1
row = len(a)-1
tra = 0
for i in range(len(a)):
    r_sum = r_sum+a[row][tra]
    row-=1
    tra+=1

if r_sum>l_sum:
        print(r_sum-l_sum)
else:
    print(l_sum-r_sum)