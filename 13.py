from canvas import draw
from aoc import split
from intcode import Intcode
from os import system
from time import sleep
from msvcrt import getch
intcode = split(int, ',')

image = {}
tiles = ['  ', '██', '░░', '══', '()']
program = Intcode(intcode)
while True:
    x, y, tile = program.take_output(3)
    if program.halted:
        break
    image[x, y] = tile

part_1 = [*image.values()].count(2)

print('part 1:', part_1)
start = len(intcode) - 840 - 840
part_2 = sum(points for tile, points in zip(
    intcode[start: start+840], intcode[start+840:]) if tile == 2)
    
print('part 2:', part_2)
if part_2 <= 10245:
    print('too low!')
if part_2 >= 10360:
    print('too high!')
if part_2 == 10342:
    print('wrong answer!')
exit()
intcode[0] = 2
program = Intcode(intcode)

score = 0
previous = 0
while True:
    x, y, tile = program.take_output(3)
    if program.halted:
        break
    if x == -1 and y == 0:
        previous = score - previous
        score = tile
    diff = (x, y) not in image or image[x, y] != tile
    image[x, y] = tile
    if diff or not program.input:
        if 3 in image.values() and 4 in image.values():
            system('cls')
            draw(image, tiles)
            print(f'                                     {score} ({previous})')
            print(program.input)
    if not program.input:
        print(sum(intcode[max(i for i, z in enumerate(intcode) if z == 0):-1]))
        c = getch().decode("utf8")
        value = int(c) - 2
        program.add_input(value)
