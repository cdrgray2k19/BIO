from collections import defaultdict
squares = defaultdict(int)
def migrate(pos, squares):
    squares[pos] += 1
    if squares[pos] == 4:
        squares[pos] = 0
        squares = migrate((pos[0]-1, pos[1]), squares)
        squares = migrate((pos[0]+1, pos[1]), squares)
        squares = migrate((pos[0], pos[1]-1), squares)
        squares = migrate((pos[0], pos[1]+1), squares)

    return squares

p,s,n = map(int, input().split())
seq = list(map(int, input().split()))
index = 0
while n > 0:
    y = (p-1)//5
    x = (p-1)%5
    squares = migrate((y, x), squares)

    p += seq[index]
    if p > 25:
        p -= 25
    index += 1
    index %= s
    n -= 1
for y in range(0, 5):
    for x in range(0, 5):
        print(squares[(y,x)], end=' ')
    print('')