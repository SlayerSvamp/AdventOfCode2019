from aoc import split
from intcode import Intcode

intcode = split(int, ',')

part_1 = Intcode(intcode).run(1).last()
part_2 = Intcode(intcode).run(5).last()

print('part 1:', part_1)
print('part 2:', part_2)
