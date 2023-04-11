def minimumTime(N, cur, pos, time):
    i = 0
    l = []
    total_time = 0
    while i<N:
        total_time = abs((cur-pos[i])*time[i])
        l.append(total_time)
        i+=1
    return min(l)

cur = 4
N = 3
pos = [1,5,6]
time = [2,3,1]
