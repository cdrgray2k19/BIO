#function that takes in string and breaks it up into groups and then concatenates the groups
#will have dictionary that will map roman numerals to numbers and convert numeral to numbers
string, n = input().split()
n = int(n)
vals = {1000: 'M', 500: 'D', 100:'C', 50:'L', 10: 'X', 5:'V', 1:'I'}

#exceptions IV, IX, XL, XC, CD and CM

def convert(num):
    roman = ''
    for v in vals:
        while num>=v:
            num -= v
            roman += vals[v]
    roman = roman.replace('IIII', 'IV') #change 4
    roman = roman.replace('VIV', 'IX') #change 9
    roman = roman.replace('XXXX', 'XL') #change 40
    roman = roman.replace('LXXXX', 'XC') #change 90
    roman = roman.replace('CCCC', 'CD') #change 400
    roman = roman.replace('DCCCC', 'CM') #change 900
    return roman



def lAndS(string):
    groups = []
    current = ''
    for c in string:
        if current == '':
            current += c
        elif c == current[0]:
            current += c
        else:
            groups.append(current)
            current = c
    groups.append(current)

    result = ''

    for g in groups:
        numOfNum = convert(len(g))
        result += numOfNum + g[0]
    #obtained groups now just need to convert lengths to roman numberals

    return result

for _ in range(n):
    string = lAndS(string)

print(string.count('I'), string.count('V'))
#d = set()
#for i in range(1, 4000):
#    string = convert(i)
#    print(string)
#    d.add(lAndS(string))
#print(len(d))

# b = 3919