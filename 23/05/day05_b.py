import math

lines = []
seeds = []

def main():
    with open('input.txt', 'r') as file:
        global lines
        lines = file.readlines()
        seedPairs = getSeedPairs(lines[0])
        
        minSeed = math.inf
        
        for pair in seedPairs:
            global seeds
            seeds = getSeeds(pair[0], pair[1])
            
            mapSeeds()
            
            minSeed = min(minSeed, min(seeds))
            print(f"minimum: {minSeed}")
            
            
            
        print(f"[{minSeed}]")

def getSeedPairs(line):
    print("creating pairs")

    list = []
    line = line.split(":")[1] # remove "seeds: "
    nums = [int(n) for n in line.split()]
    
    for i in range(0, len(nums), 2):
        list.append((nums[i], nums[i+1]))
        
    return list

def getSeeds(a, b):
    print(f"generating Seeds from {a} in range {b}")
    
    list = []
    s = a
    for k in range(0, b + 1):
        list.append(s + k)
    return list
    
def mapSeeds():
    print("mapping...")
    global seeds
    seedidx = 0
    while seedidx < len(seeds):
        progressBar(seedidx, len(seeds))
        #print(f"------- use seed {seedidx} ({seeds[seedidx]}) -------")
        pointer = 1
        for i in range(7):
            #print(f" # step {i} #")
            # to to next numbers
            while lines[pointer][0].isalpha() or lines[pointer][0] == "\n" and pointer < len(lines):
                pointer += 1
                #print(f"skipping {lines[pointer-1]}")
            
            # for each entry
            swapped = False
            seed = seeds[seedidx]
            while pointer < len(lines) and lines[pointer][0].isnumeric():
                nums = lines[pointer].split()
                minFrom = int(nums[1])
                maxFrom = int(nums[2]) + minFrom
                minTo = int(nums[0])
                
                
                if not swapped and minFrom <= seed and seed < maxFrom:
                    #print(f"minFrom: {minFrom}")
                    #print(f"maxFrom: {maxFrom}")
                    #print(f"minTo  : {minTo}")
                    
                    diff = seed - minFrom
                    seeds[seedidx] = minTo + diff
                    swapped = True
                    #print(f"swapping: {seed} -> {seeds[seedidx]}")
                    #print(f"{pointer}: {lines[pointer]}")
                pointer += 1
        seedidx += 1

def progressBar(done, total, length = 50):
    percent = (done / total) * 100
    filled_length = int(length * done // total)
    bar = '=' * filled_length + ' ' * (length - filled_length)
    print(f"\r[{bar}] {percent:.1f}%", end = "")

if __name__ == "__main__":
    main()