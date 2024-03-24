import numpy as np

def main():
    global map
    global startPos
    global targetPos
    with open("input_12.txt", 'r') as f:
        lines = f.readlines()
        map = read_map([l.strip() for l in lines])
        #print(map)

    global queue
    global dist

    # Solve A
    queue = [startPos]
    
    dist = np.full(map.shape, 1_000_000)
    dist[startPos[1], startPos[0]] = 0

    solve()

    # Solve B
    queue = []
    dist = np.full(map.shape, 1_000_000)
    for iy in range(map.shape[0]):
        for ix in range(map.shape[1]):
            if map[iy][ix] == 0:
                queue.append((ix, iy))
                dist[iy][ix] = 0
    
    solve()

def solve():
    global queue
    global dist

    while queue:
        (x, y) = queue.pop()

        current_height = map[y][x]
        # every dist
        nextPos = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
        for pos in nextPos:
            # check out of Bounds
            if pos[0] < 0 or pos[1] < 0:
                continue
            if pos[1] >= map.shape[0] or pos[0] >= map.shape[1]:
                continue
            
            # check for legit height
            if map[pos[1]][pos[0]] > map[y][x] + 1:
                continue 

            val = dist[y][x] + 1
            if val < dist[pos[1]][pos[0]]:
                dist[pos[1], pos[0]] = val
                queue.append(pos)

    print(dist[targetPos[1]][targetPos[0]])


# side effect: save start pos
def read_map(lines):
    global map
    global startPos
    global targetPos
    height = len(lines)
    width = len(lines[0])
    
    map = np.zeros((height, width), dtype = int)

    # read height
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "S":
                print(f"Start at ({x}, {y})")
                startPos = (x, y)
                map[y][x] = 0
            elif char == "E":
                print(f"End at ({x}, {y})")
                targetPos = (x, y)
                map[y][x] = 25
            else:
                map[y][x] = ord(char) - ord('a')
    return map

if __name__ == "__main__":
    main()