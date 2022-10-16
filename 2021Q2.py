#too complicated, didnt need to store triangle class can all be done in x,y plain

from collections import defaultdict
from copy import deepcopy
p, m = map(int, input().split())

#create start triangle

triangles = defaultdict(int)

class Tri:
    def __init__(self, pointUp, player, x, y):
        self.pointUp = pointUp
        self.x = x
        self.y = y
        self.player = player
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.updateSides()
    
    def updateSides(self):
        self.left = triangles[(self.x-1, self.y)]
        try:
            triangles[(self.x-1, self.y)].right = self
        except:
            pass
        self.right = triangles[(self.x+1, self.y)]
        try:
            triangles[(self.x+1, self.y)].left = self
        except:
            pass
        if not self.pointUp:
            self.up = triangles[(self.x, self.y-1)]
            self.down = None
            try:
                triangles[(self.x, self.y-1)].down = self
            except:
                pass
        else:
            self.up = None
            self.down = triangles[(self.x, self.y+1)]
            try:
                triangles[(self.x, self.y+1)].up = self
            except:
                pass
    def updateAfter(self):
        self.left = triangles[(self.x-1, self.y)]
        try:
            triangles[(self.x-1, self.y)].right = self
        except:
            pass
        self.right = triangles[(self.x+1, self.y)]
        try:
            triangles[(self.x+1, self.y)].left = self
        except:
            pass
        if not self.pointUp:
            self.up = triangles[(self.x, self.y-1)]
            self.down = None
            try:
                triangles[(self.x, self.y-1)].down = self
            except:
                pass
        else:
            self.up = None
            self.down = triangles[(self.x, self.y+1)]
            try:
                triangles[(self.x, self.y+1)].up = self
            except:
                pass

triangles[(0, 0)] = Tri(True, 0, 0, 0)


#initialise player

playerTraverals = list(map(int, input().split()))
#number of 2 by 2 triangles filled in
playerScores = [0 for _ in range(p)]
#keeps track of what edge each player is on
playerPositions = [[(0, 0), 'left'] for _ in range(p)]

topLeft = (0, 0)



#start loop
    #for number of traversals
        #for player check if on valid edge, if not then move
        #then move to next edge which will be function
        #then check edge for adding a point which will be function
        #then minus one from number of traversals
    #then move onto next player and minus one from number of moves


#then print out scores
#then start at topleft edge and traverse until topleft is found again using the move to next edge function
#print out number of edges in perimeter

def checkPosition(trianglePos, dir):
    triangle = triangles[trianglePos]
    if dir == 'left':
        return triangle.left == 0
    elif dir == 'right':
        return triangle.right == 0
    elif dir == 'up':
        return triangle.up == 0
    elif dir == 'down':
        return triangle.down == 0

def moveEdge(trianglePos, dir):
    newEdge = rotate(trianglePos, dir)
    triangle = triangles[trianglePos]
    if newEdge == 'left':

        if triangle.left == 0:
            return trianglePos, 'left'
        else:
            x, y = trianglePos
            return moveEdge((x-1, y), 'right')

    elif newEdge == 'right':

        if triangle.left == 0:
            return trianglePos, 'right'
        else:
            x, y = trianglePos
            return moveEdge((x+1, y), 'left')

    elif newEdge == 'up':

        if triangle.left == 0:
            return trianglePos, 'up'
        else:
            x, y = trianglePos
            return moveEdge((x, y-1), 'down')
        

    elif newEdge == 'down':

        if triangle.left == 0:
            return trianglePos, 'down'
        else:
            x, y = trianglePos
            return moveEdge((x, y+1), 'up')


def rotate(trianglePos, dir):
    if dir == 'left':
        if triangles[trianglePos].up == None:
            return 'right'
        else:
            return 'up'
    elif dir == 'right':
        if triangles[trianglePos].down == None:
            return 'left'
        else:
            return 'down'
    elif dir == 'up':
        return 'right'
    else:
        return 'left'

def checkScore(player, dictionary):
    #for each triangle go up to check if triangle can be made up and same with down, then check left and right and append to total if all are filled by the same player
    total = 0
    for pos in dictionary.copy():
        x, y = pos
        if dictionary[(x, y-1)] != 0 and dictionary[(x-1, y)] != 0 and dictionary[(x+1, y)] != 0:
            if dictionary[(x, y-1)].pointUp == dictionary[(x+1, y)].pointUp == dictionary[(x-1, y)].pointUp and dictionary[(x, y-1)].player == dictionary[(x-1, y)].player == dictionary[(x+1, y)].player:
                if dictionary[(x, y-1)].player == player:
                    total += 1

        if dictionary[(x, y+1)] != 0 and dictionary[(x-1, y)] != 0 and dictionary[(x+1, y)] != 0:
            if dictionary[(x, y+1)].pointUp == dictionary[(x+1, y)].pointUp == dictionary[(x-1, y)].pointUp and dictionary[(x, y+1)].player == dictionary[(x+1, y)].player == dictionary[(x-1, y)].player:
                if dictionary[(x, y+1)].player == player:
                    total += 1
    return total


def complete(trianglePos, dir, currPlayer):
    temp = deepcopy(triangles)
    x, y = trianglePos
    if dir == 'left':
        x -= 1
    elif dir == 'right':
        x += 1
    elif dir == 'up':
        y -= 1
    elif dir == 'down':
        y += 1
    temp[(x,y)] = Tri(not temp[trianglePos].pointUp, currPlayer, x, y)
    score = checkScore(currPlayer, temp)
    if score > playerScores[currPlayer-1]:
        return True
    
    return False

def addNew(trianglePos, dir, currentPlayer, topLeft):
    temp = triangles.copy()
    x, y = trianglePos
    if dir == 'left':
        x -= 1
    elif dir == 'right':
        x += 1
    elif dir == 'up':
        y -= 1
    elif dir == 'down':
        y += 1
    temp[(x,y)] = Tri(not temp[trianglePos].pointUp, currentPlayer, x, y)
    bigX, bigY = topLeft
    if y < bigY:
        topLeft = (x,y)
    if y == bigY and x < bigX:
        topLeft = (x,y)
    return temp, topLeft
        

currentPlayer = 1
while m > 0:

    if not checkPosition(playerPositions[currentPlayer-1][0], playerPositions[currentPlayer-1][1]):
            playerPositions[currentPlayer-1] = [topLeft, 'left']
        
    toAdd = playerPositions[currentPlayer-1]

    for _ in range(playerTraverals[currentPlayer-1]):
        #check if valid
        playerPositions[currentPlayer-1] = list(moveEdge(playerPositions[currentPlayer-1][0], playerPositions[currentPlayer-1][1]))
        #found edge to add onto
        #now just need to see if it will add another point
        if complete(playerPositions[currentPlayer-1][0], playerPositions[currentPlayer-1][1], currentPlayer):
            toAdd = playerPositions[currentPlayer-1]
            playerScores[currentPlayer-1] += 1
    
        for pos in triangles:
            x, y = pos
            try:
                triangles[(x,y)].updateAfter()
            except:
                pass
        

    
    triangles, topLeft = addNew(*toAdd, currentPlayer, topLeft)





    currentPlayer += 1
    if currentPlayer > p:
        currentPlayer = 1
    m -= 1

for scores in playerScores:
    print(scores)

position = (topLeft, 'left')
visited = set()
edges = 0
while position not in visited:
    visited.add(position)
    position = tuple(moveEdge(*list(position)))
    edges += 1
print(edges)