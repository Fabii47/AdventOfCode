from dataclasses import dataclass
from enum import Enum
import numpy as np

NORTH = 0
EAST  = 1
SOUTH = 2
WEST  = 3
    
def turnRight(dir):
    return (dir+ 1) % 4
    
def turnLeft(dir):
    return (dir- 1) & 4

source = "input.txt"
matrix = []
dp = []

splitVer = 5
splitHor = 6
bounceNW = 3
bounceSW = 2

def main():
    print(matrix)
    
    beamStack = []
    
    global dp
    dp = np.zeros((matrix.shape[0], matrix.shape[1], 4))
    
    beamStack.append((0, 0, EAST)) # top left look right
    
    while(beamStack):
        (x, y, dir) = beamStack.pop(0) # currentBeam 
        #print(f"{x = } {y = } {dir = }")
        (x1, y1, d1) = (x, y, dir)
        if matrix[y][x] == bounceSW:
            #print(f"bounce \\ {x = }  {y = }   {dir = }")
            (x1, y1, d1) = bounceBackSlash(x, y, dir)
        elif matrix[y][x] == bounceNW:
            #print(f"bounce / {x = }  {y = }   {dir = }")
            (x1, y1, d1) = bounceSlash(x, y, dir)
        elif matrix[y][x] == splitHor and dir != EAST and dir != WEST:
            (x1, y1, d1, x2, y2, d2) = splitMinus(x, y, dir)
            if not isOutOfBounds(x2, y2) and not visited(x2, y2, d2):
                beamStack.append((x2, y2, d2))
        elif matrix[y][x] == splitVer and dir != NORTH and dir != SOUTH:
            (x1, y1, d1, x2, y2, d2) = splitAbs(x, y, dir)
            if not isOutOfBounds(x2, y2) and not visited(x2, y2, d2):
                beamStack.append((x2, y2, d2))
        else:
            (x1, y1, d1) = move(x, y, dir)
        
        if not isOutOfBounds(x1, y1) and not visited(x1, y1, d1):
            beamStack.append((x1, y1, d1))
            #print(f"puddin in the stack {x1 = } {y1 = } {d1 = }")
            
    printDP()
    print(f"[{countDP()}]")
        
def isOutOfBounds(x, y):
    return x < 0 or y < 0 or x >= len(matrix) or y >= matrix.shape[1]
    
def visited(x, y, dir):
    return dp[y][x][dir] != 0
        
def splitMinus(x, y, dir):
    # dir either NORTH or SOUTH
    global dp
    dp[y][x][dir] = 1
    return (x - 1, y, WEST, x + 1, y, EAST)

def splitAbs(x, y, dir):
    global dp
    dp[y][x][dir] = 1
    return (x, y - 1, NORTH, x, y + 1, SOUTH)
        
def move(x, y, dir):
    global dp
    dp[y][x][dir] = 1
    if dir == NORTH:
        y -= 1 
    elif dir == SOUTH:
        y += 1
    elif dir == EAST:
        x += 1 
    elif dir == WEST:
        x -= 1
    return (x, y, dir)
    
def bounceSlash(x, y, dir): #/
    global dp
    dp[y][x][dir] = 1
    if dir == EAST:
        dir = NORTH
        y -= 1
    elif dir == NORTH:
        dir = EAST
        x += 1
    elif dir == WEST:
        dir = SOUTH
        y += 1
    elif dir == SOUTH:
        dir = WEST
        x -= 1
    return (x, y, dir)
    
def bounceBackSlash(x, y, dir): #\
    global dp
    dp[y][x][dir] = 1
    if dir == EAST:
        dir = SOUTH
        y += 1
    elif dir == NORTH:
        dir = WEST
        x -= 1
    elif dir == WEST:
        dir = NORTH
        y -= 1
    elif dir == SOUTH:
        dir = EAST
        x += 1
    return (x, y, dir)
    
def startingPos():
    list = []
    for i in range(matrix.shape[1]):
        list.append((0, i, SOUTH))    # up
        list.append((len(matrix)-1, i, NORTH))  # down
    for i in range(len(matrix)):
        list.append((i, 0, EAST))   # left
        list.append((matrix.shape[1]-1, i, WEST)) # right

##### helper functions #####    
def convertLines2Matrix(lines):
    global matrix
    matrix = np.zeros((len(lines), len(lines[0]) - 1), dtype = np.byte)
    for row in range(len(lines)):
        for column in range(len(lines[row])):
            char = lines[row][column]
            if   char == "/":
                matrix[row][column] = bounceNW
            elif char == "\\":
                matrix[row][column] = bounceSW
            elif char == "|":
                matrix[row][column] = splitVer
            elif char == "-":
                matrix[row][column] = splitHor

##### Debug and fancy Printing #####
def progressBar(done, total, length = 50):
    percent = (done / total) * 100
    filled_length = int(length * done // total)
    bar = '=' * filled_length + ' ' * (length - filled_length)
    print(f"\r[{bar}] {percent:.1f}%", end = "")
    
def printDP():
    for row in dp:
        for space in row:
            if(sum(space) > 0):
                print("#", end = "")
            else:
                print(".", end = "")
        print()

def countDP():
    count = 0
    for row in dp:
        for space in row:
            if(sum(space) > 0):
                count += 1
    return count

##### start main #####

if __name__ == "__main__":
    with open(source, 'r') as file:
        convertLines2Matrix(file.readlines())
        main()