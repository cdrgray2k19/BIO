from functools import lru_cache

#@lru_cache(maxsize=None)
def solve(min, max, remaining):
    if len(remaining) == 0:
        return 1
    total = 0
    for i in range(0, len(remaining)):
        temp = remaining.copy()
        c = temp.pop(i)
        if max == None:
            total += solve(c, c, temp)
        elif c>max:
            if max == min:
                total += solve(min, c, temp)
        elif c < max:
            if c > min:
                total += solve(min, c, temp)
            else:
                total += solve(c, max, temp)
    
    return total
            


#use memoisation
l, p = input().split()
l = int(l)#length of end list
p = list(p) #start of list
s = []#letters of alphabet not in allready opened list
for i in range(0, l):
    if chr(65+i) not in p:
        s.append(chr(65+i))
#no longer need l
#now check if string is valid
valid = True
for i in range(0, len(p)-2):
    for j in range(i+1, len(p)-1):
        for k in range(j+1, len(p)):
            if p[i]<p[j]<p[k]:
                valid = False
if not valid:
    print(0)
else:
    #find lowest acending pair
    lowest=[]
    for i in range(0, len(p)-1):
        for j in range(i+1, len(p)):
            if p[j]>p[i]:
                if len(lowest) == 0:
                    lowest = [p[i], p[j]]
                elif p[j] < lowest[1]:
                    lowest = [p[i], p[j]]
    

    #found lowest

    if len(lowest) == 0:
        lowest = [None, None]
    print(solve(lowest[0], lowest[1], s))


"""

n, p = input().split()
n = int(n)
p = list(map(lambda x:ord(x)-ord("A"), p))


def check(s):
    highest = None
    smallest = 100
    for c in s:
        smallest = min(smallest, c)
        if highest == None:
            if c > smallest:
                highest = c
        else:
            if smallest < c < highest:
                highest = c
            if c > highest:
                return False
    return (smallest, highest)

def solve(n, p, high):
    if len(p) == n:
        return 1
    total = 0
    if high == None:
        high = n
    for i in range(0, high):
        if i not in p:
            temp = p.copy()
            temp.append(i)
            res = check(temp)
            if res != False:
                tlow, thigh = res
                total += solve(n, temp, thigh)

            else:
                print("oh no")
    return total

res = check(p)
if res == False:
    print(0)
else:
    low, high = res
    print(solve(n,p,high))
"""