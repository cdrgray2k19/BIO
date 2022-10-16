nums = []
n = input()
arr = []
for i in range(0, 10):
    arr.append(n.count(str(i)))
for i in range(2, 10):
    temp=[]
    new = int(n)*i
    for j in range(0, 10):
        temp.append(str(new).count(str(j)))
    if arr == temp:
        nums.append(i)

if len(nums) == 0:
    print('NO')
else:
    for v in nums:
        print(v, end=' ')