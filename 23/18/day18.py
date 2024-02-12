def main():
    with open('input.txt', 'r') as file:
    
        edgeTiles = readInputFillList(file.readlines())
                
        (maxX, maxY) = maxValues(edgeTiles)
        (minX, minY) = minValues(edgeTiles)
        
        print(f"{maxX = } {minX = } {maxY = } {minY = }")
        
        lavaPool = [[2] * (maxX - minX + 1) for _ in range(maxY - minY + 1)]
        for (xi, yi) in edgeTiles:
            #print(f"{xi - minX = } {yi - minY = }")
            lavaPool[yi - minY][xi - minX] = 1
            
        #lavaPool[15][15] = 1
        
        queue = []
        queue.append((0,0))
        
        while(queue):
            (xq, yq) = queue.pop()
            
            try:
                tile = lavaPool[xq][yq]
            except IndexError:
                tile = -1
            
            if(tile == 2):
                #print("placed stuff")
                lavaPool[xq][yq] = 0
                queue.append((xq + 1, yq))
                queue.append((xq - 1, yq))
                queue.append((xq, yq + 1))
                queue.append((xq, yq - 1))
        
        debugMap(lavaPool)
        
        vol = 0
        for y in range(len(lavaPool)):
            for x in range(len(lavaPool[y])):
                if lavaPool[y][x] != 0:
                    vol += 1
        print(vol)
        print(swapInput(["R 9 (#521d52)"]))

def swapInput(lines):
    for line in lines:
        hexNum = int(line.split()[-1][2:-2], 16)
    

def readInputFillList(lines):
    edgeTiles = []
    edgeTiles.append((0, 0))
    x = y = 0
    for line in lines:
        (dir, dist) = line.split()[0:2]
        print(f"{dir = } {dist = }")
        for d in range(int(dist)):
            if dir == 'R':
                x += 1
            elif dir == 'L':
                x -= 1
            elif dir == 'U':
                y += 1
            elif dir == 'D':
                y -= 1
            edgeTiles.append((x, y))
    return edgeTiles

def debugMap(list):
    for y in range(0, len(list), 2):
        for x in range(0, len(list[y]), 2):
            if list[y][x] == 0:
                print(".", end = "")
            elif list[y][x] == 1:
                print("#", end = "")
            else:
                print(";", end = "")
        print()

def maxValues(list):
    maxX = maxY = 0
    for (x, y) in list:
        maxX = max(x, maxX)
        maxY = max(y, maxY)
    return (maxX, maxY)
    
def minValues(list):
    minX = minY = 0
    for (x, y) in list:
        minX = min(x, minX)
        minY = min(y, minY)
    return (minX, minY)
    
if __name__ == "__main__":
    main()