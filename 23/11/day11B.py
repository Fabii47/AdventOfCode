def isEmptyRow(line):
    return "#" not in line
    
def getColumn(matrix, i):
    return [row[i] for row in matrix]

def isEmptyColumn(lines, i):
    return "#" not in getColumn(lines, i)
    
def distance(i, j):
    return abs(i[0] - j[0]) + abs(i[1] - j[1])

with open('input_11.txt', 'r') as file:
    lines = file.readlines()
    
    galaxy = []
    
    emptyLines = []
    emptyColumns = []
    
    expandBy = 1000000
    
    for row in range(len(lines)):
        if isEmptyRow(lines[row]):
            emptyLines.append(row)
            print(emptyLines[-1])
        
    for column in range(len(lines[0])-1):
        if isEmptyColumn(lines, column):
            emptyColumns.append(column)
            print(emptyColumns[-1])
        
    y = 0
    for row in range(len(lines)):
        if isEmptyRow(lines[row]):
            #print(f"emptyRow at {row}")
            y += expandBy
            continue
        else:
            y += 1
        x = 0
        for column in range(len(lines[row])-1):
            if isEmptyColumn(lines, column):
                x += expandBy
                continue
                #print(f"emptyColumn at {column}")
            else:
                x += 1
        
            if(lines[row][column] == "#"):
                #print(f"# at {row} {column}")
                galaxy.append((x, y))
                #print(galaxy[-1])
                
    sum = 0    
    for i in range(len(galaxy)):
        for j in range(i+1 , len(galaxy)):
            sum += distance(galaxy[i], galaxy[j])
    
    print(sum)