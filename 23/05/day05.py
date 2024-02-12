with open('input_05.txt', 'r') as file:
    lines = file.readlines()
    
    # get seed numbers from first line
    seeds = [int(s) for s in (lines[0].split(":"))[1].split() if s.isnumeric()]
    print(seeds)
    
    # seed_to_soil_map
    # soil_to_fertilizer_map
    # fertilizer_to_water_map
    # water_to_light_map
    # light_to_temperature_map
    # temperature_to_humidity_ma
    # humidity_to_location_map
    map = [[] for _ in range(7)]
    seedidx = 0
    while seedidx < len(seeds):
        print(f"------- use seed {seedidx} ({seeds[seedidx]}) -------")
        pointer = 1
        for i in range(7):
            print(f" # step {i} #")
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
                    print(f"minFrom: {minFrom}")
                    print(f"maxFrom: {maxFrom}")
                    print(f"minTo  : {minTo}")
                    
                    diff = seed - minFrom
                    seeds[seedidx] = minTo + diff
                    swapped = True
                    print(f"swapping: {seed} -> {seeds[seedidx]}")
                    print(f"{pointer}: {lines[pointer]}")
                pointer += 1
        seedidx += 1
    
    print(seeds)
    minSeed = seeds[0]
    for seed in seeds:
        if seed < minSeed:
            minSeed = seed
    print(minSeed)
    