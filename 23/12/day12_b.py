def main():
    global dynamicDict
    dynamicDict = {}
    with open('input.txt', 'r') as f:
        counter = 0
        lines = f.readlines()
        for i, line in enumerate(lines):
            found = recursiveCount(unfoldStr(line), unfoldNum(line))
            print(f"{found}\t{line}", end = "")
            counter += found
            
        print(f"[{counter}]")
    
def recursiveCount(string, nums):
    
    if nums == []:
        if not '#' in string: return 1
        else: return 0
    
    
    global dynamicDict
    if (string, str(nums)) in dynamicDict:
        return dynamicDict[(string, str(nums))]

    len_nums_only = sum(nums) + len(nums) - 1
    wiggle_len = len(string) - len_nums_only
    
    counter = 0
    
    for i in range(wiggle_len + 1):
        # place first num at i
        if '#' in string[:i]:
            break
        
        try:
            if string[i + nums[0]] == '#':
                continue
        except IndexError:
            pass
        # check if this position is legal:
        if '.' in string[i:i+nums[0]]:
            continue
        
        counter += recursiveCount(string[i+nums[0]+1:], nums[1:])
        
    dynamicDict[(string, str(nums))] = counter
    
    return counter
    
def unfoldNum(line):
    return 5 * [int(x) for x in line.split()[1].split(",")]
    
def unfoldStr(line):
    s = line.split()[0]
    return (s + '?') * 4 + s

if __name__ == "__main__":
    main()
