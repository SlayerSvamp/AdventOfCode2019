from functools import reduce
from aoc import splitted_lines

lines = [list(zip(line[::2], line[1::2]))
         for line in splitted_lines(regex=r',? =?>? ?')]
reactions = dict((key, (int(amount), [(int(i), c) for i, c in values]))
                 for *values, (amount, key) in lines)

total_ore = 1000_000_000_000
costs = {}
deposit = dict((key, 0) for key in reactions)
deposit['ORE'] = total_ore


def get_cost(chemical, amount):
    global deposit
    deposit[chemical] -= amount
    if chemical == 'ORE':
        return
    while deposit[chemical] < 0:
        units, components = reactions[chemical]
        for cost, component in components:
            get_cost(component, cost)
        deposit[chemical] += units


get_cost('FUEL', 1)

part_1 = total_ore - deposit['ORE']
fuel = total_ore // part_1
fuel -= 10000
deposit = dict((key, fuel * value) for key, value in deposit.items())
deposit['ORE'] = total_ore - part_1*fuel
while deposit['ORE'] >= 0:
    get_cost('FUEL', 1)
    fuel += 1

part_2 = fuel - 1
print('part 1:', part_1)
print('part 2:', part_2)

if part_2 <= 3151632:
    print('too low!')
