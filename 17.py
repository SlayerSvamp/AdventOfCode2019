from aoc import split
from intcode import Intcode
from canvas import draw
intcode = Intcode(split(int, ','))
intcode.memory[0] = 2
intcode.run()

raw = ''.join(map(chr, intcode.output))
lines = raw.split('\n')
image = {}
chars = [*set(raw), 'O']
for y, line in enumerate(lines):
    for x, cell in enumerate(line):
        image[x, y] = chars.index(cell)

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
for x, y in image:
    all_in = True
    for dx, dy in directions:
        adjacent = x+dx, y+dy
        if adjacent not in image or image[adjacent] != chars.index('#'):
            all_in = False
    if all_in:
        image[x, y] = chars.index('O')
# draw(image, chars, ' ')

part_1 = sum(x*y for x,y in image if image[x,y] == chars.index('O'))

print('part 1:', part_1)
