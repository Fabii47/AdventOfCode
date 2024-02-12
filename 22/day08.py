import numpy as np
import utilitys

from math import prod

def main():
    with open("input_08.txt", 'r') as f:
        matrix = utilitys.np_lines2Matrix(f.readlines())
        print(countVisibleTrees(matrix)) # solve A
        print(findBestTree(matrix))      # solve B
        
def findBestTree(matrix):
    bestScore = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            utilitys.progressBar(x + y * len(matrix) + 1, matrix.size)
            bestScore = max(bestScore, scenicScore(x, y, matrix))
    print()
    return bestScore
    
def scenicScore(x, y, matrix):
    dirs = [matrix[y, :x][::-1], matrix[y, x+1:], matrix[:y, x][::-1], matrix[y+1:, x]]

    result = 1
    for direction in dirs:
        result *= scoreInDir(direction, matrix[y, x])
    return result
    
def scoreInDir(trees, treeHeight):
    if(trees.size == 0):
        return 0
    
    num = 0
    for t in trees:
        num += 1
        if t >= treeHeight:
            break
    return num
    
def countVisibleTrees(matrix):
    visibleTrees = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            visibleTrees += x_y_visible(x, y, matrix)
    return visibleTrees

# returns True if Tree (x, y) is visible
def x_y_visible(x, y, matrix):
    #       left             right              above           below
    dirs = [matrix[y, :x], matrix[y, x+1:], matrix[:y, x], matrix[y+1:, x]]
    return min(map(lambda f: -1 if f.size == 0 else max(f), dirs)) < matrix[y][x]
    #               ^^^^^^^^^^^^^ catches ValueError ^^^^^^^^^^^^^^^^^^
    

if __name__ == "__main__":
    main()