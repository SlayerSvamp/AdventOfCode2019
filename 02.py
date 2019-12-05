from aoc import split
from intcode import run
intcode = split(int, r',')

[part_1, *_], _ = run(intcode, noun=12, verb=2)

part_2_goal = 19690720
for noun in range(100):
    for verb in range(100):
        [output, *_], _ = run(intcode, noun=noun, verb=verb)
        if output == part_2_goal:
            break
    else:
        continue
    break

part_2 = 100*noun + verb

print('part 1:', part_1)
print('part 2:', part_2)
