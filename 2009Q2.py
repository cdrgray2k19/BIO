grid = []
for i in range(4):
    grid.append(list(input()))

first = [grid[0][0],grid[1][0],grid[2][0],grid[3][0]]
second = [grid[0][1],grid[1][1],grid[2][1],grid[3][1]]
third = [grid[0][2],grid[1][2],grid[2][2],grid[3][2]]
fourth = [grid[0][3],grid[1][3],grid[2][3],grid[3][3]]


def findChuncks(arr):
    visited = set()
    chunks = []
    toBeDel = []
    for y in range(4):
        for x in range(4):
            if (x,y) not in visited:
                length, visited, temp = bfs((x,y), arr, visited)
                if length > 1:
                    chunks.append(length)
                    toBeDel.extend(temp)
    return chunks, toBeDel

def bfs(start, g, visited):
    stack = [start]
    length = 1
    toBeDel = [start]
    while stack:
        x,y = stack.pop(0)
        if (x,y) not in visited:
            visited.add((x,y))
            for dx,dy in [(1,0), (-1,0), (0, 1), (0, -1)]:
                if 0 <= x+dx < 4 and 0 <= y+dy < 4:
                    if (x+dx, y+dy) not in visited:
                        if g[y+dy][x+dx] == g[y][x]:
                            stack.append((x+dx, y+dy))
                            toBeDel.append((x+dx, y+dy))
                            length += 1
    return length, visited, toBeDel

scoreArr, toBeDelled = findChuncks(grid)
for x,y in toBeDelled:
    grid[y][x] == 0

#now pop positions from grid and then replace

collumn = 0
firstCopy = first.copy()
secondCopy = second.copy()
thirdCopy = third.copy()
fourthCopy = fourth.copy()

for collumn in range(4):
    for y in range(4):
        if grid[collumn][y-1] == 0:
            grid[collumn][y-1], grid[collumn][y] = grid[collumn][y], grid[collumn][y-1]