from aoc import raw
data = [*map(int, raw)]
width = 25
height = 6

selected = {}
image = {}
for z in range(len(data) // height // width):
    counts = {0: 0, 1: 0, 2: 0}
    for y in range(height):
        for x in range(width):
            cell = z*height*width + y*width + x
            counts[data[cell]] += 1
            if (x, y) not in image and data[cell] != 2:
                image[x, y] = data[cell]
    if not selected or counts[0] < selected[0]:
        selected = counts

part_1 = selected[1] * selected[2]
print('part 1:', part_1)

print('part 2:')
for y in range(height):
    row = ''
    for x in range(width):
        color = ' #.'[image[x, y]]
        row += f' {color}'
    print(row)
