convert = {'pa':1, 're':2, 'ci':3, 'vo':4, 'mu':5, 'xa':6, 'ze':7, 'bi':8, 'so':9, 'no': 0}

'''
values = []
for v in convert:
    values.append(int(ord(v[0])-ord('a'))+int(ord(v[1])-ord('a')))
print(values)


for i in convert.keys():
    for j in convert.keys():
        for k in convert.keys():
            if len(set([i, j, k])) == 3:
                tempNum = ''
                tempNum += str(convert[i])
                tempNum += str(convert[j])
                tempNum += str(convert[k])
                if int(tempNum) == int(ord(i[0])-ord('a'))+int(ord(i[1])-ord('a')) + int(ord(j[0])-ord('a'))+int(ord(j[1])-ord('a')) + int(ord(k[0])-ord('a'))+int(ord(k[1])-ord('a')):
                    print(tempNum)
'''
current = ''
num = ''


s = input()

for c in s:
    current += c
    try:
        num += str(convert[current])
        current = ''
    except:
        pass

print(int(num))

#pareno