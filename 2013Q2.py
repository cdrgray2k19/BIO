firstOrder = list(map(int, input().split()))
secondOrder = list(map(int, input().split()))

firstIndex = -1
secondIndex = -1

playing = True
firstPieces = [[i, 4] for i in range(5)]
secondPieces = [[i, 0] for i in range(5)]
n = [2,2]

firstPlayerMove = True

printFirst = True
printSecond = True

def getMoves(pos):
    moves = []
    for i in range(0,8):
        temp = pos.copy()
        lastLegal = temp.copy()
        done = False
        while not done:
            xChange = 0
            yChange = 0
            if i+1 in [2, 3, 4]:
                xChange = 1
            if i+1 in [4, 5, 6]:
                yChange = 1
            if i+1 in [6, 7, 8]:
                xChange = -1
            if i+1 in [8, 1, 2]:
                yChange = -1
            temp[0] += xChange
            temp[1] += yChange
            if temp not in firstPieces and temp not in secondPieces and temp != n and 0 <= temp[0] <= 4 and 0 <= temp[1] <= 4:
                lastLegal = temp.copy()
            else:
                done = True
        if lastLegal != pos:
            moves.append(lastLegal.copy())
    return moves


while playing:
    piece = 0
    if firstPlayerMove:
        #gives index of the piece we need to move
        firstIndex += 1
        piece = firstOrder[firstIndex%5] - 1
    else:
        secondIndex += 1
        piece = secondOrder[secondIndex%5] - 1
    
    nMoves = getMoves(n)

    if len(nMoves) == 0:
        break
    
    #if can win then win and stop playing
    winYCoord = 0
    if firstPlayerMove:
        winYCoord = 4
    for i in range(0, len(nMoves)):
        if nMoves[i][1] == winYCoord:
            n = nMoves[i]
            playing = False
            break
    
    if not playing:
        break

    #else if only moves are losing then play first move
    loseYCoord = 4
    if firstPlayerMove:
        loseYCoord = 0


    definiteLoss = True


    for i in range(0, len(nMoves)):
        if nMoves[i][1] != loseYCoord:
            definiteLoss = False
            break


    if definiteLoss:
        n = nMoves[0]
        playing = False

    if not playing:
        break
    
    #else move neutron and then move piece
    original = n
    for i in range(0, len(nMoves)):
        n = nMoves[i]
        if nMoves[i][1] != loseYCoord:
            if firstPlayerMove:
                movesAvaillable = getMoves(firstPieces[piece])
                if movesAvaillable != []:
                    firstPieces[piece] = movesAvaillable[0]
                    break
                else:
                    n = original
            else:
                movesAvaillable = getMoves(secondPieces[piece])
                if movesAvaillable != []:
                    secondPieces[piece] = movesAvaillable[0]
                    break
                else:
                    n = original

        else:
            n = original
    
    #move made

    if printFirst:
        for y in range(5):
            for x in range(5):
                if [x,y] in firstPieces:
                    print('F', end='')
                elif [x,y] in secondPieces:
                    print('S', end='')
                elif [x,y] == n:
                    print('*', end='')
                else:
                    print('.', end='')
            print('')
        printFirst = False
    elif printSecond:
        for y in range(5):
            for x in range(5):
                if [x,y] in firstPieces:
                    print('F', end='')
                elif [x,y] in secondPieces:
                    print('S', end='')
                elif [x,y] == n:
                    print('*', end='')
                else:
                    print('.', end='')
            print('')
        printSecond = False


    firstPlayerMove = not firstPlayerMove

for y in range(5):
    for x in range(5):
        if [x,y] in firstPieces:
            print('F', end='')
        elif [x,y] in secondPieces:
            print('S', end='')
        elif [x,y] == n:
            print('*', end='')
        else:
            print('.', end='')
    print('')