def termsOfAP(x):

    # Write your code here
    # Return a list of integers
    arr = []
    i = 1
    print('x',x)
    while len(arr) < x:
        n = 3*i+2
        if n%4 != 0:
            arr.append(n)
        i+=1
        
    return arr

print(termsOfAP(2))