def main():
    with open('input.txt', 'r') as file:
    lines = file.readlines()
    
    counter = 0
    for line in lines:
        print(".", end="")
        length = len(getStr(line))
        nums = getNum(line)
        for p in getPossibleLines(length, nums):
            if verify(p, getStr(line), getNum(line)):
                counter += 1
                
    print(f"[{counter}]")

def verify(testStr, line, Nums):
    if len(testStr) != len(line):
        print("ERROR: invalid length")
        return
    for i in range(len(line)):
        if(testStr[i] != line[i] and line[i] != "?"):
            return False
    return True

def getStr(line):
    return line.split()[0]

def getNum(line):
    return [int(x) for x in line.split()[1].split(",") if x.isnumeric()]
    
def getLen(nums):
    sum = 0
    for n in nums:
        sum += n
    sum += len(nums)-1
    return sum

def getPossibleLines(length, nums):
    totalLen = getLen(nums)
    if totalLen <= 0:
        return []
    allLines = []
    #print(f"l:{length} - n{nums} - t{totalLen}")
    #4 mit 1 1 4-3 = 1
    imax = length - totalLen + 1
    for i in range(imax):
        # push "###" all possible ways
        #print(f"i = {i}")
        leftOver = getPossibleLines(length - i - nums[0] - 1, nums[1:])
        for str in leftOver:
            #print(str)
            allLines.append("." * i + "#" * nums[0] + "." + str)
        if leftOver == []:
            allLines.append("." * i + "#" * nums[0] + "." * (imax-i-1))
    
    return allLines

if __name__ == "__main__":
    main()