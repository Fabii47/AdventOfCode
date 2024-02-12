maxTickets = 500

def main():
    with open("input.txt", 'r') as f:
        sum = 0
        cardAmount = [1 for _ in range(maxTickets)]
        
        for idx, line in enumerate(f.readlines()):
            counter = countCard(readCard(line))
            
            for i in range(idx + 1, idx + counter + 1):
                cardAmount[i] += cardAmount[idx]
            
            sum += cardAmount[idx]
            
            print(f"({idx}):\t[{counter}]:\t{cardAmount[idx]}")
        print(f"total points: [{sum}]")
        
# returns tuple of Lists (winningNumbers[], myNumbers[])
def readCard(line):
    (haveStr, wantStr) = line.split(":")[1].split("|")
    have = [int(w) for w in haveStr.split() if w.isnumeric()]
    want = [int(n) for n in wantStr.split() if n.isnumeric()]
    return (want, have)
    
# counts winning Numbers in Card
def countCard(card):
    return sum(1 for num in card[0] if num in card[1])
        
if __name__ == "__main__":
    main()