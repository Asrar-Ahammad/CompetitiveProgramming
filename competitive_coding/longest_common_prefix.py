def longest_common_prefix(v):
    ans = ""
    v = sorted(v)
    first = v[0]
    last = v[-1]
    for i in range(min(len(first), len(last))):
        if(first[i] != last[i]):
            return ans
        ans += first[i]
    return ans


S = ["", ""]

print(longest_common_prefix(S))
