"""[space, stars, space]
            [4,1,4]
            [3,3,3]
            [2,5,2]
            [1,7,1]
            [0,9,0]"""
def printPattern(n):
    for i in range(n):
        # Space
        for j in range(n - i - 1):
            print(" ", end="")
        # Stars
        for k in range(2 * i + 1):
            print("*", end="")
        # Space
        for l in range(n - i - 1):
            print(" ", end="")
        print()


printPattern(5)
