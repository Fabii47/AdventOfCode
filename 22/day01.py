def main():
    with open("input_01.txt", 'r') as f:
        lines = compressLines(f.readlines())
        print(lines[0], sum(lines[0:3]))
        
def compressLines(l):
    food = []
    for _ in range(l.count('\n')):
        food.append(sum([int(x) for x in l[:l.index('\n')]]))
        l = l[l.index('\n') + 1:]
    food.sort(reverse = True)
    return food

if __name__ == "__main__":
    main()