"""
from functools import lru_cache
import time
n = int(input())
start = time.time()
pod = tuple(map(int, input().split()))
station = tuple([])

@lru_cache(maxsize=None)
def move(station, pod, atPod, time):
    if len(pod) == 0:
        return time
    times = []
    station = list(station)
    pod = list(pod)
    if atPod:
        if len(pod) == 1:
            return pod[0]
        if len(station) == 0:
            sCopy = station.copy()
            pCopy = pod.copy()
            sCopy.append(pCopy[0])
            sCopy.append(pCopy[1])
            maxTime = max([pCopy[0], pCopy[1]])
            pCopy.pop(0)
            pCopy.pop(0)
            times.append(move(tuple(sCopy), tuple(pCopy), not atPod, time+maxTime))
        else:
            for i in range(0, len(pod)-1):
                for j in range(i+1, len(pod)):
                    sCopy = station.copy()
                    pCopy = pod.copy()
                    sCopy.append(pCopy[i])
                    sCopy.append(pCopy[j])
                    maxTime = max([pCopy[i], pCopy[j]])
                    pCopy.pop(i)
                    pCopy.pop(j-1)
                    times.append(move(tuple(sCopy), tuple(pCopy), not atPod, time+maxTime))
    else:
        sCopy = station.copy()
        pCopy = pod.copy()
        index = sCopy.index(min(sCopy))
        pCopy.append(sCopy[index])
        maxTime = sCopy[index]
        sCopy.pop(index)
        times.append(move(tuple(sCopy), tuple(pCopy), not atPod, time+maxTime))
    return min(times)

print(move(station, pod, True, 0))
end = time.time()
print(end-start)

"""



from itertools import combinations
import heapq
import time

n = int(input())
startT = time.time()
times = tuple(map(int, input().split()))
if len(times) == 1:
    print(times[0])
else:
    q = []
    start = (0, times, tuple(), True)
    heapq.heappush(q, start)
    #DP = dict()
    visited = set()
    while q:
        t, p, s, atPod = heapq.heappop(q)
        if len(s) == n:
            print(t)
            break
        if (s, atPod) in visited:
            #if t >= DP[(s, atPod)]:
            #    continue
            continue
        #DP[(s, atPod)] = t
        visited.add((s, atPod))
        s = list(s)
        p = list(p)
        if atPod:
            for ind1, ind2 in list(combinations(range(len(p)), 2)):
                tempS = s.copy()
                tempP = p.copy()
                astro1 = tempP.pop(ind2)
                astro2 = tempP.pop(ind1)
                tempS.append(astro1)
                tempS.append(astro2)
                q.append((t+max(astro1, astro2),tuple(tempP), tuple(tempS), not atPod))
        else:
            tempS = s.copy()
            tempP = p.copy()
            astro = tempS.pop(tempS.index(min(tempS)))
            tempP.append(astro)
            q.append((t+astro ,tuple(tempP), tuple(tempS), not atPod))
end = time.time()
print(end-startT)

"""
#iterative approach
#works for most of inputs
n = int(input())
p = list(map(int, input().split()))
s = []
atPod = True
time = 0
smallest = p[:2]
while len(s) < n:
    if atPod:
        if len(p) == 1:
            last = p.pop()
            s.append(last)
            time += last
        else:
            p = sorted(p)
            if p[:2] == smallest:
                p.pop(0)
                p.pop(0)
                for small in smallest:
                    s.append(small)
                time += smallest[1]
            else:
                time += p[-1]
                s.append(p.pop())
                s.append(p.pop())
    else:
        s = sorted(s)
        first = s.pop(0)
        time += first
        p.append(first)
    atPod = not atPod
print(time)"""