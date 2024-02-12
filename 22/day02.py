def main():
    with open("input_02.txt", 'r') as f:
        lines = f.readlines()
        print(sum(map(solveA, lines)))
        print(sum(map(solveA, map(solveB, lines))))
        
def solveA(line):
    (e, s) = line.split()
    return "XYZ".index(s) + 1 + (("XYZ".index(s) - "ABC".index(e) + 1) % 3) * 3

def solveB(line):
    # lose draw win
    # rock paper scissor
    (a, x) = line.split()
    return a + " " + "XYZ"[("ABC".index(a) + "XYZ".index(x) - 1) % 3]

if __name__ == "__main__":
    main()