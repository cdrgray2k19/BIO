"""
import time
start = time.time()
l = []
arr = []
n = int(input())
for i in range(1, 2*n, 2):
    arr.append(i)
index = 1
while True:
    num = arr[index]
    l.append(num)
    if num > n:
        val1 = l[len(l)-1]
        if l[len(l)-2] == n:
            val2 = l[len(l)-3]
        else:
            val2 = l[len(l)-2]
        print(val2, val1)
        break
    x = 0

    while (x + num - 1) < len(arr):
        temp = x + num - 1
        arr.pop(temp)
        x = temp
    index += 1

end = time.time()
print(end-start)

"""
import time
start = time.time()
n = int(input())
odds = []
for i in range(0, n):
    odds.append(i*2+1)

index = 0
beforeFound = False
toPrint = []
while True:
    save = odds[index]
    index += 1
    num = odds[index]
    if beforeFound:
        toPrint.append(num)
        break
    if num == n:
        toPrint.append(save)
        beforeFound = True
    if num > n:
        toPrint.append(save)
        toPrint.append(num)
        break

    ind = -1
    while ind+num < len(odds):
        div = ind+num
        odds.pop(div)
        ind = div
        ind -= 1

for n in toPrint:
    print(str(n)+" ", end="")
print("")
end = time.time()
print(end-start)
#"""