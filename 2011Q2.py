cards = []
vals = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
suits = ['C', 'H', 'S', 'D']
for i in range(0, len(suits)):
    for j in range(0, len(vals)):
        cards.append(vals[j]+suits[i])
arr = list(map(int, input().split()))
shuffled = []
index = 0
while len(cards) > 0:
    number = arr[index]
    while number > len(cards):
        number -= len(cards)
    under = cards[:number-1]
    cards = cards[number-1:]
    shuffled.append(cards.pop(0))
    for i in range(0, len(under)):
        cards.append(under[i])
    index += 1
    index %= 6
print(shuffled[0], shuffled[len(shuffled)-1])


def compatable(a, b):
    return (a[0] == b[0] or a[1] == b[1])

def strat1(cards, count):
    for i in range(len(cards)-1, 0, -1):
        if compatable(cards[i], cards[i-1]):
            count[i-1] += count[i]
            count.pop(i)
            cards[i-1] = cards[i]
            cards.pop(i)
            return cards, count
        if i >= 3:
            if compatable(cards[i], cards[i-3]):
                count[i-3] += count[i]
                count.pop(i)
                cards[i-3] = cards[i]
                cards.pop(i)
                return cards, count
    return False

def strat2(cards, count):
    maximum = -1
    move = []
    for i in range(len(cards)-1, 0, -1):
        if compatable(cards[i], cards[i-1]):
            if maximum < count[i]+count[i-1]:
                maximum = count[i]+count[i-1]
                move = [i, i-1]
        if i >= 3:
            if compatable(cards[i], cards[i-3]):
                if maximum < count[i]+count[i-3]:
                    maximum = count[i]+count[i-3]
                    move = [i, i-3]
    if len(move) > 0:
        count[move[1]] += count[move[0]]
        cards[move[1]] = cards[move[0]]
        count.pop(move[0])
        cards.pop(move[0])
        return cards, count
    return False

def strat3(cards, count):
    maximum = -1
    move = []
    for i in range(len(cards)-1, 0, -1):
        if compatable(cards[i], cards[i-1]):
            tempCards = cards.copy()
            tempCards[i-1] = tempCards[i]
            tempCards.pop(i)
            available = countMoves(tempCards)
            if available > maximum:
                maximum = available
                move = [i, i-1]

        if i >= 3:
            if compatable(cards[i], cards[i-3]):
                tempCards = cards.copy()
                tempCards[i-3] = tempCards[i]
                tempCards.pop(i)
                available = countMoves(tempCards)
                if available > maximum:
                    maximum = available
                    move = [i, i-3]
    if len(move) > 0:
        cards[move[1]] = cards[move[0]]
        cards.pop(move[0])
        count[move[1]] += count[move[0]]
        count.pop(move[0])
        return cards, count
    return False

def countMoves(cards):
    moves = 0
    for i in range(len(cards)-1, 0, -1):
        if compatable(cards[i], cards[i-1]):
            moves += 1
        if i >= 3:
            if compatable(cards[i], cards[i-3]):
                moves += 1
    return moves

cards = shuffled.copy()
count = [1] * len(shuffled)
result = (cards, count)
while result != False:
    cards, count = result
    result = strat1(cards, count)
print(len(count), cards[0])

cards = shuffled.copy()
count = [1] * len(shuffled)
result = (cards, count)
while result != False:
    cards, count = result
    result = strat2(cards, count)
print(len(count), cards[0])

cards = shuffled.copy()
count = [1] * len(shuffled)
result = (cards, count)
while result != False:
    cards, count = result
    result = strat3(cards, count)
print(len(count), cards[0])