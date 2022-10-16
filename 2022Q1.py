string = input()

#go through each letter and 


def decrpyt(string):

    new = ''

    for i in range(len(string)-1, 0, -1):
        current = string[i]
        last = string[i-1]
        num1 = ord(current) - 65 + 1
        num2 = ord(last) - 65 + 1
        num = num1 - num2
        while num<1:
            num = 26+num
        new += chr(num-1+65)

    new += string[0]

    return new[::-1]

def encrpyt(string):
    for i in range(1, len(string)):
        current = string[i]
        last = string[i-1]
        num1 = ord(current) - 65 + 1
        num2 = ord(last) - 65 + 1
        num = num1 + num2
        if num > 26:
            num -= 26
        new = ''
        for index in range(0, len(string)):
            if index == i:
                new += chr(65+num-1)
            else:
                new += string[index]
        string = new
    
    return string

print(decrpyt(string))