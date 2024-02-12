def main():
    with open('input.txt', 'r') as file:
        print(sum(map(evaluateLine, file.readlines())))
    
def evaluateLine(line):
    line = line.split(": ")[-1].strip().replace(';', ',')
    pairs = [(int(x.split()[0]), x.split()[-1]) for x in line.split(",")]
    
    r = g = b = 0
    for pair in pairs:
        if pair[1] == "red":
            r = max(r, pair[0])
        elif pair[1] == "green":
            g = max(g, pair[0])
        elif pair[1] == "blue":
            b = max(b, pair[0])
            
    return r * g * b
    
if __name__ == "__main__":
    main()