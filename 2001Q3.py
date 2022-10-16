from functools import lru_cache
n = int(input())
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