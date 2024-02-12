states = {}
key = {'x':0, 'm':1, 'a':2, 's':3}

def main():
    with open('input_19.txt', 'r') as f:
        global states
        parts = []
        
        line = f.readline()
        while line != "\n":
            string = line.split("{")
            states[string[0]] = string[1].replace('}\n', '')
            line = f.readline()
            
        for l in f.readlines():
            parts.append(l[0:-1])
            
        megaSum = 0
        for part in parts:
            megaSum += evaluatePart(getPartNums(part))
        
        print(f"[{megaSum}]")

def evaluatePart(part):
    nS = "in"
    while len(nS) != 1:
        print(f"{nS = }\t{states[nS] = }")
        nS = nextState(nS, part)
    if nS == 'A':
        return sum(part)
    return 0
    
def nextState(state, part):
    string = states[state]
    steps = string.split(',')
    
    for step in steps[:-1]:
        k = step[0]
        greater = step[1] == '>'
        val = int(step.split(':')[0][2:])
        nextS = step.split(':')[1]
        
        if greater and part[key[k]] > val:
            return nextS
        elif not greater and part[key[k]] < val:
            return nextS
    
    return steps[-1]
    
def getPartNums(part):
    return [int(x[2:]) for x in part[1:-1].split(',')]
        
if __name__ == "__main__":
    main()