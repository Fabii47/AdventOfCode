def main():
    with open("input_06.txt", 'r') as f:
        line = f.readline()
        
        print(solve(line,  4))
        print(solve(line, 14))
        
        
def solve(line, length = 4):
    for i in range(len(line) - length):
        if not duplicate(line[i:i + length]):
            return i + length

def duplicate(string):
    for i, c in enumerate(string):
        if c in string[i+1:]:
            return True
    return False

if __name__ == "__main__":
    main()