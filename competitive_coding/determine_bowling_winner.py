def isWinner(player1, player2):
    # Solution 1 (Solved 1175/1205 test cases)
    sum1, sum2 = 0, 0
    ind1, ind2 = 0, 0
    cou1, cou2 = 0, 0

    # for i in range(0,len(player1)):
    #     if ind1 == 10:
    #         cou1+=1
    #         if player1[i] == 10:
    #             sum1 = sum1+(2*player1[i])
    #             cou1 = 0
    #         if cou1 <= 2:
    #             sum1 = sum1+(2*player1[i])
    #             continue
    #         elif cou1 == 3:
    #             cou1 = 0
    #             ind1 = 0
    #     if player1[i] == 10:
    #         ind1 = 10
    #         sum1 = sum1+player1[i]
    #     else:
    #         sum1 = sum1+player1[i]

    # for i in range(0,len(player2)):
    #     if ind2 == 10:
    #         cou2+=1
    #         if player2[i] == 10:
    #             sum2 = sum2+(2*player2[i])
    #             cou2 = 0
    #         elif cou2 <= 2:
    #             sum2 = sum2+(2*player2[i])
    #             continue
    #         elif cou2 == 3:
    #             cou2 = 0
    #             ind2 = 0
    #     if player2[i] == 10:
    #         ind2 = 10
    #         sum2 = sum2+player2[i]
    #     else:
    #         sum2 = sum2+player2[i]
    # print('Player 1' ,sum1)
    # print('Player 2' ,sum2)
    
    # if sum1>sum2:
    #     return 1
    # elif sum1 == sum2:
    #     return 0
    # else:
    #     return 2

    # Solution 2
    ans, s1, s2 = 0, 0, 0
    p1, p2 = player1, player2
    n = len(p1)
    for i in range(n):
        s1 += p1[i]
        s2 += p2[i]
    if n > 1:
        for i in range(1, n):
            if p1[i - 1] == 10 or ((i >= 2) and p1[i - 2] == 10):
                s1 += p1[i]
            if p2[i - 1] == 10 or ((i >= 2) and p2[i - 2] == 10):
                s2 += p2[i]
    if s1 == s2:
        ans = 0
    elif s1 > s2:
        ans = 1
    else:
        ans = 2
    return ans  
    


player1 = [4,10,7,9]
player2 = [6,5,2,3]
player1 = [9,7,10,7]
player2 =[10,2,4,10]
player1 =[7,1,3,10]
player2 =[10,9,0,9]
player1 =[3,6,10,8]
player2 =[9,9,9,9]
player1 = [7,10,2,6,8,5,4,6,10,9,1,4,3,10,0,9,6,1,0]
player2 = [2,1,9,4,5,0,6,5,6,10,10,4,8,8,6,9,2,9,5]
print(isWinner(player1, player2))