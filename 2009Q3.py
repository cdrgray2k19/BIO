#can also be done with dynamic programming and not just memoised recursion

from functools import lru_cache
s, n = map(int, input().split())

@lru_cache(maxsize=None)
def arrange(sum):
    if sum == 0:
        return 1
    if sum < 0:
        return 0
    total = 0
    for i in range(1, 10):
        temp = sum - i
        total += arrange(temp)
    return total

arrangement = ''
while s > 0:
    for i in range(1, 10):
        combs = arrange(s-i)
        if n <= combs:
            s -= i
            arrangement += str(i)
            break
        else:
            n -= combs

print(arrangement)