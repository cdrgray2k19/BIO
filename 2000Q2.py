class ant:
    def __init__(self, x, y, dir):
        self.x = int(x)
        self.y = int(y)
        self.d = dir
        self.playing = True

grid = []
for i in range(0, 11):
    row = []
    for j in range(0, 11):
        row.append(0)
    grid.append(row)

ant1 = ant(*input().split())
ant2 = ant(*input().split())

def simul(moves, ant1, ant2, grid):
    while moves > 0:
        if ant1.playing:
            dir = ant1.d
            if dir == "L":
                ant1.x -= 1
            elif dir == "R":
                ant1.x += 1
            elif dir == "T":
                ant1.y += 1
            elif dir == "B":
                ant1.y -= 1
            else:
                assert False
            
            directions = ["T", "R", "B", "L"]
            if not(0 <= 11-ant1.y < 11 and 0 <= ant1.x-1 < 11):
                ant1.playing = False

            elif grid[11-ant1.y][ant1.x-1] == 0:
                ind = directions.index(dir)
                ind += 1
                ind %= 4
                ant1.d = directions[ind]
            else:
                ind = directions.index(dir)
                ind -= 1
                ind %= 4
                ant1.d = directions[ind]

            grid[11-ant1.y][ant1.x-1] = 1 - grid[11-ant1.y][ant1.x-1]


        if ant2.playing:
            if ant2.playing:
                dir = ant2.d
                if dir == "L":
                    ant2.x -= 1
                elif dir == "R":
                    ant2.x += 1
                elif dir == "T":
                    ant2.y += 1
                elif dir == "B":
                    ant2.y -= 1
                else:
                    assert False
                
                directions = ["T", "R", "B", "L"]
                if not(0 <= 11-ant2.y < 11 and 0 <= ant2.x-1 < 11):
                    ant2.playing = False

                elif grid[11-ant2.y][ant2.x-1] == 0:
                    ind = directions.index(dir)
                    ind += 1
                    ind %= 4
                    ant2.d = directions[ind]
                    grid[11-ant2.y][ant2.x-1] = 1 - grid[11-ant2.y][ant2.x-1]
                else:
                    ind = directions.index(dir)
                    ind -= 1
                    ind %= 4
                    ant2.d = directions[ind]

                    grid[11-ant2.y][ant2.x-1] = 1 - grid[11-ant2.y][ant2.x-1]

        moves -= 1
    return ant1, ant2, grid

while True:
    order = input()
    if order == "-1":
        break
    try:
        order = int(order)
        moves = order
        ant1, ant2, grid = simul(moves, ant1, ant2, grid)
        for i in range(0, 11):
            for j in range(0, 11):
                if grid[i][j] == 0:
                    print(".", end="")
                else:
                    print("*", end="")
            print("")
        if ant1.playing:
            print(ant1.x, ant1.y, ant1.d)
        else:
            print("Removed")
        if ant2.playing:
            print(ant2.x, ant2.y, ant2.d)
        else:
            print("Removed")

    except:
        #do nothing pass
        pass