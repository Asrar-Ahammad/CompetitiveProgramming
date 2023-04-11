a = int(input())
l=list()
m = list()
for i in range(a):
    num = int(input(''))
    l.append(num)
for i in range(1,a+1):
    m.append(l[-i])

print(m)