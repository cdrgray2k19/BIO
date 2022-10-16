n = int(input())
n += 1
n = str(n)

def odd(n):
    n = str(n)
    if len(n) == 1:
        return n
    left = n[0:len(n)//2]
    mid = n[len(n)//2]
    right = n[len(n)//2+1:]
    if right > left[::-1]:
        n = int(n) + 10**(len(n)//2)
        if len(str(n))%2 == 0:
            return even(n)
        return(odd(n))
    else:
        return left + mid + left[::-1]

def even(n):
    n = str(n)
    left = n[0:len(n)//2]
    right = n[len(n)//2:]
    if right > left[::-1]:
        n = int(n) + 10**(len(n)//2)
        if len(str(n))%2 == 1:
            return odd(n)
        return even(n)
    else:
        return left + left[::-1]

if len(n)%2 == 1:
    print(odd(n))
else:
    print(even(n))