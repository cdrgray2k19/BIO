import math
a, b, c, d, n = map(int, input().split())
nums = [a, b, c, d]
result = []

while sum(nums) > 0:
    lastTotal = 0
    total = 0
    for i in range(0, 4):
        lastTotal = total
        if nums[i] > 0:
            nums[i] -= 1
            count = 0
            count = (math.factorial(sum(nums)))
            for j in range(0, 4):
                if nums[j] > 1:
                    count /= math.factorial(nums[j])
            nums[i] += 1
            total += count
            if total >= n:
                result.append(chr(65+i))
                nums[i] -= 1
                break
    n -= lastTotal

print(''.join(result))