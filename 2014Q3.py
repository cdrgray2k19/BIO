"""from math import comb
s = int(input())
result = []
x = 0
length = 1
while x+comb(36, length) < s:
    x += comb(36, length)
    length += 1
s -= x
index = 1
for i in range(0, length):
    x = 0
    while x+comb(36-index, length-i-1) < s:
        x += comb(36-index, length-i-1)
        index += 1
    s -= x
    result.append(index)
    index += 1
string = ''
for i in range(0, len(result)):
    if result[i] <= 26:
        string += chr(result[i]+65-1)
    else:
        string += str(result[i]-26-1)
print(string)"""



from functools import lru_cache

@lru_cache(maxsize=None)
def combs(highest, length):
    if length == 0:
        return 1
    total = 0
    for i in range(highest+1, 36):
        total += combs(i, length-1)
    return total


n = int(input())
#find length of string first
length = 1
while True:
    if length > 36:
        print("too long")
        assert False
    combinations = combs(-1, length)
    if combinations < n:
        n -= combinations
        length += 1
        continue
    break

def convert(num):
    if num < 26:
        return chr(ord("A")+num)
    return str(num-26)


s = ""
highest = -1
while len(s) < length:
    for i in range(highest+1, 36):
        total = combs(i, length-len(s)-1)
        if total >= n:
            s += convert(i)
            highest = i
        else:
            n -= total
print(s)