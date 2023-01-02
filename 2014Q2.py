"""#red = solid  and green = dashed
# 6 different tiles
#load in grid then for each player
#for each square start search for a cycle, each square added to visited so cant backtrack or search for cycle when allready found, each cycle search keep score to add onto total for that player

def count(col, n, grid):
    stepX = 0
    stepY = 0
    visited = set()
    total = 0
    while len(visited) < n**2:
        x = stepX
        y = stepY

        if (y, x) not in visited:
            square = grid[y][x]
            val = min(col[square])
            
            if val == 1:
                y -= 1
            elif val == 2:
                x += 1
            elif val == 3:
                y += 1
            else:
                x -= 1
            score = 1
            cycle = [(stepY, stepX)]
            while 0 <= x < n and 0 <= y < n:
                if (y, x) in visited:
                    break
                val = val - 2
                if val < 1:
                    val = 4 + val
                square = grid[y][x]
                if val in col[square]:
                    if (y, x) in cycle:
                        total += score
                        break
                    cycle.append((y, x))

                    score += 1

                    val = col[square][1-col[square].index(val)]
                    if val == 1:
                        y -= 1
                    elif val == 2:
                        x += 1
                    elif val == 3:
                        y += 1
                    else:
                        x -= 1
                    
                    
                else:
                    break
            for i in range(0, len(cycle)):
                visited.add(cycle[i])

        stepX += 1
        if stepX == n:
            stepY += 1
            stepX = 0

    return total

def main(n, grid):
    #n = int(input())

    #grid = []

    #for _ in range(n):
    #    grid.append(list(map(int, input().split())))


    red = {1: [1,3], 2: [2,4], 3: [1,4], 4: [1,2], 5: [2,3], 6: [3,4]}
    green = {1: [2,4], 2: [1,3], 3: [2,3], 4: [3,4], 5: [1,4], 6: [1,2]}
    return [count(red, n, grid), count(green, n, grid)]
    #do red first

if __name__ == '__main__':
    n = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().split())))
    
    print(*main(n, grid))"""





n = int(input())
grid = []
for _ in range(0, n):
    grid.append(list(map(int, input().split())))

#do one complete search for red
#one complete search for green
#start top right
#follow connections, keeping track of visited
#just have to work out connections myself

#red connections then green
tiles =[["UD", "LR"], ["LR", "UD"], ["LU", "DR"], ["UR", "LD"], ["DR", "LU"], ["LD", "UR"]]

translate = {"L": (-1, 0), "R":(1, 0), "U":(0, -1), "D":(0, 1)}

directions = ["U", "L", "D", "R"]

def search(x, y, ind):
    global grid
    global tiles
    global translate
    global directions
    last = ""
    visited = set()
    while True:
        visited.add((x,y))
        tileNum = grid[y][x]
        dirs = tiles[tileNum-1][ind]
        dir = ""
        if last == "":
            dir = dirs[0]
        else:
            if last not in dirs:
                return False, visited
            for d in dirs:
                if d != last:
                    dir = d
                    break
        dx,dy = translate[dir]
        last = directions[(directions.index(dir)-2)%4]
        x += dx
        y += dy
        if (x,y) in visited:
            return True, visited
        if not(0 <= x < len(grid) and 0 <= y < len(grid)):
            return False, visited

points = [0,0]
for ind in [0,1]:
    visited = set()
    for y in range(0, n):
        for x in range(0, n):
            if (x,y) in visited:
                continue
            score, searched = search(x,y,ind)
            visited.update(searched)
            if score:
                points[ind] += len(searched)

for p in points:
    print(str(p)+" ", end="")
print("")