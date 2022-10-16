from functools import lru_cache
from collections import defaultdict, deque

string = input()
s, p = map(int, input().split())


@lru_cache(maxsize=None)
def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

#E just doubles every step
#C and D just go to 2**(steps-1)for each of them
#find relationship for A and B
convert = {'A':'B', 'B':'AB', 'C':'CD', 'D':'DC', 'E': 'EE'}

def combs(letter, dict, steps):
    if steps == 0:
        dict[letter] += 1
        return dict, 1
    total = 0
    if letter == 'A':
        dict, total = combs('B', dict, steps-1)
    elif letter == 'B':
        dict['A'] += fib(steps-1)
        dict['B'] += fib(steps)
        total += fib(steps-1) + fib(steps)
    elif letter == 'C':
        dict['C'] += 2**(steps-1)
        dict['D'] += 2**(steps-1)
        total += 2**(steps)
    elif letter == 'D':
        dict['C'] += 2**(steps-1)
        dict['D'] += 2**(steps-1)
        total += 2**(steps)
    else:
        dict['E'] += 2**(steps)
        total += 2**(steps)
    
    return dict, total

d = defaultdict(int)

arr = list(string)
stack = deque(arr)
steps = s
while p > 0:
    letter = stack.popleft()
    temp = d.copy()
    temp, total = combs(letter, temp, steps)
    if total > p:
        for c in convert[letter][::-1]:
            stack.appendleft(c)
        steps -= 1
    else:
        d = temp
        p -= total

print(d['A'],d['B'],d['C'],d['D'],d['E'])