increment, msg = input().split()
increment = int(increment)
msg = msg.upper()
alphabet = []
second = []
for i in range(0, 26):
    alphabet.append(chr(i+65))
first = alphabet.copy()
num = -1
while len(alphabet) > 0:
    num += increment
    num %= len(alphabet)
    second.append(alphabet[num])
    alphabet.pop(num)
    num -= 1
newMsg = ''
for i in range(0, len(msg)):
    newMsg += second[(first.index(msg[i]) + i)%26]
print(second[0:6])
print(newMsg)