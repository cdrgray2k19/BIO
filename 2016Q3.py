l, p, q = map(int, input().split())
def generatePrimes(l):
    b = [True] * l
    b[0] = False
    b[1] = False
    for i in range(l):
        if b[i]:
            for j in range(i+i, l, i):
                b[j] = False
    return b

primes = generatePrimes(l)

posChanges = [2**i for i in range(0, 25)]
negChanges = [-posChanges[i] for i in range(0, 25)]
visited = set([p])
def solve(arr, end, max, path):
    new = []
    for val in arr:
        for i in range(0, 25):
            if 2 <= val + posChanges[i] < max:
                if primes[val + posChanges[i]] and val + posChanges[i] not in visited:
                    if val + posChanges[i] == end:
                        return path + 1
                    visited.add(val + posChanges[i])
                    new.append(val + posChanges[i])
            if 2 <= val + negChanges[i] < max:
                if primes[val + negChanges[i]] and val + negChanges[i] not in visited:
                    if val + negChanges[i] == end:
                        return path + 1
                    visited.add(val + negChanges[i])
                    new.append(val + negChanges[i])
    return solve(new, end, max, path+1)
print(solve([p], q, l, 1))