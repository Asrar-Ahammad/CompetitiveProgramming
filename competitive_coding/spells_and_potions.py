def successfulPairs(self, spells, potions, success):
        result = []
        count = 0
        low = 0
        high = len(potions)
        i = 0
        potions.sort()
        while low <=high :
                mid = low+(high-low)//2
                while spells[i]*potions[mid] > success