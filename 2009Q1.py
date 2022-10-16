word = list(input())

words = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

printed = False
for i in range(0, len(words)):
    next = 0
    found = False
    for c in word:
        if c == words[i][next]:
            next += 1
        if next == len(words[i]):
            found = True
            print(i+1)
            printed = True
            break
    if found:
        break

if not printed:
    print('NO')