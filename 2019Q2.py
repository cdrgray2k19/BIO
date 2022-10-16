n, instr, m = input().split()
n = int(n)
m = int(m)
done = False
index = 0
trail = [(0, 0)]
facing = 0
pos = [0, 0]


while not done:
    if m <= 1:
        done = True
    order = instr[index%len(instr)]
    if order == 'L':
        facing -= 1
    elif order == 'R':
        facing += 1
    facing %= 4
    
    tries = 0
    trying = True
    while trying:
        if tries == 4:
            done = True
            trying = False
        if facing == 0:
            temp = [pos[0], pos[1]+1]
            if tuple(temp) not in trail:
                pos = temp
                trying = False
            else:
                tries += 1
                facing += 1
                facing %= 4
        elif facing == 1:
            temp = [pos[0]+1, pos[1]]
            if tuple(temp) not in trail:
                pos = temp
                trying = False
            else:
                tries += 1
                facing += 1
                facing %= 4
        elif facing == 2:
            temp = [pos[0], pos[1]-1]
            if tuple(temp) not in trail:
                pos = temp
                trying = False
            else:
                tries += 1
                facing += 1
                facing %= 4
        elif facing == 3:
            temp = [pos[0]-1, pos[1]]
            if tuple(temp) not in trail:
                pos = temp
                trying = False
            else:
                tries += 1
                facing += 1
                facing %= 4
        
    trail.insert(0, tuple(pos))
    if len(trail) > n:
        trail.pop()
    m -= 1
    index += 1

print(tuple(pos))