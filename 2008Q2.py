n = int(input())
s = list(map(lambda x:int(ord(x)-ord("A")), input()))

class rotor:
    #simulate wire connections, changes in index
    changes = []
    def __init__(self, changes):
        self.changes = changes
    def rotate(self, times):
        times %= 4
        for i in range(0, times):
            start = self.changes.pop(0)
            self.changes.append(start)
    def encrypt(self, num):
        change = self.changes[num]
        num += change
        num %= 4
        return num
    def reflect(self, num):
        for i in range(0, len(self.changes)):
            if (i+self.changes[i])%4 == num:
                return i
        assert False, "reflect not found"

r1 = rotor([0, 2, -1, -1])
r2 = rotor([0, 1, -1, 0])

r1.rotate(n)
r2.rotate(n//4)
rotations = n%4

encrypted = ""
rotations = n
for i in range(0, len(s)):
    num = s[i]
    num = r1.encrypt(num)
    num = r2.encrypt(num)
    reflectedNum = 3-num
    num = r2.reflect(reflectedNum)
    num = r1.reflect(num)
    char = chr(ord("A")+num)
    encrypted += char
    r1.rotate(1)
    rotations += 1
    if rotations%4 == 0:
        r2.rotate(1)

print(encrypted)
#BCBCDB