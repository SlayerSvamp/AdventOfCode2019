def draw(pixels, characters=' #', default=' ', *, padding=0):
    y_min = min([y for _, y in pixels]) - padding
    y_max = max([y for _, y in pixels]) + padding
    x_min = min([x for x, _ in pixels]) - padding
    x_max = max([x for x, _ in pixels]) + padding

    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if (x, y) in pixels and pixels[x, y] < len(characters):
                character = characters[pixels[x, y]]
            else:
                character = default
            print(character, end='')
        print()
