def isomorphic(s, t):
    # s_map = {}
    # t_map = {}
    # i = 0
    # while i < len(s):
    #     if s[i] not in s_map:
    #         s_map[s[i]] = {t[i]}
    #     else:
    #         s_map[s[i]].update({t[i]})
    #     if t[i] not in t_map:
    #         t_map[t[i]] = {s[i]}
    #     else:
    #         t_map[t[i]] = {s[i]}
    #     i += 1
    
    # for x in s_map:
    #     if len(s_map[x]) == 2:
    #         return False
    # for x in t_map:
    #     if len(t_map[x]) == 2:
    #         return False
    # for x in 
    # return s_map,t_map

    # Solution 2
    s_map = []
    t_map = []
    for x in s:
        s_map.append(s.index(x))
    for x in t:
        t_map.append(t.index(x))
    # if t_map == s_map:
    #     return True
    return s_map, t_map


s = "badc"
t = "baba"

s = "egg"
t = "add"

s = "paper"
t = "title"
print(isomorphic(s, t))  # calling the function
