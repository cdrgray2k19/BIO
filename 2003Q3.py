"""from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    return n * factorial(n-1)

@lru_cache(maxsize=None)
def arrangements(ones, zeros):
    combs = factorial(ones+zeros)
    oneCombs = factorial(ones)
    zeroCombs = factorial(zeros)
    total = (combs/oneCombs)/zeroCombs
    return total


n, m = map(int, input().split())
if m == 0:
    print('0')
else:
    zeros = -1
    temp = n
    while temp > 0:
        zeros += 1
        temp -= arrangements(m-1, zeros)
        if temp <= 0:
            break
        else:
            n = temp

    string = '1'
    while len(string) < m+zeros:
        #figure out how many ways we can have after adding 0 to string
        if m == string.count('1'):
            #used all ones, just add zeros
            while string.count('0') < zeros:
                string += '0'
            break
        if zeros == string.count('0'):
            while string.count('1') < m:
                string += '1'
            break
        combsAfterZero = arrangements(m-string.count('1'), zeros-string.count('0')-1)
        if n-combsAfterZero > 0:
            n -= combsAfterZero
            string += '1'
        else:
            string += '0'

    #print value with spaces inbetween
    toPrint = ''
    for i in range(0, len(string)):
        if i%6==0 and i!=0:
            toPrint += ' '
        toPrint += string[i]
    print(toPrint)

"""
import math
n, m = map(int, input().split())
if m == 0:
    assert False, "answer: 0"

def comb(ones, zeros):
   return int(math.factorial(ones+zeros)/(math.factorial(ones)*math.factorial(zeros)))
#first get length
zeros = 0
while True:
    combs = comb(m-1, zeros)
    if combs < n:
        n -= combs
        zeros += 1
    else:
        break


ones = m-1
res = "1"
while (ones+zeros)>0:
    for num in [0,1]:
        if num == 0:
            if zeros == 0:
                continue
            zeros -= 1
        elif num == 1:
            if ones == 0:
                continue
            ones -= 1
        combs = comb(ones, zeros)
        if combs >= n:
            res += str(num)
            break
        else:
            n -= combs
            if num == 0:
                zeros += 1
            else:
                ones += 1
res2 = ""
for i in range(0, len(res)):
    if i%6 == 0:
        res2 += " "
    res2 += res[i]
print(res2[1:])