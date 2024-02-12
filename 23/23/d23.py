import collections

def parse(task_input):
    _map = {}
    for row_index, line in enumerate(task_input):
        for column_index, character in enumerate(line):
            _map[row_index, column_index] = character

    return _map


def get_neighbors(hiking_map, point):
    if hiking_map[point] == 'v':
        yield point[0] + 1, point[1]
        return

    if hiking_map[point] == '^':
        yield point[0] - 1, point[1]
        return

    if hiking_map[point] == '>':
        yield point[0], point[1] + 1
        return

    if hiking_map[point] == 'v':
        yield point[0], point[1] - 1
        return

    for direction in ((0, -1), (1, 0), (-1, 0), (0, 1)):
        new_point = point[0] + direction[0], point[1] + direction[1]
        if new_point not in hiking_map or hiking_map[new_point] == '#':
            continue

        yield new_point


def find_the_longest_path(hiking_map, start, end):
    to_check = collections.deque([(*start, set())])
    cost_so_far = dict()
    cost_so_far[start] = 0

    while to_check:
        row_index, column_index, path = to_check.pop()

        if (row_index, column_index) == end:
            continue

        for new_point in get_neighbors(hiking_map, (row_index, column_index)):
            new_cost = cost_so_far[row_index, column_index] + 1

            if new_point in path:
                continue

            if new_point not in cost_so_far or new_cost > cost_so_far[new_point]:
                cost_so_far[new_point] = new_cost

                new_path = path.copy()
                new_path.add(new_point)

                to_check.appendleft((*new_point, new_path))

    return cost_so_far[end]


def solution(task_input):
    hiking_map = parse(task_input)
    max_rows = max(row for row, _ in hiking_map.keys())
    start = next( point for point, tile in hiking_map.items() if point[0] == 0 and tile == '.' )
    end = next(point for point, tile in hiking_map.items() if point[0] == max_rows and tile == '.')

    return find_the_longest_path(hiking_map, start, end)

with open("input_23.txt", 'r') as f:
    print(solution(f))