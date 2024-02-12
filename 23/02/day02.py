source = 'input.txt'

max_red = 12;
max_green = 13;
max_blue = 14;

with open(source, 'r') as file:
    lines = file.readlines()
    
    id_sum = 0;
    
    i = 1;
    for line in lines:
        print(line, "  ", i)
        parts = line.split(';')
        
        lineIsLegal = True;
        
        for part in parts:
            part = part.split(':', 1)[-1].strip()
            # Zerlege jedes Teil weiter in Farbe und Anzahl
            color_count_pairs = [item.strip().split() for item in part.split(',')]

            # Iteriere über die Farb-Zahlen-Paare und gib die Anzahl der Zahlen vor jeder Farbe aus
            for pair in color_count_pairs:
                if len(pair) == 2:
                    count, color = pair
                    print(f"Vor {color} stehen {count} Zahlen")
                    
                    if color == "red" and int(count) > max_red:
                        lineIsLegal = False
                    if color == "green" and  int(count) > max_green:
                        lineIsLegal = False
                    if color == "blue" and int(count) > max_blue:
                        lineIsLegal = False
                    
                else:
                    print(f"Ungültiges Farb-Zahlen-Paar: {pair}")
        
        if lineIsLegal:
            id_sum = id_sum + i
        i = i + 1;
        
    print("[", id_sum, "]")