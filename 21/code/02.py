import utilities as util

def main():
    data = util.get_as_str_list()
    task1(data)
    task2(data)

def task1(data):
    pos   = 0
    depth = 0
    for row in data:
        dir = row.split()[0]
        num = int(row.split()[1])
        
        if dir == "forward": pos   += num
        if dir == "down"   : depth += num
        if dir == "up"     : depth -= num
    print(pos * depth)

def task2(data):
    pos = 0
    depth = 0
    aim = 0
    for row in data:
        cmd = row.split()[0]
        num = int(row.split()[1])

        if cmd == "down" : aim += num
        if cmd == "up"  : aim -= num
        if cmd == "forward":
            pos += num
            depth += aim * num
    print(pos * depth)

if __name__ == "__main__":
    main()