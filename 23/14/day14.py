import time

SOURCE = "input.txt"

def main():
    global matrix
    start_time = time.time()
    
    iterations = 1_000_000_000
    
    foundHashes = []
    
    for i in range(iterations):
        rotationCycle()
        
        #print(f"({i = })")
        h = sum([hash(s) for s in matrix])
        if h in foundHashes:
            print()
            print(i, ":\t", supportBeamWeight(), end = '\t' )
            foundAt = foundHashes.index(h)
            length = i - foundHashes.index(h)
            
            print(f"{foundAt = }, {length = }")
            
            
            for _ in range((iterations - i) % length - 1):
                rotationCycle()
                
            break
        else:
            foundHashes.append(h)
        
        
        
            progressBar(i + 1, iterations)
        
    #printMatrix(matrix)
    
    print(f"\n[{supportBeamWeight()}] finished in {time.time() - start_time:.4f} seconds")

def rotationCycle():
    tiltBoardNorth()
    tiltBoardWest()
    tiltBoardSouth()
    tiltBoardEast()
    

def printMatrix():
    print()
    for line in matrix:
        print(line, end = "")

def getColumn(i):
    return [row[i] for row in matrix]

def replaceCharAt(line, char, at):
    return line[:at] + char + line[at+1:]

def placeColumn(column, idx):
    global matrix
    for i in range(len(matrix)):
        matrix[i] = replaceCharAt(matrix[i], column[i], idx)
        
    
    #return lines

def pushTowards(towards, origin):
    newTowards = ""
    newOrigin  = ""
    for c in range(len(towards)):
        if origin[c] == "O" and towards[c] == ".":
            newOrigin  += "."
            newTowards += "O"
        else:
            newOrigin  += origin[c]
            newTowards += towards[c]
    return (newTowards, newOrigin)

def tiltBoardNorth():
    global matrix
    for i in range(1,len(matrix)): # line
        for k in range(i, 0, -1):  # lines above: move/swap
            (towards, origin) = pushTowards(matrix[k - 1], matrix[k])
            matrix[k-1] = towards
            matrix[k]   = origin
    #return matrix
    
def tiltBoardWest():
    global matrix
    for i in range(1, len(matrix[0])):   # column                -> from
        for k in range(i, 0, -1):       # columns from i to 0   -> insert
            (towards, origin) = pushTowards(getColumn(k - 1), getColumn(k))
            placeColumn(towards, k - 1)
            placeColumn(origin, k)
    #return lines

def tiltBoardSouth():
    global matrix
    for i in range(len(matrix)-1, 0, -1): # line
        for k in range(i, len(matrix)):  # lines above: move/swap
            (towards, origin) = pushTowards(matrix[k], matrix[k - 1])
            matrix[k] = towards
            matrix[k - 1]   = origin
    #return lines

def tiltBoardEast():
    global matrix
    for i in range(len(matrix[0]) - 1, 0, -1):   # column                -> from
        for k in range(i, len(matrix[0])):       # columns from i to 0   -> insert
            (towards, origin) = pushTowards(getColumn(k), getColumn(k - 1))
            placeColumn(towards, k)
            placeColumn(origin, k - 1)
    #return lines

def supportBeamWeight():
    sum = 0
    for i in range(len(matrix)):
        for c in matrix[i]:
            if c == "O":
                sum += len(matrix) - i
    return sum

def progressBar(done, total, length = 50):
    percent = (done / total) * 100
    filled_length = int(length * done // total)
    bar = '=' * filled_length + ' ' * (length - filled_length)
    print(f"\r[{bar}] {percent:.7f}%", end = "")

with open(SOURCE, 'r') as file:
    global matrix
    matrix = file.readlines()
    main()