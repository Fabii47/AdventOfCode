def main():
    with open("input_09.txt", 'r') as f:
        lines = f.readlines()
        
        print(evalRope(lines, 2))   # 6498
        print(evalRope(lines, 10))  # 2531
    
def evalRope(lines, length = 2):
    global tailVisited
    rope = [(0,0) for _ in range(length)]
    tailVisited = [rope[-1]]
    
    for line in lines:
        rope = moveRope(rope, line)
        #print(line[:-1], rope)
    
    return len(tailVisited)
    
def moveRope(rope, line):
    global tailVisited
    dir = line.split()[0]
    num = int(line.split()[1])
    for _ in range(num):
        rope[0] = moveHead(rope[0], dir)
        for i in range(1, len(rope)):
            rope[i] = moveTail(rope[i-1], rope[i])
        
        if rope[-1] not in tailVisited:
            tailVisited.append(rope[-1])
    return rope
    
def moveHead(head, dir):
    move = {'U': (0, 1), 'R': (1, 0), 'D': (0, -1), 'L': (-1, 0)}
    return tupleAddition(head, move[dir])

def moveTail(head, tail):
    #   T T T
    # T   v   T
    # T > H < T
    # T   ^   T
    #   T T T
    
    # catch Diagonal
    (dx, dy) = tupleSubstration(tail, head)
    if abs(dx) == 2 and abs(dy) == 2:
        return (head[0] + dx // 2, head[1] + dy // 2)
    
    if tail[1] > head[1] + 1:       # move Down
        tail = (head[0], head[1] + 1)
    elif tail[1] < head[1] - 1:     # move Up
        tail = (head[0], head[1] - 1)
    elif tail[0] > head[0] + 1:     # move left
        tail = (head[0] + 1, head[1])
    elif tail[0] < head[0] - 1:     # move right
        tail = (head[0] - 1, head[1])
    
    return tail

def tupleAddition(a, b):
    return tuple(map(sum, zip(a, b)))
    
def tupleSubstration(a, b):
    return tuple(map(lambda i, j: i - j, a, b))

if __name__ == "__main__":
    main()