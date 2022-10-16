inc1, inc2 = map(int, input().split())
t1 = 0
t2 = 0
done = False
while not done:
    t1 += 60 + inc1
    t2 += 60 + inc2
    if int(t1//60)%24 == int(t2//60)%24 and (int(t1%60) == int(t2%60)):
        done = True
hours = str(int(t1//60)%24)
if len(hours) == 1:
    hours = '0' + hours
mins = str(int(t1%60))
if len(mins) == 1:
    mins = '0' + mins
print(hours+':'+mins)