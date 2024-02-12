import bisect

with open('input_07.txt', 'r') as file:
    lines = file.readlines()
    decks = []
    
    for line in lines:
        max_count = 0
        isFullHouse = False
        twoPair = False
        twoPairC = 'x'
        for char in line.split()[0]:
            count = line.split()[0].count(char)
            if count == 2 and max_count == 3:
                isFullHouse = True
            elif count == 3 and max_count == 2:
                isFullHouse = True
            elif count == 2:
                if twoPairC == 'x':
                    twoPairC = char
                if max_count == 2 and char != twoPairC:
                    twoPair = True
                    print(line)
            if count > max_count:
                max_count = count
        strength = max_count;
        if(max_count > 3) or isFullHouse:
            strength += 1
        if(max_count >= 3) or twoPair:
            strength += 1
        
        cardEdit = line.split()[0].translate(str.maketrans("TJQKA", "abcde"))
        
        deck = (strength, cardEdit, int(line.split()[1]))
        bisect.insort(decks, deck)
        
    sum = 0
    for i in range(len(decks)):
        print(f"{i} - {decks[i]} - {decks[i][2]} * {i+1} | {decks[i][1].translate(str.maketrans('abcde', 'TJQKA'))}")
        sum +=  decks[i][2] * (i+1)
    
    print(f"{sum}")
        
        
                