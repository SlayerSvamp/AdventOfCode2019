from aoc import split
from intcode import Intcode
from canvas import draw

robot = Intcode(split(int, ','))

commands = {
    1: (0, -1),
    2: (0, 1),
    3: (-1, 0),
    4: (1, 0),
}
order = [3, 1, 4, 2]


def build_maze():
    x, y = 0, 0
    previous = 1
    grid = {(0, 0): 3}
    while True:
        for direction in range(4):
            direction = (direction + previous + 3) % 4
            command = order[direction]
            response = robot.run(command).pop()
            if response:
                dx, dy = commands[command]
                x, y = x+dx, y+dy
                if x == 0 and y == 0:
                    return grid
                grid[x, y] = response
                previous = direction
                break


def spread(grid, start):
    distances = {start: 0}
    current = {start}
    while any(current):
        following = set()
        for x, y in current:
            for dx, dy in commands.values():
                direction = x + dx, y + dy
                if direction in grid and direction not in distances:
                    following.add(direction)
                    distances[direction] = distances[x, y]+1
        current = following

    return distances


grid = build_maze()
target = max(grid, key=lambda d: grid[d] == 2)
distance = spread(grid, (0, 0))
oxygen = spread(grid, target)

part_1 = distance[target]
part_2 = max(oxygen.values())

draw(grid, ['  ', '██',  'Ox', 'RB'], '  ')
print('part 1:', part_1)
print('part 2:', part_2)
