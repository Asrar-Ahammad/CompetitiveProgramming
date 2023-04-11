# When we need to keep track of the previous variable we use stack
# When we need to remove strings from middle th also we use stack
from collections import deque
class stack:
    def __init__(self):
        self.container = deque()
    def push(self, val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)

def reverse(string):
    string = string[::-1]
    return string
    
def max_profit(X, Y, S):
    s = stack()
    a = 'pr'
    b = 'rp'

    if X<Y:
        X, Y = Y, X
        a, b = b, a
    ans = 0

    for i in S:
        if s.is_empty():
            s.push(i)
        elif i == a[1] and s.peek() == a[0]:
            ans += X
            s.pop()
        else:
            s.push(i)
    S = ''
    while s.is_empty()== False:
        S+=s.peek()
        s.pop()

    S = reverse(S)

    for i in S:
        if s.is_empty():
            s.push(i)
        elif i == b[1] and s.peek() == b[0]:
            ans+=Y
            s.pop()
        else:
            s.push(i)
    
    return ans

# S = "orzprqrd"
S = 'lrrfrrprgprpppppmurr' # X = 10, Y = 20
X = 10
Y = 20
print(max_profit(X, Y, S))
    

