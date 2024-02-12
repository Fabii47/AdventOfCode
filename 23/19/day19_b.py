from dataclasses import dataclass

MIN_VAL = 1
MAX_VAL = 4000
SOURCE = "input.txt"

# important Workflow States
ACCEPTED = 'A'
REJECTED = 'R'
START    = "in"

@dataclass
class PartSet:
    # every Value inclusive(!)
    x_min: int
    x_max: int
    m_min: int
    m_max: int
    a_min: int
    a_max: int
    s_min: int
    s_max: int
    
    def __init__(self, x_min: int, x_max: int, m_min: int, m_max: int, a_min: int, a_max: int, s_min: int, s_max: int):
        self.x_min = x_min
        self.x_max = x_max
        self.m_min = m_min
        self.m_max = m_max
        self.a_min = a_min
        self.a_max = a_max
        self.s_min = s_min
        self.s_max = s_max
    
    def total_amount(self) -> int:
        x = self.x_max - self.x_min + 1
        m = self.m_max - self.m_min + 1
        a = self.a_max - self.a_min + 1
        s = self.s_max - self.s_min + 1
        return x * m * a * s

    def __repr__(self):
        representation = "("
        representation += f"x[{self.x_min},{self.x_max}] "
        representation += f"m[{self.m_min},{self.m_max}] "
        representation += f"a[{self.a_min},{self.a_max}] "
        representation += f"s[{self.s_min},{self.s_max}])"
        return representation
        

def main():
    print(f"starting with {4000 ** 4} total Parts...")
    
    # read states and safe instructions as string in dict
    global workflow_states
    workflow_states = read_states(SOURCE)
    
    
    # create Queue with initial PartSet
    global workflow_queue
    workflow_queue = [(START, get_init_part_set())]
    
    accepted_count = 0
    rejected_count = 0
    
    while(workflow_queue):
        (state, part) = workflow_queue.pop()
        
        if state == ACCEPTED:
            accepted_count += part.total_amount()
            continue
            
        if state == REJECTED:
            rejected_count += part.total_amount()
            continue
        
        print(f"||| {state} ||| {part} |||")
        print(f"[{part.total_amount()}]")
        for instruction in get_instructions(state):
            if isinstance(instruction, tuple):
                print(f"- {instruction}")
                part = move_fitting_parts(part, instruction)
            else:
                print(f"rest goes to {instruction}")
                workflow_queue.append((instruction, part))
                
        #break
    
    print(f"{workflow_queue = }")
    print(f"{accepted_count = }")
    print(f"{rejected_count = }")
    print(f"{accepted_count + rejected_count}")
            
# returns not fitting parts  
def move_fitting_parts(part, instruction):
    global workflow_queue
    (match, rest) = split_part(part, instruction)
    workflow_queue.append((instruction[-1], match))

    return rest

#return (matches instruction, rest)
def split_part(part, instruction):
    print(f"split_part() {part}")
    (stat, greater, value, nextState) = instruction
    
    rest = PartSet(part.x_min, part.x_max, part.m_min, part.m_max, part.a_min, part.a_max, part.s_min, part.s_max)
    
    match stat:
        case 'x':
            if greater:
                part.x_min = max(part.x_min, value + 1)
                rest.x_max = min(value, rest.x_max)
            else:
                rest.x_min = max(rest.x_min, value)
                part.x_max = min(value - 1, part.x_max)
        case 'm':
            if greater:
                part.m_min = max(part.m_min, value + 1)
                rest.m_max = min(value, rest.m_max)
            else:
                rest.m_min = max(rest.m_min, value)
                part.m_max = min(value - 1, part.m_max)
        case 'a':
            if greater:
                part.a_min = max(part.a_min, value + 1)
                rest.a_max = min(value, rest.a_max)
            else:
                rest.a_min = max(rest.a_min, value)
                part.a_max = min(value - 1, part.a_max)
        case 's':
            if greater:
                part.s_min = max(part.s_min, value + 1)
                rest.s_max = min(value, rest.s_max)
            else:
                rest.s_min = max(rest.s_min, value)
                part.s_max = min(value - 1, part.s_max)
    
    return (part, rest)

def get_instructions(state):
    print(f"get_instructions({state})", end = "")
    string = workflow_states[state]
    print(f" : {string}")
    
    instructions = list(map(raw_instruction_to_tuple, string.split(',')[:-1]))
    instructions.append(string.split(',')[-1])
    #print(f" -> {instructions}")
    return instructions
    
def raw_instruction_to_tuple(instruction):
    #print(f"raw_instruction_to_tuple({instruction})")
    stat = instruction[0]
    greater = instruction[1] == '>'
    value = int(instruction.split(":")[0][2:])
    nextState = instruction.split(":")[1]
    return (stat, greater, value, nextState)
       
def read_states(file_path):
    states = {}
    with open(file_path, 'r') as f:
        line = f.readline()
        while line != "\n":
            string = line.split("{")
            states[string[0]] = string[1].replace('}\n', '')
            line = f.readline()
    return states
       
def get_init_part_set():
    return PartSet(MIN_VAL, MAX_VAL, MIN_VAL, MAX_VAL, MIN_VAL, MAX_VAL, MIN_VAL, MAX_VAL)
        
if __name__ == "__main__":
    main()