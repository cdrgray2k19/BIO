s = input()
x = float(s)
a = float(x*(10**(len(s)-2)))
b = float(10**(len(s)-2))
done = True
while done:
    done = False
    if (a/5)%1 == 0:
        a /= 5
        b /= 5
        done = True
    if (a/2)%1 == 0:
        a /= 2
        b /= 2
        done = True


print(int(a), '/', int(b))