n = int(input())
#dont need to find primes just from 2 to square root of number dividing by anything that goes into n, if total is 1 then n is prime

nums = [True for i in range(0, n+1)] #generates array of falses representing numbers from 0 - 1000000 inclusive
nums[0] = False
nums[1] = False
for i in range(2, len(nums)):
    for j in range(i+i, len(nums), i):
        nums[j] = False
#nums now contains true if prime
if nums[n]:
    print(n)
else:
    factors = []

    for i in range(0, len(nums)):
        if n == 1:
            break
        if nums[n]:
            factors.append(n)
            break
        if nums[i] == False:
            continue
        if n%i == 0:
            factors.append(i)
        while n%i == 0:
            n /= i
        n = int(n)

    total = 1
    for val in factors:
        total *= val
    print(total)

#10, 20, 40, 50, 80, 100, 160, 320, 500, 640

#210