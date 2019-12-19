from aoc import raw
from itertools import count
phase = list(map(int, raw))
pattern_base = [0, 1, 0, -1]
patterns = []


def generate_pattern(n, length):
    li = list()
    for i in count():
        li += [pattern_base[i % 4]] * n
        if len(li) > length:
            return li[1:]


def next_phase(current, depth=1):
    phase = list()
    for n in range(len(current)):
        new = sum(x*y for x, y in zip(current, patterns[n]) if x and y)
        phase.append(abs(new) % 10)
    if 100 > depth:
        return next_phase(phase, depth+1)
    return phase


offset = int(raw[:7])
length = len(phase)
# length *= 10_000
patterns = [generate_pattern(n+1, length) for n in range(length)]
part_1 = next_phase(phase)[:8]
# part_2 = next_phase(phase*10_000)[offset:offset+8]

print('part 1: ', *part_1, sep='')
# print('part 2: ', *part_2, sep='')
