import math
source = 'input.txt'

def isSymbol(c):
    return not c.isnumeric() and c != '.' and c != '\n'

with open(source, 'r') as file:
    lines = file.readlines()
    
    sum = 0
    
    for y in range(len(lines)):
        x = 0
        while x < len(lines[y]):  
            c = lines[y][x]
            if isSymbol(c):
                print(f"{lines[y][x]} at {x},{y}")
                
            num = 0
            while c.isnumeric():
                num = (num * 10) + int(c)
                x += 1
                c = lines[y][x]
            
            added = False
            if num != 0:
                #print(f"num = {num} at {x},{y}")
                numlen = int(math.log10(num))
                for yi in range(max(y-1, 0), min(len(lines), y+2)):
                    for xi in range (max((x-2)-numlen, 0), min(len(lines[y]), x+1)):
                        if isSymbol(lines[yi][xi]) and added == False:
                            sum += num
                            added = True
                            print(f"{num} was added at {x},{y} because {lines[yi][xi]}:{xi},{yi}")
            
            x += 1
    
    print(f"[{sum}]")