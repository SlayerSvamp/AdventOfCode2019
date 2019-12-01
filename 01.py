from aoc import lines


def fuel_needed(x):
    return max(int(x) // 3 - 2, 0)


requirements = lines(fuel_needed)
part_1 = sum(requirements)

part_2 = 0
for fuel in requirements:
    while fuel:
        part_2 += fuel
        fuel = fuel_needed(fuel)

print('Part 1:', part_1)
print('Part 2:', part_2)
