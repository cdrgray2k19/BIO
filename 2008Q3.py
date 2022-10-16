from functools import lru_cache

start = list(map(int, input()))

def first(order):
    shirts = order.copy()
    removed = shirts.pop(0)
    shirts.insert(3, removed)
    return shirts

def second(order):
    shirts = order.copy()
    removed = shirts.pop()
    shirts.insert(3, removed)
    return shirts

def third(order):
    shirts = order.copy()
    removed = shirts.pop(3)
    shirts.insert(0, removed)
    return shirts

def fourth(order):
    shirts = order.copy()
    removed = shirts.pop(3)
    shirts.insert(6, removed)
    return shirts

visited = set()

def bfs(orders, depth):
    new = []
    for arrangment in orders:
        if tuple(arrangment) not in visited:
            visited.add(tuple(arrangment))
            temp = arrangment.copy()
            next = first(temp)
            if next == [1, 2, 3, 4, 5, 6, 7]:
                return depth
            new.append(next)
            temp = arrangment.copy()
            next = second(temp)
            if next == [1, 2, 3, 4, 5, 6, 7]:
                return depth
            new.append(next)
            temp = arrangment.copy()
            next = third(temp)
            if next == [1, 2, 3, 4, 5, 6, 7]:
                return depth
            new.append(next)
            temp = arrangment.copy()
            next = fourth(temp)
            if next == [1, 2, 3, 4, 5, 6, 7]:
                return depth
            new.append(next)
    

    return bfs(new, depth+1)

if start ==  [1, 2, 3, 4, 5, 6, 7]:
    print(0)
else:
    print(bfs([start], 1))