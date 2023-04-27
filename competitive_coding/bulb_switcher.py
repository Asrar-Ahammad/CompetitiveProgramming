from math import sqrt

def bulbSwitcher(n):
    # It is a brain teaser 
    return int(sqrt(n))
    # l = []
    # for i in range(n):
    #     if i%2 == 0:
    #         l.append(1)
    #     else:
    #         l.append(0)
    # i = 2
    # while i < n:
    #     for j in range(0,n,i):
    #         if l[j-1] == 0:
    #             l[j-1] = 1
    #         else:
    #             l[j-1] = 0
    #     i+=1
    # return l

print(bulbSwitcher(4))
