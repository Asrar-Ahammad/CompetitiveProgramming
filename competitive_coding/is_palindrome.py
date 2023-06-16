import string


def is_palindrome(s) -> bool:
    s = s.lower()
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    a = ''
    for i in s:
        if i in string.punctuation or i == ' ' or i in numbers:
            continue
        else:
            a += i
    b = a[::-1]
    if a == b:
        return True
    else:
        return False


print(is_palindrome(' '))
