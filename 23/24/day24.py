AREA_MIN = 200_000_000_000_000
AREA_MAX = 400_000_000_000_000

def main():
    with open("input_24.txt", 'r') as f:
        hailStorm = list(map(evalRawLine, f.readlines()))

        counter = 0
        for h in range(len(hailStorm)):
            for k in range(h + 1, len(hailStorm)):
                #print(f"{hailStorm[h]} + {hailStorm[k]}")
                #(p0x, p0y, v0x, v0y) = hailStorm[h]
                #(p1x, p1y, v1x, v1y) = hailStorm[k]
                
                counter += linesCrossing(hailStorm[h], hailStorm[k])
                
                #print(get_line_intersection(p0x, p0y, v0x, v0y, p1x, p1y, v1x, v1y))
        
        print(counter)
        
def linesCrossing(hailA, hailB):
    (p0x, p0y, v0x, v0y) = hailA
    (p1x, p1y, v1x, v1y) = hailB
    
    collision = get_line_intersection(p0x, p0y, v0x, v0y, p1x, p1y, v1x, v1y)
    
    if not collision:
        return 0
    
    (x, y) = collision
    if x >= AREA_MIN and y >= AREA_MIN and x <= AREA_MAX and y <= AREA_MAX:
        return 1
    return 0
    
def get_line_intersection(p0x, p0y, v0x, v0y, p1x, p1y, v1x, v1y):
    v0x += p0x
    v0y += p0y
    v1x += p1x
    v1y += p1y
    
    s1_x = v0x - p0x;     
    s1_y = v0y - p0y;
    s2_x = v1x - p1x;     
    s2_y = v1y - p1y;

    try:
        s = (-s1_y * (p0x - p1x) + s1_x * (p0y - p1y)) / (-s2_x * s1_y + s1_x * s2_y);
        t = ( s2_x * (p0y - p1y) - s2_y * (p0x - p1x)) / (-s2_x * s1_y + s1_x * s2_y);
    except ZeroDivisionError:
        return False

    if s >= 0 and t >= 0:
        # Collision detected
        return p0x + (t * s1_x), p0y + (t * s1_y)

    return False; # No collision
        
def evalRawLine(line):
    (px, py) = line.split('@')[0].split(',')[:-1]
    (vx, vy) = line.split('@')[1].split(',')[:-1]
    return(int(px), int(py), int(vx), int(vy))

if __name__ == "__main__":
    main()