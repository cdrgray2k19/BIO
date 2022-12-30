from functools import lru_cache
p, i, n, w = map(int, input().split())


#need to construct a function which figures out, given the number of items, and the weight of a single parcel, how many distinct parcels could be made
#do this for each combination of p numbers adding up to n

res = 0

def splitPackets(n, p, packets):
    if n < 0:
        return 0
    if p == 0 and n > 0:
        return 0
    if n == 0 and p == 0:
        global w
        global res
        global i
        total = 1
        for packet in packets:
            total *= packetComb(i, w, packet, 1)
        res += total
        return 1

    total = 0
    for items in range(1, n-p+2):
        temp = packets.copy()
        temp.append(items)
        total += splitPackets(n-items, p-1, temp)
    return total


@lru_cache(maxsize=None)
def packetComb(i, w, k, max):
    if w < 0:
        return 0
    if k == 0 and w > 0:
        return 0
    if w == 0 and k == 0:
        return 1
    total = 0
    for weight in range(max, i+1):
        total += packetComb(i, w-weight, k-1, weight)
    return total

splitPackets(n, p, [])
print(res)