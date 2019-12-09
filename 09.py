from aoc import split
from intcode import Intcode

intcode = split(int, ',')
part_1 = Intcode(intcode, [1]).read_output()
part_2 = Intcode(intcode, [2]).read_output()


print('part 1:', part_1)
print('part 2:', part_2)
