from aoc import lines


def fuel(double_checker):
    def inner(x):
        value = max(x // 3 - 2, 0)
        if double_checker and value:
            value += inner(value)
        return value

    return lambda x: inner(int(x))


part_1 = sum(lines(fuel(False)))
part_2 = sum(lines(fuel(True)))

print('Part 1:', part_1)
print('Part 2:', part_2)
