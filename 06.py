from aoc import splitted_lines
from test import test
from itertools import count


class Node:
    def __init__(self, nodes, name):
        self.nodes = nodes
        self.name = name
        self.orbits = set()
        self.center = None

    def total_orbits(self, total=0):
        if self.center:
            return self.nodes[self.center].total_orbits(total + 1)
        return total


def generate_nodes(data):
    nodes = {}
    for center, orbit in data:
        c_node = nodes.get(center)
        o_node = nodes.get(orbit)

        if not c_node:
            c_node = nodes[center] = Node(nodes, center)
        if not o_node:
            o_node = nodes[orbit] = Node(nodes, orbit)

        c_node.orbits.add(orbit)
        o_node.center = center
    return nodes


def sum_orbits(nodes):
    return sum(node.total_orbits() for node in nodes.values())


def get_jumps(nodes):
    current = nodes['YOU'].center
    visited = {current: 0}
    latest = {current}
    for i in count(1):
        next_latest = set()
        for name in latest:
            node = nodes[name]
            for candidate in [node.center, *node.orbits]:
                if candidate and candidate not in visited:
                    next_latest.add(candidate)
                    visited[candidate] = i
        if len(nodes) == len(visited):
            break
        latest = next_latest
    return visited


# test
test_data = [['COM', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E'], ['E', 'F'], ['B', 'G'],
             ['G', 'H'], ['D', 'I'], ['E', 'J'], ['J', 'K'], ['K', 'L'], ['K', 'YOU'], ['I', 'SAN'], ]
test_nodes = generate_nodes(test_data)
test(3, test_nodes['D'].total_orbits())
test(7, test_nodes['L'].total_orbits())
test(42, sum_orbits(
    dict((name, node) for name, node in test_nodes.items() if name not in ['YOU', 'SAN'])))
test(4, get_jumps(test_nodes)[test_nodes['SAN'].center])
# end of tests

data = splitted_lines(regex=r'\)')
nodes = generate_nodes(data)
target = nodes['SAN'].center
distances = get_jumps(nodes)

part_1 = sum_orbits(nodes)
part_2 = distances[target]

print('part 1:', part_1)
print('part 2:', part_2)
