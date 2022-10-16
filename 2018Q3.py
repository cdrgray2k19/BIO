from functools import lru_cache

def switch(string, prev) -> list:
        possible = []
        change = True
        while change:
            change = False
            arr = list(string)
            for i in range(len(arr)-1):
                if i > 0 and (min(arr[i], arr[i+1]) < arr[i-1] < max(arr[i], arr[i+1])):
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    if ''.join(arr) in possible or ''.join(arr) in prev:
                        arr[i], arr[i+1] = arr[i+1], arr[i]
                    else:
                        change = True
                        possible.append(''.join(arr))
                        break
                elif i < (len(arr) - 2) and (min(arr[i], arr[i+1]) < arr[i+2] < max(arr[i], arr[i+1])):
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    if ''.join(arr) in possible or ''.join(arr) in prev:
                        arr[i], arr[i+1] = arr[i+1], arr[i]
                    else:
                        change = True
                        possible.append(''.join(arr))
                        break
        return possible

#@lru_cache(maxsize=None)
def solve(arr, prev, count) -> int:
    arr = list(arr)
    prev = list(prev)
    if len(arr) == 0:
        return count
    new = []
    for string in arr:
        result = switch(string, prev)
        for val in result:
            new.append(val)
            prev.append(val)
    return solve(tuple(new), tuple(prev), count+1)

d = int(input())
s = input()
print(solve(tuple([s]), tuple([s]), -1))