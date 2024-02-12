def main():
    pass

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

with open('input.txt', 'r') as file:
    lines = file.readlines()
    final = []
    
    for line in lines:
        nums = [int(x) for x in line.split() if x.isnumeric]    # get numbers from file
        print(f"{nums} - {derive(nums)}")
        
        # walk down until 0
        print("deriving-...")
        triangle = [nums]
        list = nums
        while(not allNull(list)):
            list = derive(list)
            triangle.append(list)
            print(list)
        
        nextNums = [triangle[-1][-1]]
        for i in range(len(triangle)-2, 0, -1):
            nextNums.append(triangle[i][-1] + nextNums[-1])
            print(f"{triangle[i]} + {nextNums[-1]}")
        print(nextNums)
        print(f"{nums[-1]} {nums[-1] + nextNums[-1]}")
        final.append(nums[-1] + nextNums[-1])
    
    print(final)
    
    #sum = 0
    #for f in final:
    #    sum += f
        
    print(f"-----> {sum(final)} <-----")