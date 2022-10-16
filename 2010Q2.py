def move(heading, pos, sides):
    if heading == 0:
        pos[0] -= 1
        tempF = sides['f']
        tempB = sides['b']
        tempU = sides['u']
        tempD = sides['d']
        sides['f'] = tempU
        sides['b'] = tempD
        sides['d'] = tempF
        sides['u'] = tempB
    elif heading == 1:
        pos[1] += 1
        tempL = sides['l']
        tempR = sides['r']
        tempU = sides['u']
        tempD = sides['d']
        sides['l'] = tempD
        sides['r'] = tempU
        sides['d'] = tempR
        sides['u'] = tempL
    elif heading == 2:
        pos[0] += 1
        tempF = sides['f']
        tempB = sides['b']
        tempU = sides['u']
        tempD = sides['d']
        sides['f'] = tempD
        sides['b'] = tempU
        sides['d'] = tempB
        sides['u'] = tempF
    else:
        pos[1] -= 1
        tempL = sides['l']
        tempR = sides['r']
        tempU = sides['u']
        tempD = sides['d']
        sides['l'] = tempU
        sides['r'] = tempD
        sides['d'] = tempL
        sides['u'] = tempR

    return pos, sides

sides = {'f':2, 'b':5, 'l':3, 'r':4, 'u':1, 'd':6}

#0 is up, 1 is right, 2 is down, 3 is left
heading = 0

pos = [5, 5]

#11 by 11 all 1 apart from middle block of 9
grid = []
for i in range(0,11):
    row = []
    for j in range(0,11):
        row.append(1)
    grid.append(row)
for i in range(0, 3):
    row = list(map(int, input().split()))
    for j in range(0, 3):
        grid[4+i][4+j] = row[j]
while True:
    moves = int(input())
    print('')
    if moves == 0:
        break
    while moves > 0:
        grid[pos[0]][pos[1]] = ((grid[pos[0]][pos[1]] + sides['u']))
        if grid[pos[0]][pos[1]] > 6:
            grid[pos[0]][pos[1]] -= 6
        val = grid[pos[0]][pos[1]]
        if val == 1 or val == 6:
            pos, sides = move(heading, pos, sides)
        elif val == 2:
            heading = (heading + 1)%4
            pos, sides = move(heading, pos, sides)
        elif val == 3 or val == 4:
            heading = (heading + 2)%4
            pos, sides = move(heading, pos, sides)
        else: #val = 5
            heading = (heading - 1)%4
            pos, sides = move(heading, pos, sides)
        if pos[0] > 10:
            pos[0] -= 11
        elif pos[0] < 0:
            pos[0] += 11
        if pos[1] > 10:
            pos[1] -= 11
        elif pos[1] < 0:
            pos[1] += 11
        moves -= 1
    #print 3 by 3 around die
    for i in range(0, 3):
        for j in range(0, 3):
            y = pos[0] - 1 + i
            x = pos[1] - 1 + j
            if 0 <= y <= 10 and  0 <= x <= 10:
                print(grid[y][x], end=' ')
            else:
                print('x', end=' ')
        print('')
    print('')