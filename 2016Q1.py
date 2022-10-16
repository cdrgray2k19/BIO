l = 1
m = 0
r = 0
s = 1
up = 1
down = 1
string = input()
for char in string:
    if char == 'L':
        l = up
        m = down
        up = l + r
        down = m + s
    else:
        r = up
        s = down
        up = l+r
        down = m + s
    done = False
    while not done:
        done = True
        for i in range(2, int(up)):
            if down%i == 0 and up%i == 0:
                up /= i
                down /= i
                done = False
                break
print(str(up) + ' / ' + str(down))