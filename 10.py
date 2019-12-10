from aoc import lines
from math import atan2, pi


def get_vector(p0, p1):
    dy, dx = p1[0]-p0[0], p1[1]-p0[1]
    angle = (2.5*pi - atan2(-dy, dx)) % (2*pi)
    distance = (dy**2 + dx**2)**.5
    return angle, distance


targets = {(y, x) for y, row in enumerate(lines())
           for x, cell in enumerate(row) if cell == '#'}

station = {}
for origin in targets:
    vectors = {}
    for target in targets:
        if origin != target:
            angle, distance = get_vector(origin, target)
            vectors.setdefault(angle, []).append((distance, target))
    station = max(vectors, station, key=len)

vaporized = [target for _, target in
             sorted(((index, origin, distance), target)
                    for origin, values in station.items()
                    for index, (distance, target) in enumerate(values))]

part_1 = len(station)
vy, vx = vaporized[199]
part_2 = vx*100 + vy

print('part 1:', part_1)
print('part 2:', part_2)
