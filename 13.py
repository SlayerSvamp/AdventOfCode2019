from canvas import draw
from aoc import split
from intcode import Intcode
from os import system
from time import sleep
from msvcrt import getch, kbhit
intcode = split(int, ',')

image = {}
tiles = ['  ', '██', '░░', '══', '()']
mode = input("live, play, watch or run? ")
game = Intcode(intcode)
draw_mode = mode in ['live', 'play', 'watch']
play_mode = mode in ['live', 'play']
live_mode = mode in ['live']
score = 0
sleep_length = .4 if live_mode else 0 if play_mode else .03


def read_into_image():
    global score
    while game.output:
        x, y, tile = game.take(3)
        if x == -1 and y == 0:
            score = tile
            continue
        elif (x, y) not in image or image[x, y] != tile:
            image[x, y] = tile


game.memory[0] = 2
game.run()
read_into_image()
part_1 = [*image.values()].count(2)

while game.running:
    if draw_mode:
        system('cls')
        draw(image, tiles)
        print(f'                                score: {score}')
        if play_mode:
            print('steer with: 1 (left), 2 (stay), 3 (right)')
        sleep(sleep_length)

    if play_mode:
        if live_mode:
            inp = 0
            while kbhit():
                inp = int(getch().decode("utf-8")) - 2
        else:
            inp = int(getch().decode("utf-8")) - 2
    else:
        ball, paddle = [
            x for (x, y), tile in image.items() if tile in [3, 4]]
        inp = -1 if ball < paddle else ball > paddle

    game.run(inp)
    read_into_image()


part_2 = score
print('part 1:', part_1)
print('part 2:', part_2)
