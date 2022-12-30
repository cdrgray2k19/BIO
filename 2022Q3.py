res, num = input().split()
num = int(num)
res = list(map(lambda x:int(ord(x)-ord("a")), res))
length = len(res)

def findComb(res, next, length):
    if next == length:
        return 1
    positions = 0
    ind = res.index(next)
    positions += 1
    for i in range(ind-1, -1, -1):
        if res[i] < next:
            positions += 1
        else:
            break
    if positions == 0:
        return 0
    return positions*findComb(res, next+1, length)

pref = []
next = 0
while len(pref) < len(res):
    pos = set()
    ind = res.index(next)
    pos.add(ind)
    for i in range(ind-1, -1, -1):
        if res[i] < next:
            pos.add(i)
        else:
            break
    for new in pos:
        target = num
        temp = pref.copy()
        temp.append(new)
        target -= findComb(res, next+1, len(res))
        if target <= 0:
            pref.append(new)
            break
        else:
            num = target
    next += 1

print("".join(list(map(lambda x:chr(x+ord("A")),pref))))