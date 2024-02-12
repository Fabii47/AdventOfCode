def main():
    global cycle_checks 
    global current_cycle
    global x_result
    global operation_cache
    global result_A
    
    with open("input_10.txt", 'r') as f:
        result_A = 0
        operation_cache = []
        x_result = 1
        cycle_checks = [x for x in range(20, 221, 40)]
        current_cycle = 1
        
        for line in f.readlines():
            if line[:4] == "noop":
                tick()
            else:
                operation_cache.append(addX(line))
                tick()
                tick()
            
        print(result_A) # 11220


def tick():
    global x_result
    global operation_cache
    global current_cycle
    global result_A
    
    # check for finished operations
    for op in operation_cache:
        if op[0] <= 0:
            x_result += op[1]
            operation_cache.remove(op)
    
    # reduce Op Counter
        operation_cache = list(map(decreaseTimer, operation_cache))
    
    # check if cycle needs 2 be tracked
    if current_cycle in cycle_checks:
        #print(f"current Cycle {current_cycle}: {x_result}")
        result_A += x_result * current_cycle
    
    # Draw CRT
    print("#" if spriteVisible() else " ", end = "\n" if current_cycle % 40 == 0 else "")

    # increase current_cycle tracker
    current_cycle += 1
    
def spriteVisible():
    return abs(x_result - ((current_cycle-1) % 40)) <= 1
    
def addX(line, delay = 2):
    return (delay, int(line.split()[1]))

def decreaseTimer(entry):
    return (entry[0] - 1, entry[1])

if __name__ == "__main__":
    main()