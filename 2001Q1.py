#test
f = int(input())
friends = [i for i in range(0, f)]
words = int(input())
index = 0
while len(friends) > 1:
    index += words - 1
    index %= len(friends)
    friends.pop(index)
print(friends[0]+1)