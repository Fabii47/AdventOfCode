import utilities as util

def main():
    data = util.get_as_int_list()
    task_1(data)
    task_2(data)

def task_1(data):
    print(sum([data[i] > data[i-1] for i in range(1, len(data))]))

def task_2(data):
    print(sum([sum(data[i:i+3]) > sum(data[i-1:i+2]) for i in range(1, len(data)-2)]))

if __name__ == "__main__":
    main()