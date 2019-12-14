from aoc import split
from intcode import Intcode
from test import test

intcode = split(int, ',')


def permutate(avail):
    def inner(avail, state=[]):
        if not avail:
            yield state
            return
        for x in avail:
            yield from inner(avail - {x}, state + [x])
    return inner({*avail})


part_1 = 0
for state in permutate(range(5)):
    output = 0
    for i in state:
        output = Intcode(intcode).run(i, output).output[-1]
    part_1 = max(output, part_1)


part_2 = 0
for state in permutate(range(5, 10)):
    state = [Intcode(intcode).run(i) for i in state]
    output = 0
    running = True
    while running:
        for code in state:
            code.push(output)
            output = code.run().last()
            running = code.running

    part_2 = max(part_2, output)

print('part 1:', part_1)
print('part 2:', part_2)
