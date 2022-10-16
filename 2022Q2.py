rJump, bJump = map(int, input().split())
skirmishNum, feudNum = map(int, input().split())

#create hexagon class
#create skirmish function
#create feud function


#1 for red, -1 for blue

#sum of sides can then be found to see if it is positive then red is in control, if it is negative then blue is control

class Hex:
    def __init__(self):
        self.edges = [0 for _ in range(6)]

hive = []
for y in range(0, 5):
    row = []
    for x in range(0, 5):
        row.append(Hex())
    hive.append(row)


def own(hex, direction, red):
    hexY = int((hex)//5)
    hexX = hex-(5*hexY)
    #current hex that bee is on
    val = -1
    if red:
        val = 1
    hive[hexY][hexX].edges[direction-1] = val
    dy = 0
    dx = 0
    if direction == 1:
        dy = -1
        if hexY%2 == 0:
            dx = 0
        else:
            dx = 1
    elif direction == 2:
        dy = 0
        dx = 1
    elif direction == 3:
        dy = 1
        if hexY%2 == 0:
            dx = 0
        else:
            dx = 1
    elif direction == 4:
        dy = 1
        if hexY%2 == 0:
            dx = -1
        else:
            dx = 0
    elif direction == 5:
        dy = 0
        dx = -1
    elif direction == 6:
        dy = -1
        if hexY%2 == 0:
            dx = -1
        else:
            dx = 0
    if 0 <= hexX + dx < 5 and 0 <= hexY + dy < 5:
        newDir = direction + 3
        while newDir > 6:
            newDir -= 6
        hive[hexY + dy][hexX + dx].edges[newDir-1] = val
    
    return None


def skirmish(redJumps, blueJumps, rounds):
    redHex = 0
    redDir = 1
    blueHex = 24
    blueDir = 6
    while rounds > 0:
        #take ownership of red hex
        own(redHex, redDir, True)
        #change direction
        redDir += 1
        if redDir == 7:
            redDir = 1

        #jump
        redHex += redJumps
        if redHex > 24:
            redHex -= 25
        
        #same for blue

        own(blueHex, blueDir, False)


        #change dir
        blueDir -= 1
        if blueDir == 0:
            blueDir = 6
        

        #jump
        blueHex += blueJumps
        if blueHex > 24:
            blueHex -= 25




        rounds -= 1



def gainedLost(y, x, direction, red):
    if hive[y][x].edges[direction-1] != 0:
        return False
    gaining = 0
    dy = 0
    dx = 0
    if direction == 1:
        dy = -1
        if y%2 == 0:
            dx = 0
        else:
            dx = 1
    elif direction == 2:
        dy = 0
        dx = 1
    elif direction == 3:
        dy = 1
        if y%2 == 0:
            dx = 0
        else:
            dx = 1
    elif direction == 4:
        dy = 1
        if y%2 == 0:
            dx = -1
        else:
            dx = 0
    elif direction == 5:
        dy = 0
        dx = -1
    elif direction == 6:
        dy = -1
        if y%2 == 0:
            dx = -1
        else:
            dx = 0
    
    if sum(hive[y][x].edges) == 0:
        gaining += 1
    if 0 <= x + dx < 5 and 0 <= y + dy < 5:
        if sum(hive[y+dy][x+dx].edges) == 0:
            gaining += 1
    

    losing = 0
    opVal = 1
    if red:
        opVal = -1
    if sum(hive[y][x].edges) == opVal:
        losing += 1
    if 0 <= x + dx < 5 and 0 <= y + dy < 5:
        if sum(hive[y+dy][x+dx].edges) == opVal:
            losing += 1
    
    return gaining, losing

def feuds(rounds):
    #unowned edge
    #so for each colour go through all edges and keep best edge
    while rounds > 0:
    #will be array with gained for theirself, lost for others, hex, and edge
        bestRed = []
        for y in range(0, 5):
            for x in range(0,5):
                for i in range(1, 7):
                    result = gainedLost(y, x, i, True)
                    if result != False:
                        control, lost = result

                        if len(bestRed)==0:
                            bestRed = [control, lost, y*5+x, i]
                        else:
                            if control > bestRed[0]:
                                bestRed = [control, lost, y*5+x, i]
                            elif control == bestRed[0]:
                                if lost > bestRed[1]:
                                    bestRed = [control, lost, y*5+x, i]
        
        own(bestRed[2], bestRed[3], True)

        bestBlue = []
        for y in range(0, 5):
            for x in range(0,5):
                for i in range(1, 7):
                    result = gainedLost(y, x, i, False)
                    if result != False:
                        control, lost = result

                        if len(bestBlue)==0:
                            bestBlue = [control, lost, y*5+x, i]
                        else:
                            if control > bestBlue[0]:
                                bestBlue = [control, lost, y*5+x, i]
                            elif control == bestBlue[0]:
                                if lost > bestBlue[1]:
                                    bestBlue = [control, lost, y*5+x, i]
                                if lost == bestBlue[1]:
                                    bestBlue = [control, lost, y*5+x, i]
        
        own(bestBlue[2], bestBlue[3], False)
    
        rounds -= 1

skirmish(rJump, bJump, skirmishNum)
feuds(feudNum)


red = 0
blue = 0
for y in range(5):
    for x in range(5):
        if sum(hive[y][x].edges) > 0:
            red += 1
        elif sum(hive[y][x].edges) < 0:
            blue += 1
print(red)
print(blue)