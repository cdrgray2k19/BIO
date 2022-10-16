#have a chase the lights function, have  brute force function that reference chase the lights function
#somethings going wrong
string = input()
vals = []
for i in range(0, 5):
    row = []
    for j in range(0, 5):
        if chr(i*5 + j + ord('A')) in string:
            row.append(2)
        elif chr(i*5 + j + ord('a')) in string:
            row.append(1)
        else:
            row.append(0)
    vals.append(row)

pressed = [0 for _ in range(25)]

def press(arr, pos, presses):
    temp = arr.copy()
    if presses == 0:
        return temp
    y, x = pos
    for dy, dx in [(1, 0), (0, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= y+dy < 5 and 0 <= x+dx < 5:
            temp[y+dy][x+dx] = (temp[y+dy][x+dx] + presses)%3
    return temp

def chaseLights(arr, pressed):
    for y in range(1, 5):
        for x in range(0, 5):
            presses = (3-arr[y-1][x])%3
            arr = press(arr, (y, x), presses)
            pressed[y*5 + x] += presses
    return arr, pressed

def done(arr):
    for y in range(0, 5):
        if sum(arr[i]) > 0:
            return False
    return True

def combinations(arr, pressed, xPos):
    if xPos < 5:
        for p in range(0, 3):
            temp = arr.copy()
            temp = press(temp, (0, xPos), p)
            tempPressed = pressed.copy()
            tempPressed[xPos] += p
            found = combinations(temp, tempPressed, xPos+1)
    else:
        temp = arr.copy()
        tempPressed = pressed.copy()
        
        temp,tempPressed = chaseLights(temp, tempPressed)
        if done(temp):
            print(convert(pressed))

        
    
    return False

def convert(pressed):
    string = ''
    for i in range(0, len(pressed)):
        if pressed[i] == 1:
            string += chr(i+ord('a'))
        elif pressed[i] == 2:
            string += chr(i+ord('A'))
    return string

chaseLights(vals, pressed)
if done(vals):
    print(convert(pressed))
else:
    if combinations(vals, pressed, 0) == False:
        print('IMPOSSIBLE')