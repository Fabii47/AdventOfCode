import utilities as util

def main():
    data = util.get_as_int_list()
    task_1(data)
    

def task_1(data):
    print(sum([data[i] > data[i-1] for i in range(1, len(data))]))

if __name__ == "__main__":
    main()