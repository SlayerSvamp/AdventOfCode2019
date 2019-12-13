from aoc import splitted_lines
import re
from itertools import count

moon_order = ('Io', 'Europa', 'Ganymede', 'Callisto')
moons = set(moon_order)
axi = ('x', 'y', 'z')
axi_set = set(axi)
data = [[*map(int, filter(lambda v: re.match(r'^-?\d+$', v), line))]
        for line in splitted_lines(regex=r'<x=|, y=|, z=|>')]
positions = dict((moon, dict(zip(axi, values)))
                 for moon, values in zip(moons, data))
velocities = dict((moon, dict((a, 0) for a in axi)) for moon in moons)


visited = dict((axis, [set(), list()]) for axis in axi)
done = set()


def total_energy(moon):
    def inner(aspect):
        return sum(abs(value) for value in aspect[moon].values())
    return inner(positions) * inner(velocities)


def get_state(axis):
    return tuple((positions[moon][axis], velocities[moon][axis])
                 for moon in moons)


initial_states = dict((axis, get_state(axis)) for axis in axi)
loops = []
for step in count(1):
    # apply gravity
    for moon in moons:
        for other in moons - {moon}:
            for axis in axi:
                diff = positions[other][axis] - positions[moon][axis]
                if diff:
                    velocities[moon][axis] += 1 if diff > 0 else -1
    # apply velocity
    for moon in moons:
        for axis in axi:
            positions[moon][axis] += velocities[moon][axis]

    # print part 1
    if step == 1000:
        part_1 = sum(total_energy(moon) for moon in moons)

    # observe sub cycles
    for axis in axi_set - done:
        state = get_state(axis)
        if state == initial_states[axis]:
            print(f'{axis} done! {step}')
            done.add(axis)
            loops.append(step)

    if not axi_set - done:
        break


def calculate_reset(values):
    first, second, third = values
    for common in count(first, first):
        if not common % second:
            break
    for common2 in count(common, common):
        if not common2 % third:
            return common2


part_2 = calculate_reset(loops)

print('part 1:', part_1)
print('part 2:', part_2)
