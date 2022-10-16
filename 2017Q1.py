pattern = input()

colours = set(['R', 'G', 'B'])
while len(pattern) > 1:
    new = ''
    
    for i in range(1, len(pattern)):
        if pattern[i-1] == pattern[i]:
            new += pattern[i]
        else:
            new += str(list(colours - set([pattern[i-1], pattern[i]]))[0])
    
    pattern = new

print(pattern)

# 3 possible rows RRRBBGGRG, BGBRGBRGR, GBGGRRBBB

# only 1 way, if you have a complete row then the row before that will always be predetermined. once you have a completed row and one known square, the squares next to the known one will have to make the square above it allowing one option, this means as you fill out the squares the next square to fill out will only have one possible option. This process continues allowing for each row and then the next only 1 possible arrangement of squares

# 10