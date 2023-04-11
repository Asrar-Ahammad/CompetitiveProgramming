from collections import deque
stack = deque()
# print(dir(stack))

stack.append(1)
print(stack)
stack.append(2)
stack.append(3)
stack.append(4)
print(stack)

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
    
s = stack()
s.push(5)
print(s.peek())
print(s.pop())
print(s.is_empty())
s.push(6)
s.push(7)
s.push(8)
print(s.size())

# Q1
print('Q1')
string = 'We will conquere COVID-19'
rev = stack()
rev.push(string)
rev_string = []
for i in string:
    rev.push(i)
print(string)
i = 0
while i<len(string):
    rev_string.append(rev.pop())
    i+=1
print(''.join(rev_string))

# Q2
# string = '("))((a+b}{")'
# i = 0
# o_stack = stack()
# c_stack = stack()
# flag = 0
# while i < len(string):
#     a = o_stack.pop()
#     b = c_stack.pop()
#     if a != '(' and b != ')':
#         flag = 1
#     elif a != '[' and b != ']':
#         flag = 1
#     elif a != '{' and b != '}':
#         flag = 1
# if flag == 1:
#     print(False)
# else:
#     print(True)