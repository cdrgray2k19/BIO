first = input()
second = input()
grid1 = []
grid2 = []
for char in first:
    if char not in grid1:
        grid1.append(char)
index = len(grid1)
num = 0
for i in range(index, 25):
    while chr(65+num%27) in grid1 or chr(65+num%27) == 'Q':
        num += 1
    grid1.append(chr(65+num%27))
    num += 1

for char in second:
    if char not in grid2:
        grid2.append(char)
index = len(grid2)
num = 0
for i in range(index, 25):
    while chr(65+num%27) in grid2 or chr(65+num%27) == 'Q':
        num += 1
    grid2.append(chr(65+num%27))
    num += 1

temp = grid2
grid2 = []
for i in range(len(temp)-1, -1, -1):
    grid2.append(temp[i])
temp1 = grid1
temp2 = grid2
grid1 = []
grid2 = []
row = []
for i in range(0, len(temp1)):
    print(temp1[i], end=' ')
    row.append(temp1[i])
    if (i+1)%5 == 0:
        print('')
        grid1.append(row)
        row = []
row = []
for i in range(0, len(temp2)):
    print(temp2[i], end=' ')
    row.append(temp2[i])
    if (i+1)%5 == 0:
        print('')
        grid2.append(row)
        row = []
while True:
    order = input()
    if order == 'E':
        arr = list(input())
        string = ''
        if len(arr)%2 == 1:
            arr.append('X')
        for i in range(0, len(arr), 2):
            x1 = 0
            y1 = 0
            x2 = 0
            y2 = 0
            for y in range(0, 5):
                found = False
                for x in range(0, 5):
                    if grid1[y][x] == arr[i]:
                        found = True
                        x1 = x
                        y1 = y
                        break
                if found:
                    break
            for y in range(0, 5):
                found = False
                for x in range(0, 5):
                    if grid2[y][x] == arr[i+1]:
                        found = True
                        x2 = x
                        y2 = y
                        break
                if found:
                    break
            if y1 == y2:
                string += grid1[y1][(x1+1)%5]
                string += grid2[y2][(x2+1)%5]
            else:
                string += grid1[y2][x1]
                string += grid2[y1][x2]
        print(string)
    elif order == 'D':
        arr = list(input())
        string = ''
        for i in range(0, len(arr), 2):
            x1 = 0
            y1 = 0
            x2 = 0
            y2 = 0
            for y in range(0, 5):
                found = False
                for x in range(0, 5):
                    if grid1[y][x] == arr[i]:
                        found = True
                        x1 = x
                        y1 = y
                        break
                if found:
                    break
            for y in range(0, 5):
                found = False
                for x in range(0, 5):
                    if grid2[y][x] == arr[i+1]:
                        found = True
                        x2 = x
                        y2 = y
                        break
                if found:
                    break
            if y1 == y2:
                string += grid1[y1][(x1-1)%5]
                string += grid2[y2][(x2-1)%5]
            else:
                string += grid1[y2][x1]
                string += grid2[y1][x2]
        if string[len(string)-1] == 'X':
            string = string[0:len(string)-1]
        print(string)
    elif order == 'Q':
        break
