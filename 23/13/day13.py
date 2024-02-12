def equalLines(a, b):
    smudges = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            smudges += 1
    return smudges

def perfectReflectionHorizontal(matrix, row):
    p = 0
    totalSmudges = 0
    while row - 1 - p >= 0 and row + p < len(matrix):
        totalSmudges += equalLines(matrix[row - 1 - p], matrix[row + p])
        if totalSmudges > 1:
            return False
        p += 1
    return True

#   ..##...
#   1234567 -> 3
def perfectReflectionVertical(matrix, column):
    p = 0
    #print(f"called prv with {column} .... len: {len(matrix[0])}")
    totalSmudges = 0
    while column - 1 - p >= 0 and column + p < len(matrix[0])-1:
        a_ = getColumn(matrix, column - p - 1)
        b_ = getColumn(matrix, column + p)
        #print(f"-----> {a_}\n{b_} <-----")
        totalSmudges += equalLines(a_, b_)
        if totalSmudges > 1:
            return False
        p += 1
    return True

def getColumn(matrix, i):
    return [row[i] for row in matrix]

def printMatrix(block):
    print()
    for str in block:
        print(str, end = "")
        
def getMatrixList(input):
    block = [0]
    for i in range(1, len(lines)):
        if lines[i] == "\n":
            block.append(i)
    block.append(len(lines))
    
    matrixList = []
    for i in range(1, len(block)):
        matrix = lines[block[i-1]:block[i]]
        if matrix[0] == "\n":
            matrix.remove('\n')
        matrixList.append(matrix)
        
    return matrixList

def isHoriziontalReflection(matrix):
    for i in range(1, len(matrix)):
        if perfectReflectionHorizontal(matrix, i):
            return i * 100
    return 0

def isVerticalReflection(matrix):
    for i in range(1, len(matrix[0])-1):    # -1 -> \n
        if perfectReflectionVertical(matrix, i):
            return i
    return 0

def main(matrixList):
    counter = 0
    for matrix in matrixList:
        printMatrix(matrix)
        matrixScore = isHoriziontalReflection(matrix) + isVerticalReflection(matrix)
        counter += matrixScore
        print(matrixScore)
    print(counter)

with open('input.txt', 'r') as file:
    lines = file.readlines()
    main(getMatrixList(lines))