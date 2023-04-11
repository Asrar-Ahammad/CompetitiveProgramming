def longest_palindrome(s):
    count = {}
    sum = 0
    flag = 0
    for i in s:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    for i in count:
        if count[i]%2 == 0:
            sum+=count[i]
        elif count[i] == 1:
            flag = 1
        
    return sum+flag

s = "a"
print(longest_palindrome(s))