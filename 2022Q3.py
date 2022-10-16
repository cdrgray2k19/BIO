from functools import lru_cache
parked, n = input().split()
n = int(n)
letters = []
for i in range(0, len(parked)):
    letters.append(chr(65+i))

prefered = []
seen = []
for i in range(0, len(parked)):
    if parked[i] == 'a':
        prefered.append([chr(i+65)])
        seen.append(chr(i+65))
        break
#now we know the first one

for char in range(1, len(parked)):
    for i in range(0, len(parked)):
        if parked[i] == chr(ord('a')+char):
            #found car we were looking for
            arr = [chr(i+65)]
            seen.append(chr(i+65))
            for c in letters:
                if c < chr(i+65) and c in seen:
                    arr.append(c)
            prefered.append(arr)

#now just find combinations
#need to sort each preferred so backtracking works

for i in range(0, len(prefered)):
    prefered[i] = sorted(prefered[i])

print(prefered)

@lru_cache(maxsize=None)
def combinations(indexToStart):
    if indexToStart == len(prefered):
        return 1
    
    combs = 1
    for i in range(indexToStart, len(prefered)):
        combs *= len(prefered[i])
    
    return combs

string = prefered[0][0]
car = 1
while len(string)<len(parked):
    for i in range(0, len(prefered[car])):
        arrange = combinations(car+1)
        if arrange >= n:
            string += prefered[car][i]
            car += 1
            break
        else:
            n -= arrange

print(string)