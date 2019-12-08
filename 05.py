from aoc import split
from intcode import Intcode

intcode = split(int, ',')

*_, part_1 = Intcode(intcode, [1]).output_stream
*_, part_2 = Intcode(intcode, [5]).output_stream

print('part 1:', part_1)
print('part 2:', part_2)
