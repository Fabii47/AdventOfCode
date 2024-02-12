def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        
        #Time:        54     70     82     75
        #Distance:   239   1142   1295   1253
        time = int(lines[0].split(":")[1].replace(" ", ""))
        dist = int(lines[1].split(":")[1].replace(" ", ""))
        
        print(f"{time = }\n{dist = }")
        move = 0
        
        
        for t in range(time):
            if t * (time - t) > dist:
                move += 1
                    
        print(move)
        
if __name__ == "__main__":
    main()