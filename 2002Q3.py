#dynamic programming

import math
n = int(input())

def findFactors(num):
    factors = []
    for i in range(2, math.floor(math.sqrt(num))+1):
        if (num/i)%1 == 0:
            factors.append((i, int(num/i)))
    return factors

previous = [0, 1, 2, 3, 4, 5]#base cases
for i in range(6, n+1):
    previous.append(previous[i-1]+1)
    factors = findFactors(i)
    for pair in factors:
        a, b = pair
        previous[i] = min(previous[i], previous[a]+previous[b])
print(previous[n])