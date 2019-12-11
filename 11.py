from aoc import split
from intcode import Intcode
intcode = split(int, ',')

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def run(start_pane):
    panes = {}
    x, y, direction = 0, 0, 0
    robot = Intcode(intcode, [start_pane])
    direction = 0
    while True:
        color, turn = robot.take_output(2)
        if robot.halted:
            break
        panes[x, y] = color
        direction = (direction + turn*2 + 3) % 4
        dx, dy = directions[direction]
        x, y = x+dx, y+dy
        robot.add_input(panes.get((x, y), 0))
    return panes


def draw(panes):
    y_min = min([y for _, y in panes])
    y_max = max([y for _, y in panes])
    x_min = min([x for x, _ in panes])
    x_max = max([x for x, _ in panes])

    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            print(' # '[panes.get((x, y), 2)]*2, end='')
        print()


panes = run(0)
part_1 = len(panes)
panes = run(1)

print('part 1:', part_1)
print('part 2:')
draw(panes)
