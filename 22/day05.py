import copy

def main():
    with open("input_05.txt", 'r') as f:
        stack = (lambda ls: [[ls[y][x] for y in reversed(range(len(ls))) if ls[y][x] != ' '] for x in range(len(ls[0]))])([[l[x] for x in range(len(l)) if (x-1) % 4 == 0] for l in [l for l in iter(f.readline, '\n')][:-1]])

        instructionLines = f.readlines()
        
        crateMover9000(copy.deepcopy(stack), instructionLines)
        crateMover9001(copy.deepcopy(stack), instructionLines)

def crateMover9000(stack, instructions):
    for line in instructions:
        (amount, origin, destination) = evalInstruction(line)
        
        for _ in range(amount):
            stack[destination - 1].append(stack[origin-1].pop())
    printTopCrates(stack)
    
def crateMover9001(stack, instructions):
    for line in instructions:
        (amount, origin, destination) = evalInstruction(line)
        
        tempStack = []
        for _ in range(amount):
            tempStack.append(stack[origin-1].pop())
            
        for item in reversed(tempStack):
            stack[destination-1].append(item)
    printTopCrates(stack)

def printTopCrates(stack):
    for s in stack:
        print(s[-1], end = "")
    print()

def evalInstruction(line):
    return [int(x) for x in line.split() if x.isnumeric()]
    
def printStack(stack):
    highestStack = 0
    for s in stack:
        highestStack = max(len(s), highestStack)
    for y in reversed(range(highestStack)):
        for x in range(len(stack)):
            try:
                print(f"[{stack[x][y]}] ", end = "")
            except IndexError:
                print("    ", end = "")
        print()
    for i in range(len(stack)):
        print(f" {i+1}  ", end = "")
    print()
    
if __name__ == "__main__":
    main()
    