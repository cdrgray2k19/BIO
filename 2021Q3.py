"""#dont need warehouse just need to convert letters to numbers and then get next one after shops max
#reduces need for deepcopy and storing warehouses
from functools import lru_cache
from copy import deepcopy

desired = input()
warehouse = []
for i in range(len(desired)):
    warehouse.append(i)
shop = []

def add(arr):
    if len(arr) < len(desired):
        maximum = -1
        if len(arr) > 0:
            maximum = max(arr)
        toAdd = warehouse[maximum+1]
        arr.append(toAdd)
        return arr
    else:
        return False

def swap(arr):
    if len(arr) >= 2:
        store = arr[0]
        arr[0] = arr[1]
        arr[1] = store
        return arr
    else:
        return False

def rotate(arr):
    if len(arr) >= 3:
        store = arr.pop(0)
        arr.append(store)
        return arr
    else:
        return False

def translate(arr):
    string = ''
    for c in arr:
        string += chr(ord('A')+c)
    return string


visited = set()
def bfs(orders, depth):
    new = []
    for shop in orders:
        if tuple(shop) not in visited:
            visited.add(tuple(shop))
            temp = shop.copy()
            result = add(temp)
            if result != False:
                if translate(result) == desired:
                    return depth
                new.append(result)
            
            temp = shop.copy()
            result = swap(temp)
            if result != False:
                if translate(result) == desired:
                    return depth
                new.append(result)
            
            temp = shop.copy()
            result = rotate(temp)
            if result != False:
                if translate(result) == desired:
                    return depth
                new.append(result)
            

    return bfs(new, depth+1)

print(bfs([shop], 1))"""





from collections import deque

def add(s):
    s.append(chr(len(s) + ord("A")))
    return s

def swap(s):
    temp = s[0]
    s[0] = s[1]
    s[1] = temp
    return s

def rotate(s):
    front = s.pop(0)
    s.append(front)
    return s


target = tuple(input())

q = deque()
q.append(((), 0))
visited = set()
while q:
    cur, dist = q.popleft()
    
    if cur == target:
        print(dist)
        break

    if cur in visited:
        continue

    visited.add(cur)
    cur = list(cur)

    if len(cur) < len(target):
        temp = cur.copy()
        added = tuple(add(temp))
        if added not in visited:
            q.append((added, dist+1))

    if len(cur) >= 2:
        temp = cur.copy()
        swapped = tuple(swap(temp))
        if swapped not in visited:
            q.append((swapped, dist+1))

    if len(cur) >= 1:
        temp = cur.copy()
        rotated = tuple(rotate(temp))
        if rotated not in visited:
            q.append((rotated, dist+1))