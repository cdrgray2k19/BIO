from collections import deque
s = list(input())

def solve(s):
    for i in range(1, len(s)//2+1):
        for j in range(0, len(s)-i-i+1):
            if s[j:j+i] == s[j+i:j+i+i]:
                return False
    return True

if solve(s):
    print("ACCEPTED")
else:
    print("REJECTED")

"""
valid = ["A", "B", "C"]

q = deque()
q.append([])
visited = set()
while q:
    s = q.popleft()
    if str(s) in visited:
        continue
    visited.add(str(s))
    added = False
    for c in valid:
        temp = s.copy()
        temp.append(c)
        if not solve(temp):
            continue
        q.append(temp)
        added = True
    if not added:
        print(s, len(s))
        break"""

#part 2 = 7, ['A', 'B', 'A', 'C', 'A', 'B', 'A']