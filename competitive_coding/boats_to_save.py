def boats(people, limit):
    # First try
    # i = 0
    # j = 1
    # boats = 0
    
    # people.sort()
    # while i < len(people):
    #     if people[i] == limit:
    #         boats+=1
    #         i+=1
    #     elif j < len(people):
    #         if people[i]+people[j] <= limit:
    #             boats+=1
    #             i=j+1
    #             j=i+1
    #         else:
    #             boats+=1
    #             i+=1
    #             j=i+1
    #     else:
    #         boats+=1
    #         i+=1
    #         j=i+1
    # return boats

    # Second try
    i = 0
    j = len(people)-1
    boats = 0
    people.sort()
    while i<=j:
        if people[i]+people[j] <= limit:
            i+=1
        j-=1
        boats+=1
    return boats

people = [3,2,2,1]
limit = 3
print(boats(people, limit))        