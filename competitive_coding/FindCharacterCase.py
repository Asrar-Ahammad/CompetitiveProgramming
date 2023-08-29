import string

a = input("Enter a character")
if a in string.ascii_uppercase:
    print(1)
elif a in string.ascii_lowercase:
    print(0)
else:
    print(-1)