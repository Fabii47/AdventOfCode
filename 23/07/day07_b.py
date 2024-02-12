import bisect

JOKER = '0'

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULLHOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0

powerDir = {}

def main():
    with open("input.txt", 'r') as f:
        decks = []
        sum = 0
        for idx, line in enumerate(f.readlines()):
            (hand, bid) = readCard(line)
            
            #print(f"({idx})\t{hand} - {bid}\t", end = "")
            #print(evalDeck(hand))
            
            deck = (evalDeck(hand), hand, bid)
            bisect.insort(decks, deck)
            
        for idx, hand in enumerate(decks):
            sum += (idx + 1) * hand[-1]
            print(idx + 1 , ": ", hand)
        
        print(f"[{sum}]")
            
def evalDeck(card):
    jokers = card.count(JOKER)
    
    if jokers >= 4: # instant 5 of a kind
        return FIVE_OF_A_KIND
    
    max_count = 0
    twoPair = False
    readChars = []
    for char in card:
        if char == JOKER:
            continue
            
        count = card.count(char) + jokers
        
        if count == 5:
            return FIVE_OF_A_KIND
        if count == 4:
            return FOUR_OF_A_KIND
        
        if count + max_count == 5 and char not in readChars:
            return FULLHOUSE
            
        if count == 2 and max_count == 2 and char not in readChars:
            twoPair = True
        
        readChars.append(char)
        max_count = max(count - jokers, max_count)
    max_count += jokers
    if max_count == 3:
        return THREE_OF_A_KIND
    if twoPair:
        return TWO_PAIR
    if max_count == 2:
        return ONE_PAIR
    return HIGH_CARD
            
# (( translated Card as String ,, int bid of Hand ))
def readCard(line):
    return (translCards(line.split()[0]), int(line.split()[1]))
    
def translCards(c):
    return c.translate(str.maketrans("J23456789TQKA", "0123456789abc"))
    
if __name__ == "__main__":
    main()