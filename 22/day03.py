def main():
    with open("input_03.txt", 'r') as f:
        lines = f.readlines()
        print(sum(map(findMatch, lines)))
        print(sum(map(findBatch, lines[0::3], lines[1::3], lines[2::3])))

def findMatch(line):
    return [charValue(c) for c in line[:len(line)//2] if c in line[len(line)//2:-1]][0]

def findBatch(l1, l2, l3):
    return [charValue(c) for c in l1 if c in l2 and c in l3][0]
    
def charValue(c):
    return ord(c) - ((ord('a') - 1) if c.islower() else (ord('A') - 27))
    
if __name__ == "__main__":
    main()