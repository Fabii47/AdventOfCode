import numpy as np


matrix = np.zeros(0)
startPos = (0, 0)

moveDirs = [(0,1), (1, 0), (0, -1), (-1, 0)]

def main():
    with open('input.txt', 'r') as f:
        convertLines2Matrix(f.readlines())
        print(matrix)
        print(startPos)
        
        queue = []
        queue.append(startPos)
        nextTurnQueue = []
        
        for _ in range(64):
            while queue:
                (x, y) = queue.pop()
                #print(">< pop ><")
                for (dx, dy) in moveDirs:
                    #print(f"{dx} {dy}")
                    coord = (x + dx, y + dy)
                    try:
                        if matrix[y + dy][x + dx] and not coord in nextTurnQueue:
                            nextTurnQueue.append(coord)
                    except IndexError:
                        continue
            while nextTurnQueue:
                item = nextTurnQueue.pop()
                queue.append(item)
            #print(queue)
            
        print(len(queue))
            
            
    
def convertLines2Matrix(lines):
    global matrix
    global startPos
    matrix = np.zeros((len(lines), len(lines[0]) - 1), dtype = np.byte)
    for r, row in enumerate(range(len(lines))):
        for c, column in enumerate(range(len(lines[row]) - 1)):
            char = lines[row][column]
            if char == "S":
                startPos = (r, c)
                
            if   char == "#":
                matrix[row][column] = 0
            else:
                matrix[row][column] = 1
    
if __name__ == "__main__":
    main()