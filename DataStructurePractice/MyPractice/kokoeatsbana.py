import math

def minEatingSpeed(piles, h):

    left = 1
    right = max(piles)
    result = right

    while left<= right:
        k = (left+right)//2
        hours = 0

        for pile in piles:
            hours += math.ceil(pile/k)

        if hours <= h:
            result = k
            right = k-1
        else:
            left = k+1
    return result


piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles, h))