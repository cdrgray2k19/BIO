from functools import lru_cache
#backtracking function?

alphabetCode = {'.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e', '..-.':'f', '--.':'g', '....':'h', '..':'i', '.---':'j', '-.-':'k', '.-..':'l', '--':'m', '-.':'n', '---':'o', '.--.':'p', '--.-':'q', '.-.':'r', '...':'s', '-':'t', '..-':'u', '...-':'v', '.--':'w', '-..-':'x', '-.--':'y', '--..':'z'}

s = input()
#get length
length = len(s)
#get morse code of word
morse = ''
while len(s) > 0:
    char = s[:1]
    s = s[1:]
    for code in alphabetCode:
        if alphabetCode[code] == char:
            morse += code

@lru_cache(maxsize=None)
def solve(remainingCode, lettersLeft):
    if lettersLeft == 0:
        return []
    words = []
    for i in range(1, len(remainingCode)+1-lettersLeft+1):
        try:
            newLetter = alphabetCode[remainingCode[:i]]
            if lettersLeft > 1:
                wordsToAdd = solve(remainingCode[i:], lettersLeft-1)
                for w in wordsToAdd:
                    words.append(newLetter+w)
            elif remainingCode[i:] == '':
                words.append(newLetter)

        except:
            continue
    return words

print(len(solve(morse, length)))