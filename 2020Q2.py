class Room:
    def __init__(self, visits):
        self.exits = {}
        self.visits = visits
    def addExit(self, exit):
        if exit not in self.exits:
            self.exits[exit] = 0
    #increment visits after exits?
    def move(self):
        e = ''
        self.visits += 1
        if self.visits%2 == 0:
            vals = sorted(self.exits)
            for i in range(0, len(vals)):
                if self.exits[vals[i]]%2 == 1:
                    if i == len(vals)-1:
                        e = vals[i]
                        break
                    else:
                        e = vals[i+1]
                        break

        else:
            e = min(self.exits)
        
        self.exits[e] += 1
    
        return e


plan, p, q = input().split()
p = int(p)
q = int(q)
plan = list(plan)
n = len(plan) + 2

rooms = {}

#got not chosen to intiliase rooms
notChosen = []
for i in range(n):
    if chr(i + ord('A')) not in plan:
        notChosen.append(chr(i + ord('A')))


#set up room objects
for i in range(0, len(plan)):
    if plan[i] in rooms:
        continue
    rooms[plan[i]] = Room(0)
for i in range(0, len(notChosen)):
    rooms[notChosen[i]] = Room(0)

chosen = set()

while len(plan) > 0:
    toAdd1 = notChosen.pop(notChosen.index(min(notChosen)))
    toAdd2 = plan.pop(0)
    rooms[toAdd1].addExit(toAdd2)
    rooms[toAdd2].addExit(toAdd1)
    chosen.add(toAdd1)
    if (toAdd2 not in plan) and (toAdd2 not in chosen):
        notChosen.append(toAdd2)

rooms[notChosen[0]].addExit(notChosen[1])
rooms[notChosen[1]].addExit(notChosen[0])

#intiliased rooms


#print rooms
temp = rooms.copy()
while len(temp) > 0:
    r = temp.pop(min(temp))
    print(''.join(sorted(r.exits.keys())))

current = 'A'
moves = 0

stringToPrint = ''

while moves < q:
    if moves == p:
        stringToPrint += current
    
    current = rooms[current].move()
    
    moves += 1


stringToPrint += current
print(stringToPrint)

#

#add up all exits