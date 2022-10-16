first, second, moves = input().split()
first = ord(first) - 64
second = ord(second) - 64
moves = int(moves) - 2
while moves > 0:
    val = first + second
    if val > 26:
        val -= 26
    temp = second
    second = val
    first = temp
    moves -= 1
print(chr(second+64))