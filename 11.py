from aoc import split
from intcode import Intcode
from canvas import draw
intcode = split(int, ',')

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def run(start_pane):
    panes = {}
    x, y, direction = 0, 0, 0
    robot = Intcode(intcode).run(start_pane)
    direction = 0
    while robot.running:
        color, turn = robot.take(2)
        panes[x, y] = color
        direction = (direction + turn*2 + 3) % 4
        dx, dy = directions[direction]
        x, y = x+dx, y+dy
        robot.push(panes.get((x, y), 0))
        robot.run()
    return panes


panes = run(0)
part_1 = len(panes)
# draw(panes, ' #', ' ')
panes = run(1)

print('part 1:', part_1)
print('part 2:')
draw(panes, ['  ', '##'], '  ')
