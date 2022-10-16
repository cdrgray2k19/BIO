def bre(cards):
    new = cards.copy()
    top = new.pop(0)
    new.append(top)
    return new

def outer(cards):
    first = cards[0:4]
    second = cards[4:]
    new = []
    while first:
        new.append(first.pop(0))
        new.append(second.pop(0))
    return new

def inner(cards):
    first = cards[4:]
    second = cards[0:4]
    new = []
    while first:
        new.append(first.pop(0))
        new.append(second.pop(0))
    return new

def do(times, instr, cards):
    pack = cards.copy()
    for _ in range(0, int(times)):
        num = 1
        start = False
        string = ''
        openCount = 0
        closeCount = 0
        for i in range(0, len(instr)):
            c = instr[i]
            if c.isdigit():
                if start:
                    string += c
                else:
                    num = int(c)
            elif c == 'b':
                if start:
                    string += c
                else:
                    for _ in range(0, num):
                        pack = bre(pack)
                    num = 1
            elif c == 'i':
                if start:
                    string += c
                else:
                    for _ in range(0, num):
                        pack = inner(pack)
                    num = 1
            elif c == 'o':
                if start:
                    string += c
                else:
                    for _ in range(0, num):
                        pack = outer(pack)
                    num = 1
            elif c == '(':
                openCount += 1
                if start:
                    string += c
                else:
                    start = True
            elif c == ')':
                closeCount += 1
                if openCount == closeCount:
                    closeCount = 0
                    openCount = 0
                    pack = do(num, string, pack)
                    start = False
                    string = ''
                    num = 1
                else:
                    string += c

            
    return pack





instr = input()

cards = [i+1 for i in range(8)]

print(do(1, instr, cards))

#[12, 17, 2, 7, 13, 18, 3, 8, 14, 19, 4, 9, 15, 20, 5, 10, 16, 1, 6, 11]

#6, 3, 8