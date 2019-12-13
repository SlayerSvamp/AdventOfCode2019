def draw(pixels, characters=' #', default=' '):
    y_min = min([y for _, y in pixels])
    y_max = max([y for _, y in pixels])
    x_min = min([x for x, _ in pixels])
    x_max = max([x for x, _ in pixels])

    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if (x, y) in pixels and pixels[x, y] < len(characters):
                character = characters[pixels[x, y]]
            else:
                character = default
            print(character, end='')
        print()
