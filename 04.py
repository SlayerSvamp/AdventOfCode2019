from re import search
start, end = 156218, 652527


def valid(password):
    return search(r'(.)\1', password) and all(password[i] <= password[i + 1] for i in range(len(password) - 1))


def still_valid(password):
    return any(not search(str(d)*3, password) for d in range(10) if search(str(d)*2, password))


possibles = [*map(str, range(start, end))]
possibles = [*filter(valid, possibles)]
part_1 = len(possibles)

possibles = [*filter(still_valid, possibles)]
part_2 = len(possibles)

print('part 1:', part_1)
print('part 2:', part_2)
