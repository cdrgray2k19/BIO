from functools import lru_cache

letters, adj, totLength = map(int, input().split())
n = int(input())

@lru_cache(maxsize=None)
def count(length, lastCount, last):
    if length == 0:
        return 1
    total = 0
    for c in range(letters):
        c = str(c)
        if c == last:
            if lastCount+1>adj:
                continue
            total += count(length-1, lastCount+1, c)
        else:
            total += count(length-1, 1, c)
    return total

prefix = ''
lastCount = 0
last = ''
while len(prefix) < totLength:
    for c in range(letters):
        c = str(c)
        if c == last:
            withPrefix = count(totLength - len(prefix)-1, lastCount+1, c)
        else:
            withPrefix = count(totLength - len(prefix)-1, 1, c)
        if withPrefix >= n:
            #found right prefix
            if c == last:
                lastCount += 1
            else:
                lastCount = 1
            last = c
            prefix += c
            break

        n -= withPrefix

result = ''
for c in prefix:
    result += chr(ord('A')+int(c))
print(result)