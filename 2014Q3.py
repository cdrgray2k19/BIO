from math import comb
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
print(string)