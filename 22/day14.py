import utilitys
import numpy as np

ROCK = 1
AIR = 0
SAND = 2
START = -1

CAVE_SIZE = 800

def main():
    build_cave()
    sand_flood()
    print_cave()

def sand_flood():
    global SAND_COUNT
    SAND_COUNT = 0
    while move_sand() :
        pass

    print(f"{SAND_COUNT = }")

def move_sand():
    global SAND_COUNT
    SAND_COUNT += 1

    return SAND_COUNT < 3

def build_cave():
    global cave
    cave = np.zeros((CAVE_SIZE, CAVE_SIZE), dtype = int)
    cave[0][500] = START

    coords = fetch_coords_from_file("example_14.txt")

    for line in coords:
        temp_coord = line[0]
        for coord in line[1:]:
            place_rocks(temp_coord, coord)
            temp_coord = coord


def place_rocks(vec_a, vec_b):
    if vec_a[0] == vec_b[0]:
        for y in range(vec_a[1], vec_b[1] + 1):
            cave[y][vec_a[0]] = ROCK
        for y in range(vec_b[1], vec_a[1] + 1):
            cave[y][vec_a[0]] = ROCK
    else :
        for x in range(vec_a[0], vec_b[0] + 1):
            cave[vec_a[1]][x] = ROCK
        for x in range(vec_b[0], vec_a[0] + 1):
            cave[vec_a[1]][x] = ROCK


def fetch_coords_from_file(filename = "example_14.txt"):
    coords = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            coords.append([])
            for pair in line.split(" -> "):
                coords[-1].append([int(x) for x in pair.split(',')])
    return coords

def print_cave():
    for y in range(0, find_max_y() + 2):
        for x in range(find_min_x() - 1, find_max_x() + 2):
            if   cave[y][x] == AIR   : print('.', end = '')
            elif cave[y][x] == ROCK  : print('#', end = '')
            elif cave[y][x] == SAND  : print('o', end = '')
            elif cave[y][x] == START : print('+', end = '')
        print()

def find_max_y():
    for y in range(len(cave) - 1, 0, -1):
        if sum(cave[y]) != 0:
            return y
    return 0

def find_min_x():
    for x in range(0, CAVE_SIZE):
        if sum(cave[:,x]) != 0:
            return x
    return CAVE_SIZE // 2 - 1

def find_max_x():
    for x in range(CAVE_SIZE - 1, 500, -1):
        if sum(cave[:,x]) != 0:
            return x
    return CAVE_SIZE // 2 + 1

if __name__ == "__main__":
    main()