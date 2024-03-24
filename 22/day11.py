import utilitys

class Monkey:
    def __init__(self, id, items, operation, test, nextYes, nextNo):
        self.id         = id
        self.items      = items
        self.operation  = operation
        self.test       = test
        self.nextYes    = nextYes
        self.nextNo     = nextNo
        self.inspectedItems = 0
        
    def __str__(self):
        return f"Monkey {self.id}: {self.items}"
        
    def throwItems(self):
        while self.items:
            item = self.items.pop()
            item = self.operation(item)
            if nowSolving == 'A':
                item //= 3
            else:
                item %= lcm_testNums
                pass
            self.inspectedItems += 1
            
            if item % self.test == 0:
                monkeys[self.nextYes].items.append(item)
            else:
                monkeys[self.nextNo].items.append(item)
            
def main():
    with open("input_11.txt", 'r') as f:
        global monkeys
        global nowSolving
        global allTestNums
        global lcm_testNums
        allTestNums = []
        
        lines = f.readlines()
        
        # solve A
        nowSolving = 'A'
        monkeys = list(map(createMonkeys, splitMonkeys(lines)))
        throwAround(20) # 108240
        printInspectionCount()
        
        # solve B 
        print(f"\nnow Part B")
        #lcm_testNums = utilitys.least_common_multiple(allTestNums)
        lcm_testNums = 1
        for num in allTestNums:
            lcm_testNums *= num
        allTestNums = []
        nowSolving = 'B'
        monkeys = list(map(createMonkeys, splitMonkeys(lines)))
        print(lcm_testNums, "LCM of", allTestNums)
        throwAround(10_000) # should return 2713310158
        printInspectionCount()

def throwAround(rounds = 20):
    for round in range(rounds):
        for monkey in monkeys:
            monkey.throwItems()
        utilitys.progressBar(round + 1, rounds)

        #if round == 1:
        #    print("Round", round)
        #    for monkey in monkeys:
        #        print(monkey.inspectedItems)
    print()

def printInspectionCount():
    inspectionCount = getInspectionCount()
    print("Inspection Count:")
    print(inspectionCount[0], inspectionCount[1])
    print(inspectionCount[0] * inspectionCount[1])
    # 52166  52013 

def getInspectionCount():
    inspectionCount = []
    for monkey in monkeys:
        inspectionCount.append(monkey.inspectedItems)
    
    inspectionCount.sort(reverse = True)
    return inspectionCount
        
def createMonkeys(rawMonkey):
    global allTestNums
    monkeyID        = int(rawMonkey[0].split()[1][:-1])    # Monkey id:
    startingItems   = [int(x) for x in rawMonkey[1].split(":")[1].split(",")]
    operation       = buildLambda(rawMonkey[2].split(" = ")[1])
    test            = int(rawMonkey[3].split("by")[1])
    yes             = int(rawMonkey[4].split()[-1])
    no              = int(rawMonkey[5].split()[-1])
 
    allTestNums.append(test)
    return Monkey(monkeyID, startingItems, operation, test, yes, no)
        
def buildLambda(raw):
    if raw == "old * old":
        return lambda f: f * f
    
    if raw.split()[1] == "+":
        return lambda f: f + int(raw.split()[2])
    elif raw.split()[1] == "*":
        return lambda f: f * int(raw.split()[2])
        
def splitMonkeys(lines):
    monkeyList = []
    idx = 0
    
    for line in lines:
        if line == "\n":
            continue
    
        if line.split()[0] == "Monkey":
            idx = int(line.split()[1][:-1])
            monkeyList.append([line[:-1]])
            continue
        
        monkeyList[idx].append(line[:-1])
    
    return monkeyList

if __name__ == "__main__":
    main()