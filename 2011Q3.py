import math
#1,9
#2,8
#3,7
#4,6
#5,5
#6,4
#7,3
#8,2
#9,1
#9 possible combinations for every 2 digits unless length is odd then only 1 combination in middle 5
#find length then narrow down
n = int(input())
total = 0
length = 1
while total < n:
    lastTotal = total
    total += 9**(length//2)
    length += 1

n -= lastTotal
s = ''
length -= 1

for i in range(length//2, 0, -1):
    total = 0
    val = 1
    while total < n:
        lastTotal = total
        total += 9**(i-1)
        val += 1
    n -= lastTotal
    s += str(val-1)
if length%2 == 1:
    s += '5'
for i in range(0, length//2):
    s += str(10-int(s[length//2-i-1]))
print(s)