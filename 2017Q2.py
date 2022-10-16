pos1, m1, pos2, m2, t = map(int, input().split())

edges = set()

firstSquares = set()

secondSquares = set()

def move(position, modifier, firstPlayer):
    #each player has different way of testing if they can add edge, so configure acording to player the array which they will have
    #then add a modifier and then test position, if position is found, then add to edges and test for square
    #then return true if square false if not and position of player
    edgeDif = [-6, -1, 6, 1]
    if firstPlayer:
        edgeDif = [-6, 1, 6, -1]
    
    pos = position
    m = modifier
    pos += m
    while True:

        while pos > 36:
            pos -= 36

        for offSet in edgeDif:
            if 0 < pos + offSet <= 36:
                if offSet in [1, -1] and (pos-1)//6 != (pos + offSet-1)//6:
                    continue
                
                points = [pos, pos+offSet]
                edge = (min(points), max(points))
                if edge in edges:
                    continue
                #if here then edge can be added
                edges.add(edge)
                added = checkSquares(edge, firstPlayer)
                if added:
                    return True, pos
                else:
                    return False, pos
        


        pos += 1

def checkSquares(edge, firstPlayer):
    #see if edge if horizontal or vertical
    #then check squares one up or down or one left and right
    #if square found then return top left corner
    
    added = False
    small, large = edge
    if (large - small) == 6:

        #square to the left

        testEdges = [(small-1, large-1), (large-1, large), (small-1, small)]

        add = True
        for edge in testEdges:
            if edge not in edges:
                add = False

        if add:
            added = True
            corner = small-1
            if firstPlayer:
                firstSquares.add(corner)
            else:
                secondSquares.add(corner)
        


        #square to the right

        testEdges = [(small+1, large+1), (large, large+1), (small, small+1)]

        add = True
        for edge in testEdges:
            if edge not in edges:
                add = False

        if add:
            added = True
            corner = small
            if firstPlayer:
                firstSquares.add(corner)
            else:
                secondSquares.add(corner)

    else:

        #square above

        testEdges = [(small-6, small), (large-6, large), (small-6, large-6)]

        add = True
        for edge in testEdges:
            if edge not in edges:
                add = False

        if add:
            added = True
            corner = small-6
            if firstPlayer:
                firstSquares.add(corner)
            else:
                secondSquares.add(corner)

        #square below

        

        testEdges = [(small, small+6), (large, large+6), (small+6, large+6)]

        add = True
        for edge in testEdges:
            if edge not in edges:
                add = False

        if add:
            added = True
            corner = small
            if firstPlayer:
                firstSquares.add(corner)
            else:
                secondSquares.add(corner)
    
    return added

first = True

while t > 0:
    if first:
        added, newPos = move(pos1, m1, first)
        pos1 = newPos
    else:
        added, newPos = move(pos2, m2, first)
        pos2 = newPos
    
    if not added:
        first = not first
    
    t -= 1


for i in range(1, 31):
    if i in firstSquares:
        print('X', end='')
    elif i in secondSquares:
        print('O', end='')
    elif i%6 == 0:
        print('')
    else:
        print('*', end='')

print(len(firstSquares), len(secondSquares))

#23