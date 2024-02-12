def main():
    with open("input_04.txt", 'r') as f:
        lines = [[int(c) for c in line.replace('-', ',').split(',')] for line in f.readlines()]
        print(*map(lambda f: sum(map(f, lines)), [solveA, solveB]))

def solveA(l):
    return (l[0] <= l[2] and l[1] >= l[3]) or (l[2] <= l[0] and l[3] >= l[1])
    
def solveB(l):
    return solveA(l) or ((l[0] <= l[2] and l[1] >= l[2]) or (l[0] <= l[3] and l[1] >= l[3]))
    
if __name__ == "__main__":
    main()