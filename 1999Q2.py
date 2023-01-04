grid = []

atoms = set()

for i in range(0, 5):
    x,y = map(int, input().split())
    atoms.add((x-1,10-y))

def display(grid):
    for y in range(0, 10):
        print("".join(grid[y]))

def reset(grid, atoms):
    grid = []
    for y in range(0, 10):
        row = []
        for x in range(0, 10):
            if (x,y) in atoms:
                row.append("A")
            else:
                row.append(".")
        grid.append(row)
    return grid
    
    #grid[10-y][x-1] = "A"
grid = reset(grid, atoms)
display(grid)
while True:
    inp = input()
    if inp == "X 0":
        break
    side, num = inp.split()
    num = int(num)
    if side == "L":
        x = -1
        y = 10-num
        dir = (1,0)
    elif side == "R":
        x = 10
        y = 10-num
        dir = (-1,0)
    elif side == "T":
        y = -1
        x = num-1
        dir = (0,1)
    else:
        y = 10
        x = num-1
        dir = (0,-1)
    visited = set()
    status = ""
    while True:
        dx, dy = dir
        try:
            if grid[y+dy][x+dx] == "A":
                #absorbed
                grid[y+dy][x+dx] = "*"
                status = "Absorbed"
                break
        except:
            pass
        else:
            if dx == 0:
                try:
                    if grid[y+dy][x+1] == "A" and grid[y+dy][x-1] == "A":
                        dy += 2
                        if dy > 1:
                            dy = -1
                        dir = (dx, dy)
                        status = "Reflected"
                        continue
                except:
                    pass
                try:
                    if grid[y+dy][x+1] == "A":
                        dir = (-1,0)
                        continue
                except:
                    pass
                
                try:
                    if grid[y+dy][x-1] == "A":
                        dir = (1,0)
                        continue
                except:
                    pass


            elif dy == 0:
                try:
                    if grid[y+1][x+dx] == "A" and grid[y-1][x+dx] == "A":
                        dx += 2
                        if dx > 1:
                            dx = -1
                        dir = (dx, dy)
                        status = "Reflected"
                        continue
                except:
                    pass
                try:
                    if grid[y+1][x+dx] == "A":
                        dir = (0,-1)
                        continue
                except:
                    pass
                try:
                    if grid[y-1][x+dx] == "A":
                        dir = (0,1)
                        continue
                except:
                    pass
        x += dx
        y += dy
        visited.add((x,y))
        if not (0<= x < 10 and 0 <= y < 10):
            visited.remove((x,y))
            break
    for v in visited:
        X, Y = v
        grid[Y][X] = "+"
    
    
    display(grid)
    if status != "":
        print(status)
    else:
        if x < 0:
            print(f"Exits at L {10-y}")
        elif x > 9:
            print(f"Exits at R {10-y}")
        elif y < 0:
            print(f"Exits at T {x+1}")
        elif y > 9:
            print(f"Exits at B {x+1}")
    grid = reset(grid, atoms)