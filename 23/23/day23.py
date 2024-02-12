import numpy as np

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def main():
    with open("input.txt", 'r') as f:
        convertLines2Matrix(f.readlines())
        createDPMatrix           
        
        # posX posY length iteration
        queue = [(0, 1, 1, 1)]
        
        print(matrix)
        
def move(x, y):
    
def step(x, y):
    nextPos = []
    for dir in dirs:
        newPos = 
        try:
            if dp[]
        
def isFinished():
    
        
def clearNumFromDP(num):
    dpMatrix[dpMatrix >= num] = 0
        
def createDPMatrix():
    global dpMatrix
    dpMatrix = np.zeros_like(matrix)
        
def convertLines2Matrix(lines):
    global matrix
    matrix = np.zeros((len(lines), len(lines[0]) - 1), dtype = np.byte)
    for row in range(len(lines)):
        for column in range(len(lines[row]) - 1):
            char = lines[row][column]
            if   char == '#':
                matrix[row][column] = 0
            else:
                matrix[row][column] = ord(char)

if __name__ == "__main__":
    main()