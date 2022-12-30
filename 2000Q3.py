#just a brute force method, how else to do?
n = int(input())
die1 = sorted(list(map(int, input().split())))
die2 = sorted(list(map(int, input().split())))

combs = []

def getCombs(length, arr, max):
    if len(arr) == length:
        global combs
        combs.append(arr)
        return
    for i in range(max, 9):
        temp = arr.copy()
        temp.append(i)
        getCombs(length, temp, i)

def getSum(die1, die2):
    sums = []
    for i in die1:
        for j in die2:
            sums.append(i+j)
    return sorted(sums)


getCombs(n, [], 1)
target = getSum(die1,die2)

for i in range(0, len(combs)-1):
    if combs[i] in [die1, die2]:
        continue
    for j in range(i+1, len(combs)):
        if combs[j] in [die1, die2]:
            continue
        if getSum(combs[i], combs[j]) == target:
            assert False, [combs[i], combs[j], getSum(combs[i], combs[j]), target]

print("impossible")