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

## Set matrix zero
# def setZeroes(matrix) -> None:
#     zeros = {}

#     m = len(matrix)
#     n = len(matrix[0])
#     i,j = 0,0
#     while(i<m):
#         while(j<n):
#             if(matrix[i][j] == 0):
#                 if i not in zeros:
#                     zeros[i]= [j]
#                 else:
#                     zeros[i].append(j)
#             j+=1
#         i+=1

#     print(zeros)
#     for a in zeros:
#         for b in zeros[a]:
#             matrix

# def setZeroes(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
#     first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))
#
#     # Mark rows and columns to be zeroed out in the first row and first column
#     for i in range(1, rows):
#         for j in range(1, cols):
#             if matrix[i][j] == 0:
#                 matrix[i][0] = 0
#                 matrix[0][j] = 0
#
#     # Zero out the necessary rows and columns based on the first row and first column
#     for i in range(1, rows):
#         for j in range(1, cols):
#             if matrix[i][0] == 0 or matrix[0][j] == 0:
#                 matrix[i][j] = 0
#
#     # Zero out the first row and first column if needed
#     if first_row_has_zero:
#         for j in range(cols):
#             matrix[0][j] = 0
#
#     if first_col_has_zero:
#         for i in range(rows):
#             matrix[i][0] = 0
#
#     print(matrix)
#
#
# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# setZeroes(matrix)

# def sample_fun(l):
#     # l.append('a') # This changes the value of the list
#     l = ['b']  # This don't change the value of the list
#     return l
#
#
# my_list = ['z']
# print("Before : ", my_list)
# sample_fun(my_list)
# print("After : ", my_list)

a = None
x = b'hello'
print(type(x))

print(type(a))

import random

print(random.randrange(1, 10))
