#not working for some ships? - go through a solution to one yourself and see where program goes wrong
a, c, m  = map(int, input().split())
r = 0
occupied = []
ships = [4,3,3,2,2,2,1,1,1,1]
while len(ships) > 0:
    currentShip = ships.pop(0)
    placed = False
    while not placed:
        placed = True
        r = ((a*r)+c)%m
        temp = r
        x = temp%10
        temp -= x
        y = (temp%100)/10
        r = ((a*r)+c)%m
        direction = ''
        if r%2 == 0:
            direction = 'H'
        else:
            direction = 'V'
        ship=[]
        for i in range(0, currentShip):
            test = []
            if direction == 'H':
                test = [x+i, y]
            else:
                test = [x, y+i]
            if not (0 <= test[0] <= 10 and 0 <= test[1] <= 10):
                placed = False
                break
            for x_change in range(-1, 2):
                for y_change in range(-1, 2):
                    if [test[0]+x_change, test[1]+y_change] in occupied:
                        placed = False
                        break
                if not placed:
                    break
            if not placed:
                break
            else:
                ship.append(test)
        if placed:
            occupied.extend(ship)
            print(x, int(y), direction)