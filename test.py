# A = [2, 1, 3, 5]
# sub_array = []
# i = 0

# while i < len(A):
#     sub_array = A[i:len(A)]
#     print(sub_array)
#     i+=1

# sub_array = sorted(sub_array)
# print(sub_array,len(sub_array))


# def square(T):
#     T = list(T)
#     i = 0
#     n = len(T)
#     while i < n:
#         T.append(T[i]*T[i])
#         i+=1
#     return tuple(T)

# L = [1,2,3,4,5,6]
# T = tuple(L)
# ans = square(T)

# if type(T) == type(ans):
#     print(ans)

# def replaceV(S):
#   vowels =list('aeiouAEIOU')
#   L = list(S)
#   n = len(S)
  
#   for i in range(n):
#     if L[i] in vowels and L[i+1] in vowels and L[i+2] in vowels:
#       L[i]='*'
#       L[i+1]='*'
#       L[i+2]='*'
#     i+=1
#     return (''.join(L).replace('***','_'))
            
# S = 'aaahellooo'
# print(replaceV(S))


# d = {'a':1}
# s = 'a'
# if d[s[0]] == 1:
#     print('H')

# Missing number in array
# def missing(l, n):
#     l = sorted(l)
#     for i in range(0,len(l)):
#         if min(l) != 1:
#             return 1
#         elif l[i+1]-l[i] != 1:
#             ans = l[i]+1
#             break
#     return ans
# l = [2]
# n = len(l)
# print(missing(l, n))

# a=[1,2,3]
# a.reverse()
# s=''
# for i in a:
#     s+=str(i)
# print(s)

# count = {}
#         letters = ''
#         sum = 0
#         i = 0
#         j = 1

#         while i < len(s):
#             if j < len(s):
#                 if s[i] != s[j]:
#                     letters = s[i]+s[j]
#                     if letters not in count:
#                         count[letters]=1
#                         i=j+1
#                         j=i+1
#                     else:
#                         count[letters]+=1
#                         i = j+1
#                         j = i+1
#             else:
#                 if letters == '':
#                      letters+=s[i]
#                 # letters = str(letters)
#                 if letters not in count:
#                     count[letters] = 1
#                     letters=''
#                     i+=1
#                 else:
#                     count[letters] +=1
#                     letters=''
#                     i+=1
#         for i in count:
#             sum = sum + count[i]
#         return sum