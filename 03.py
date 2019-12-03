from aoc import splitted_lines

wires = splitted_lines(lambda x: (x[0], int(x[1:])), ',')


def manhattan(x, y):
    return abs(x) + abs(y)


grid = {}
directions = {
    'U': (0, -1),
    'R': (1, 0),
    'D': (0, 1),
    'L': (-1, 0),
}

for i in range(2):
    wire_id = i + 1
    x, y, distance = 0, 0, 0
    for direction, steps in wires[i]:
        dx, dy = directions[direction]
        for step in range(steps):
            x += dx
            y += dy
            distance += 1
            if (x, y) not in grid:
                grid[x, y] = (0, 0)
            wire, previous_distance = grid[x, y] if (x, y) in grid else (0, 0)
            grid[x, y] = (wire_id | wire, previous_distance + distance)


part_1 = min(manhattan(*pos) for pos, (wire, _) in grid.items() if wire == 3)
part_2 = min(distance for wire, distance in grid.values() if wire == 3)

print('part 1:', part_1)
print('part 2:', part_2)
