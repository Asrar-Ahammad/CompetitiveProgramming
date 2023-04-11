from collections import deque

class stack:
    def __init__(self) -> None:
        self.container = deque()
    def push(self, val):
        self.container.append(val)
    def pop(self):
        self.container.pop()
    def top(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)
    
def valid_parathensis(s):
    par = { '(' : ')',
            '{' : '}',
            '[' : ']'}
    val = stack()
    for i in s:
        if val.is_empty():
            val.push(i)
        else:
            if par[val.top()] == i:
                val.pop()
    if val.is_empty:
        return True
    else:
        False

s = '()()()()(()'
valid_parathensis(s)