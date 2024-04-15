import utilitys

CORRECT = 1
WRONG   = 0
EVEN    = 2
TEN = 'X'

def main():
    # 6046 to low ... :()
    # 6325 false
    #lines = fetch_lines("example_13.txt")
    lines = fetch_lines()
    number = 0
    for i in range(0, len(lines), 2):
        idx = i // 2 + 1
        print(f"\n== Pair {idx} ==")
        left  = lines[i]
        right = lines[i+1]
        #print(f"\tleft : {left} -> {str_to_list(left)}")
        #print(f"\tright: {right} -> {str_to_list(right)}")

        left_sub = str_to_list(left.replace("10", TEN))
        right_sub = str_to_list(right.replace("10", TEN))
        result = compare_list(left_sub, right_sub)

        if result == CORRECT or result == EVEN:
            print("CORRECT")
            number += idx
        else :
            print("WRONG ORDER")
    
    print(f"<<< {number} >>>")

def compare_list(left, right):
    print(f" compare_list()\n  L: {left}\n  R: {right}")

    # Empty List
    if not left and not right : return EVEN
    if not left and     right : return CORRECT
    if     left and not right : return WRONG


    if both_are_num(left[0], right[0]):
        if left[0] < right[0] : return CORRECT
        if left[0] > right[0] : return WRONG
        if left[0] == right[0] : 
            return compare_list(left[1:], right[1:])

    if both_are_list(left[0], right[0]):
        left_sub  = str_to_list(left[0])
        right_sub = str_to_list(right[0])
        recursive = compare_list(left_sub, right_sub)

        if recursive == EVEN:
            return compare_list(left[1:], right[1:])
        else:
            return recursive

    # List and Num
    if isinstance(left[0], int) :
        left[0] = f"[{left[0]}]"
        return compare_list(left, right)

    if isinstance(right[0], int):
        right[0] = f"[{right[0]}]"
        return compare_list(left, right)

    print("ERROR: compare_list() reached end of method")

def both_are_num(a, b) -> bool:
    return isinstance(a, int) and isinstance(b, int) 

def both_are_list(a, b) -> bool:
    return not isinstance(a, int) and not isinstance(b, int)

def str_to_list(line : str) :
    out = []
    depth = 0
    temp = ""
    for c in line:
        match c:
            case '[' : depth += 1
            case ']' : 
                depth -= 1
                if depth == 1:
                    temp += c
                    out.append(temp)
                    temp = ""
        
        if depth > 1: temp += c

        if depth == 1 :
            if c.isdigit():
                out.append(int(c))
            elif c == TEN:
                out.append(10)
    
    if temp : out.append(temp)
    
    return out

def fetch_lines(file_name : str = "input_13.txt"):
    packages = []
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines), 3):
            packages.append(lines[i].strip())
            packages.append(lines[i+1].strip())
    return packages

if __name__ == "__main__":
    main()