with open('input.txt', 'r') as file:
    lines = file.readlines()
    
    # S at 49, 96
    ze = 42
    sp = 25
    
    print(lines[ze][sp])
    
    ze += 1
    length = 1
    prev = "N"
    while lines[ze][sp] != "S":
        print(f"{length}: reading {lines[ze][sp]} from {prev} at {ze},{sp}")
        length += 1
        match lines[ze][sp]:
            case "L": # NE
                if prev == "N": # N 2 E
                    sp += 1
                    prev = "W"
                elif prev == "E": # E 2 N
                    ze -= 1
                    prev = "S"
                else:
                    print("ERROR")
                    break;
            case "F":
                if prev == "S":
                    sp += 1
                    prev = "W"
                elif prev == "E":
                    ze += 1
                    prev = "N"
                else:
                    print("ERROR")
                    break;
            case "7":
                if prev == "S":
                    sp -= 1
                    prev = "E"
                elif prev == "W":
                    ze += 1
                    prev = "N"
                else:
                    print("ERROR")
                    break;
            case "J":
                if prev == "N":
                    sp -= 1
                    prev = "E"
                elif prev == "W":
                    ze -= 1
                    prev = "S"
                else:
                    print("ERROR")
                    break;
            case "-":
                if prev == "W":
                    sp += 1
                elif prev == "E":
                    sp -= 1
                else:
                    print("ERROR")
                    break;
            case "|":
                if prev == "S":
                    ze -= 1
                elif prev == "N":
                    ze += 1
                else:
                    print("ERROR")
                    break;
            case ".":
                print("Dead End")
                break;
                
    
    print(length // 2)