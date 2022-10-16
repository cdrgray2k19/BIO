from functools import lru_cache

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