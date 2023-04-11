def shortest_distance(A, N, M):
    i = 0
    j = 0
    x = []
    y= []
    # Finding coordinates of X and Y
    while i < N:
        j = 0
        while j < M:
            if A[i][j] == 'X':
                i = int(i)
                j = int(j)
                x.append([i+1, j+1])
            if A[i][j] == 'Y':
                y.append([i+1,j+1])
            j+=1
        i += 1

    # Calculating manathan distance
    dist = []
    i = 0 
    j = 0
    temp = []
    while i < len(x):
        temp = x[i]
        j = 0
        while j <len(y):
            dist.append(abs(temp[0]-y[j][0]) + abs(temp[1]-y[j][1]))
            j+=1
        i+=1

    return min(dist)

grid  = [['X', 'X', 'O'],
         ['O', 'O', 'Y'],
         ['Y', 'O', 'O']]
N = M = 3
print(shortest_distance(grid, N, M))
