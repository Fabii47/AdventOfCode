word = ["one"   , "two"     , "three", 
        "four"  , "five"    , "six"  , 
        "seven" , "eight"   , "nine" ]

def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        
        megasum = 0
        
        for line in lines:
            sum = 10 * firstNum(line) + lastNum(line)
            print(f"({sum}) {line}", end = "")
            megasum += sum
            
        print(f"\n[{megasum}]")

def firstNum(line):
    firstDigit = getNumFirst(line)
    firstWord  = getWordFirst(line)
    
    if firstWord[1] < 0:
        return firstDigit[0]
    
    if firstDigit[1] < firstWord[1]:
        return firstDigit[0]
    
    return firstWord[0]
    
def lastNum(line):
    lastDigit = getLastDigit(line)
    lastWord  = getLastWord(line)

    if lastWord[1] < 0:
        return lastDigit[0]
    
    if lastDigit[1] > lastWord[1]:
        return lastDigit[0]
    
    return lastWord[0]

def getLastWord(line):
    maxIdx = -1
    num = 0
    
    for n, w in enumerate(word):
        idx = line.rfind(w)
        if idx > maxIdx and idx >= 0:
            maxIdx = idx
            num = n + 1
            
    return(num, maxIdx)

def getLastDigit(line):
    maxIdx = -1
    digit = 0
    for idx, c in enumerate(line):
        if c.isdigit():
            maxIdx = idx
            digit = int(c)
    return (digit, maxIdx)

def getWordFirst(line):
    minIdx = 100
    num = 0
    
    for n, w in enumerate(word):
        idx = line.find(w)
        if idx < minIdx and idx >= 0:
            minIdx = idx
            num = n + 1
            
    return(num, minIdx)

def getNumFirst(line):
    for idx, c in enumerate(line):
        if c.isdigit():
            return (int(c), idx)
    return (0, -1)

if __name__ == "__main__":
    main()