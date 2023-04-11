roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000}
s = 'MCMXCIV'

result = 0

# Solution 1
# for a, b in zip(s, s[1:]):
#     if roman[a] < roman[b]:
#         result -= roman[a]
#     else:
#         result += roman[a]
#
# print(result+roman[s[-1]])


# Solution 2
a = 0
n = len(s) - 1
while a < n:
    if roman[s[a]] < roman[s[a + 1]]:
        result -= roman[s[a]]
    else:
        result += roman[s[a]]
    a += 1
print(result + roman[s[-1]])
