N = int(input('Enter number of rows :'))

# arr = [[0]*N]*N
arr = []
for i in range(N):
    col = []
    for j in range(N):
        num = int(input('Enter number :'))
        col.append(num)

    arr.append(col),

count = {1: 0, 2: 0, 3: 0}
a = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            count[a] += 1
    a += 1
if count[1] > count[2]:
    if count[1] > count[3]:
        print('max count :', count[1])
    if count[1] < count[3]:
        print('max count :', count[3])
else:
    if count[3] > count[2]:
        print('max count :', count[3])
    else:
        print('max count :', count[2])
