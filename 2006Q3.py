from functools import lru_cache

score, darts = map(int, input().split())

@lru_cache(maxsize=None)
def solve(score, darts, start):
    if darts > 0 and score <= 0:
        return 0
    if darts == 0 and score == 0:
        return 1
    if darts == 0:
        return 0
    total = 0
    for i in range(1, 21):
        if darts == start:
            total += solve(score-(i*2), darts-1, darts)
        else:
            total += solve(score-(i), darts-1, darts)
    return total

print(solve(score, darts, darts))