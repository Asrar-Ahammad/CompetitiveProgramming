def printPattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(2*i-1):
            print("*",end="")
        for l in range(n-i-1):
            print(" ",end="")
        print()

    for i in range(n-1,0,-1):
        '''[0,9,0]
            [1,7,1]'''
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(2*i-1):
            print("*", end="")
        for l in range(n-i-1):
            print(" ",end="")
        print()

printPattern(10)