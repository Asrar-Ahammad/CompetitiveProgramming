def printPattern(n):
    for i in range(1,n+1):
        print("*"*i,end="")
        print()
    for i in range(n-1,-1,-1):
        print("*"*i,end="")
        print()

printPattern(10)