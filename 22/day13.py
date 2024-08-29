## 6428, but how

def main():
    file = 'input_13.txt'
    with open(file, 'r') as f:
        

        sum_of_idx = 0


        lines = f.readlines()
        for i in range(0, len(lines), 3):
            index = i // 3 + 1

            line1 = convert_string_to_list(lines[i].strip())
            line2 = convert_string_to_list(lines[i+1].strip())

            result = eval(line1, line2)

            if result:
                sum_of_idx += index

            #print(f"{index} : [{result}]")
            #print(f"\t{line1}\n\t{line2}")
            if result: print(index, end = " ")

        print(sum_of_idx)
    pass

def eval(l1 : list, l2 : list):
    #print(f"eval :  {l1}\n\t{l2}")

    i = 0
    while(True):

        if len(l1) == i: return True
        if len(l2) == i: return False

        # check if both are ints
        if type(l1[i]) == int and type(l2[i]) == int:
            if l1[i] < l2[i]: return True
            if l1[i] > l2[i]: return False

        # check if both are lists
        if type(l1[i]) == list and type(l2[i]) == list:
            result = eval(l1[i], l2[i])
            if result is not None:
                return result

        # check if l1 is int
        if type(l1[i]) == int and type(l2[i]) == list:
            l1[i] = [l1[i]]
            continue
        
        # check if l2 is int
        if type(l1[i]) == list and type(l2[i]) == int:
            l2[i] = [l2[i]]
            continue

        i += 1

    return True

def convert_string_to_list(string):
    fancy_list = []

    inside_brackets = -1
    sub_list_start = 1
    for i, c in enumerate(string):
        match(c):
            case '[': 
                inside_brackets += 1
                if inside_brackets == 1:
                    sub_list_start = i
            case ']': 
                inside_brackets -= 1
                if inside_brackets == 0:
                    fancy_list.append(convert_string_to_list(string[sub_list_start:i+1]))
            case ',': pass 
            case num:
                if inside_brackets == 0:
                    fancy_list.append(int(num))

    return fancy_list

def int_to_list(num):
    return [num]
if __name__ == "__main__":
    main()