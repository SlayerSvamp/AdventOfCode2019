from aoc import split
from intcode import run

intcode = split(int, ',')

_, [*tests_1, part_1] = run(intcode, input_stream=[1])
_, [*tests_2, part_2] = run(intcode, input_stream=[5])

if any(x != 0 for x in tests_1 + tests_2):
    print('tests failed!')

print('part 1:', part_1)
print('part 2:', part_2)
