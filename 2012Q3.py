from functools import lru_cache
#bfs of ladder and changes
#visited for ladder so it cant loop around

#have a convert function that converts numbers to letters

#do bfs with numbers to test, end number, and depth
#for each number given to function go through numbers 1-999 inclusive and see if difference in letters are equal to or less than 5
#have a visited to check so that numbers cannot be looked up twice

def convert(num):
    numLetMap = {'1': 'ONE', '2': 'TWO', '3': 'THREE', '4': 'FOUR', '5': 'FIVE', '6': 'SIX', '7': 'SEVEN', '8': 'EIGHT', '9': 'NINE', '0': 'ZERO'}
    letters = []
    for c in num:
        letters.extend(numLetMap[c])
    return letters

@lru_cache(maxsize=None)
def check(num1, num2):
    
    #convert numbers to letters

    let1 = convert(str(num1))
    let2 = convert(str(num2))

    #test to see if numbers are compatable
    dif = 0
    for i in range(0, len(let1)):
        if let1[i] not in let2:
            dif += 1
        else:
            let2.pop(let2.index(let1[i]))
    
    total = dif + len(let2)
    if total <= 5:
        return True
    else:
        return False


def bfs(nums, target, depth):
    new = set()
    for n in nums:
        visited.add(n)
        for i in range(1, 1000):
            if i not in visited:
                if check(n, i):
                    if i == target:
                        return depth
                    new.add(i)
    
    return bfs(list(new), target, depth+1)

pairs = []
for _ in range(3):
    pairs.append(list(map(int, input().split())))

for i in range(0, len(pairs)):
    visited = set()
    print(bfs([pairs[i][0]], pairs[i][1], 1))

#13

#7

#yes