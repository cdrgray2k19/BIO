class lazy:
    def __init__(self, stations) -> None:
        s, left, right = (stations[0], stations[1], stations[2])
        self.current= left
        self.other = right
        self.straight = s

    def enter(self, direction):
        if direction == self.straight:
            return self.current
        elif direction == self.current:
            return self.straight
        else:

            temp = self.other
            self.other = self.current
            self.current = temp

            return self.straight

class flipFlop:
    def __init__(self, stations) -> None:
        s, left, right = (stations[0], stations[1], stations[2])
        self.current = left
        self.other = right
        self.straight = s

    def enter(self, direction):
        if direction == self.straight:

            temp = self.other
            self.other = self.current
            self.current = temp

            return self.other
        else:
            return self.straight


#have letters for station and their corresponding objects
points = {}
#station with straigh point, left point, then right point
links = {'A': 'DEF', 'B': 'CGH', 'C': 'BIJ', 'D': 'AKL', 'E': 'AMN', 'F': 'ANO', 'G': 'BOP', 'H': 'BPQ', 'I': 'CQR', 'J': 'CRS', 'K': 'DST', 'L': 'DTM', 'M': 'ULE', 'N': 'UEF', 'O': 'VFG', 'P': 'VGH', 'Q': 'WHI', 'R': 'WIJ', 'S': 'XJK', 'T': 'XKL', 'U': 'VMN', 'V': 'UOP', 'W': 'XQR', 'X': 'WST'}
flipflops = input()
for i in range(0, 24):
    c = chr(ord('A')+i)
    if c in flipflops:
        linkedStations = links[c]
        points[c] = flipFlop(linkedStations)
    else:
        linkedStations = links[c]
        points[c] = lazy(linkedStations)

current = input()
moves = int(input())
while moves > 0:

    previous = current[0]
    next = current[1]
    #get point object of next and set direction to previous

    newPoint = points[next].enter(previous)
    #get next point
    #update current so that we can print it out or get points to manage it with
    current = next + newPoint
    moves -= 1

print(current)

#?

#passed through all points

#8