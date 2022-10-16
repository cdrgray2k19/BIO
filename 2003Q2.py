from collections import defaultdict
from copy import deepcopy
class Wave:
    def __init__(self, center, height):
        self.center = center
        self.height = height
        self.points = [tuple(center)]
        self.time = 0
    
    def calc(self):
        self.time += 1
        new = []
        if self.time == 1:
            #start the four points
            for x, y in [(1, 0), (-1, 0), (0,1), (0,-1)]:
                new.append((x,y))
        else:
            #wave allready started, push out waves with adding one to x unless directly under or above wave
            for x,y in self.points:
                if x == self.center[0]:
                    if y > self.center[1]:
                        y += 1
                    else:
                        y -= 1
                    new.append((x,y))
                else:
                    if x > self.center[0]:
                        x += 1
                    else:
                        x -= 1
                    new.append((x,y))
            
            for dx, dy in [(1, self.time-1), (1, -self.time+1), (-1, self.time-1), (-1, -self.time+1)]:
                if dy != 0:
                    new.append((self.center[0]+dx, self.center[1]+dy))
    
        self.points = new.copy()

    def convert(self, river1, river2):
        #just convert points so that any overlapping with x's bounce off
        maxRight = 0
        maxLeft = 0
        center = self.center[0]
        if river1 > center and river2 > center:
            maxRight = min(river1, river2)
            maxLeft = 1000000000
        elif river1 < center and river2 < center:
            maxRight = 1000000000
            maxLeft = max(river1,river2)
        else:
            maxLeft = min(river1,river2)
            maxRight = max(river1, river2)
        new = []
        for x,y in self.points:
            while x >= maxRight or x <= maxLeft:
                if x >= maxRight:
                    x = maxRight-(x-maxRight)-1
                elif x <= maxLeft:
                    x = maxLeft+(maxLeft-x)+1
            new.append((x,y))
        
        return new

'''
w = Waves([0,0], 1)
w.calc()
w.calc()
w.calc()
result = w.convert(-100, 100)

for y in range(-3, 4):
    for x in range(-3, 4):
        if (x,y) in result:
            print('*', end='')
        else:
            print('-', end='')
    print('')
'''
p = int(input())
pebbles = []
for _ in range(p):
    new = list(map(int, input().split()))
    new.append(1)
    pebbles.append(new)
banks = list(map(int, input().split()))
r = int(input())
print(pebbles)

time = 1
currentWaves = []
while time < r:

    for w in currentWaves:
        w.calc()

    newPebbles = deepcopy(pebbles)
    for i in range(0, len(pebbles)):
        if pebbles[i][2] == time:
            newWave = newPebbles.pop(i)
            obj = Wave([newWave[0], newWave[1]], newWave[3])
            currentWaves.append(obj)
            if newWave[3] == 1:
                newPebbles.append([newWave[0], newWave[1], time+2, -1])
    
    time += 1

total = defaultdict(int)
for w in currentWaves:
    result = w.convert(banks[0], banks[1])
    for x, y in result:
        total[(x,y)] += w.height

for y in range(-4, 5):
    for x in range(-4, 5):
        if x in banks:
            print('X', end='')
        else:
            if total[(x,y)] > 0:
                print('*', end='')
            elif total[(x,y)] < 0:
                print('O', end='')
            else:
                print('-', end='')
    print('')