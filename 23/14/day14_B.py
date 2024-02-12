import time
import numpy as np

matrix = np.zeros(0)

def main():
    print(matrix)
    print(matrix.shape[0])

##### Board tiling #####
def tiltNorth():
    global matrix
    for columnIdx in range(matrix.shape[1]):    
        for rowIdx in range(len(matrix)):
            if matrix[rowIdx][columnIdx] > 0:
                fittingRowIdx = rowIdx
                for searchIdx in range(rowIdx - 1, 0, -1):
                    if matrix[searchIdx][columnIdx] == 0:
                        fittingRowIdx = searchIdx
                    else
                        break
                
                
    pass


##### helper functions #####    
def convertLines2Matrix(lines):
    global matrix
    matrix = np.zeros((len(lines), len(lines[0]) - 1), dtype = np.byte)
    for row in range(len(lines)):
        for column in range(len(lines[row])):
            char = lines[row][column]
            if   char == "#":
                matrix[row][column] = -1
            elif char == "O":
                matrix[row][column] = 1

##### Debug and fancy Printing #####
def progressBar(done, total, length = 50):
    percent = (done / total) * 100
    filled_length = int(length * done // total)
    bar = '=' * filled_length + ' ' * (length - filled_length)
    print(f"\r[{bar}] {percent:.1f}%", end = "")

##### start main #####
with open('input.txt', 'r') as file:
    convertLines2Matrix(file.readlines())
    main()