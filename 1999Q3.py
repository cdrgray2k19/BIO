from collections import deque
n = int(input())
points = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))
savedEnds = targets.copy()
targets = set(targets)
maxTarget = max(targets)

#for each term in BFS, store - (score, rounds, history)

q = deque()
visited = set()
q.append((0, 0, []))

results = dict()

while q:
    score, rounds, history = q.popleft()
    if score in targets:
        results[score] = (rounds, history)
        targets.remove(score)
        if len(targets) == 0:
            break
    if score in visited:
        continue
    if score > maxTarget:
        continue
    visited.add(score)

    for p in points:
        temp = history.copy()
        temp.append(p)
        q.append((score+p, rounds+1, temp))


for s in savedEnds:
    if s not in results:
        print("Impossible")
    else:
        rounds, history = results[s]
        numbers = dict()
        for num in history:
            if num not in numbers:
                numbers[num] = 1
            else:
                numbers[num] += 1
        output = ""
        output += str(rounds) + " "
        for num in numbers.keys():
            output += str(numbers[num]) + "x" + str(num) + " "
        print(output)