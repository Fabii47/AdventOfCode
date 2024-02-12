from ast import literal_eval as make_tuple

with open('input.txt', 'r') as file:
    lines = file.readlines()
    
    path = lines[0]
    
    dict = {}
    for i in range(2, len(lines), 1):
        line = lines[i]
        idx = line.split(" = ")[0]
        tup_string = line.split(" = ")[1]
        tup = tuple(x for x in tup_string[1:-2].split(', '))
        dict[idx] = tup
        
    position = 'AAA'
    p = 0
    counter = 0
    while position != 'ZZZ':
        print(f"{position} - {path[p]}")
        if path[p] == 'L':
            position = dict[position][0]
        else:
            position = dict[position][1]
        p += 1
        if p >= len(path) - 1:
            p = 0
        counter += 1
    print(counter)
    print(path)