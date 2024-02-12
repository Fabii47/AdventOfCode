import sys
sys.path.append('..')
import utilitys

def main():
    with open('input.txt', 'r') as file:
        path = file.readline()
        dict = getDict(file.readlines())

        cyclus = []
        
        for pos in getStartingPoints(dict):
            counter = 0
            p = 0
            while pos[-1] != 'Z':
                pos = dict[pos][{'L':0, 'R':1}[path[p]]]
                p = (p + 1) % (len(path) - 1)
                counter += 1
                
            print(f"{counter}")
            cyclus.append(counter)
        
        nums = cyclus.copy()
        print(nums)
        
        print(utilitys.least_common_multiple(nums))
            
        print(nums)
        
def equal(list):
    n = list[0]
    for i in list:
        if i != n:
            return False
    return True
        
def getStartingPoints(dict):
    positions = []
    for key in dict:
        if key[-1] == 'A':
            positions.append(key)
    return positions
        
        
def getDict(lines):
    dict = {}
    for i in range(1, len(lines), 1):
        line = lines[i]
        (idx, tup_string) = line.split(" = ")
        tup = tuple(x for x in tup_string[1:-2].split(', '))
        dict[idx] = tup
    return dict
        
if __name__ == "__main__":
    main()