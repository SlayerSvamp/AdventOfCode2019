from aoc import split
from intcode import Intcode
intcode = split(int, r',')


def with_input(intcode, noun, verb):
    code = Intcode(intcode)
    code.memory[1] = noun
    code.memory[2] = verb
    [*code.output_stream]
    return code.memory[0]


part_1 = with_input(intcode, 12, 2)

part_2_goal = 19690720
combinations = [(noun, verb) for noun in range(100) for verb in range(100)]
for noun, verb in combinations:
    if part_2_goal == with_input(intcode, noun, verb):
        break

part_2 = 100*noun + verb

print('part 1:', part_1)
print('part 2:', part_2)
