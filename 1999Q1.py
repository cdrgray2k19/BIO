n = int(input())


def river(n, order):
    history = set()
    for i in range(0, order):
        s = str(n)
        history.add(n)
        total = 0
        for c in s:
            total += int(c)
        n += total
    return history

one = river(1, 100000)
three = river(3, 100000)
nine = river(9, 100000)

while True:
    if n in one:
        print("first meets river 1 at", n)
        break
    if n in three:
        print("first meets river 3 at", n)
        break
    if n in nine:
        print("first meets river 9 at", n)
        break
    s = str(n)
    total = 0
    for c in s:
        total += int(c)
    n += total