def palindrome(number):
    number = list(number)

    if number == number[::-1]:
        return True
    else:
        return False


num = input()

if palindrome(num):
    print('True')
else:
    print('False')
