string = input()
def blockPalindrome(string):
    blocks = 0
    for i in range(1, (len(string)//2)+1):
        if string[:i] == string[len(string)-i:]:
            blocks += 1 + blockPalindrome(string[i:len(string)-i])
    return blocks

print(blockPalindrome(string))