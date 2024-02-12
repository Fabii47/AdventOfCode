source = 'input.txt'

with open(source, 'r') as file:
    lines = file.readlines()
    
    sum = 0
    
    for line in lines:
        line = line.split(":")
        
        (winningNums, haveNums) = line[1].split("|")
        
        print(haveNums)
        
        wNum  = [int(w) for w in winningNums.split(" ") if w.isnumeric()]
        myNum = [int(n) for n in haveNums.split() if n.strip().isnumeric()]
        print(wNum, " - ", myNum)
        
        counter = 0
        for w in wNum:
            if w in myNum:
                counter += 1
        
        if(counter > 0): 
            sum += pow(2, counter-1)
    
    print(f"total points: [{sum}]")