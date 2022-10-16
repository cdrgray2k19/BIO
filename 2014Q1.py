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