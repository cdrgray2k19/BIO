from functools import lru_cache
import math

string1, string2 = input().split()
@lru_cache(maxsize=None)
def pat(string):
    if len(string) == 1:
        return True

    for splitPoint in range(1, len(string)):
        left = string[:splitPoint]
        right = string[splitPoint:]
        if pat(left[::-1]) and pat(right[::-1]):
            #check for alphabet
            if min(left) <= max(right):
                return False
            return True
    return False

'''
total = 0
for p in permutations('ACDEFGHIJKLMNOPQRSTUVWXYZ'):
    if pat('B'+str(p)):
        total += 1
print(total)
'''

if pat(string1):
    print('YES')
else:
    print('NO')

if pat(string2):
    print('YES')
else:
    print('NO')

if pat(string1+string2):
    print('YES')
else:
    print('NO')


#CDAB