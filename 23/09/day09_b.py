def main():
    with open('input.txt', 'r') as file:
        result = 0
        for line in file.readlines():
            nums = [int(x) for x in line.split() if x.isnumeric]
            triangle = getTriangle(nums)
            result += getPreviousElement(triangle)
        print(f"[{result}]")

def getPreviousElement(triangle):
    previous = 0
    for i in range(len(triangle) - 2, -1, -1):
        previous = triangle[i][0] - previous
    return previous

def getTriangle(nums):
    triangle = [nums]
    list = nums
    while(not allNull(list)):
        list = derive(list)
        triangle.append(list)
    return triangle

def derive(list):
    d = []
    for i in range(len(list) - 1):
        d.append(list[i+1] - list[i])
    return d
        
def allNull(list):
    for num in list:
        if num != 0:
            return False
    return True

if __name__ == "__main__":
    main()