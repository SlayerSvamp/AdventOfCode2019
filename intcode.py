

class Intcode:
    param_count = {
        1: 4,
        2: 4,
        3: 2,
        4: 2,
        5: 3,
        6: 3,
        7: 4,
        8: 4,
        9: 2,
        99: 1,
    }

    @staticmethod
    def get_modes(instruction):
        opcode = instruction % 100
        yield opcode
        instruction //= 100
        param_count = Intcode.param_count[opcode]
        for _ in range(1, param_count):
            yield instruction % 10
            if instruction:
                instruction //= 10

    def __init__(self, intcode, input_stream=[]):
        self.memory = [*intcode]
        self.input = input_stream
        self.halted = False
        self.current = None
        self.output_stream = self.runner()

    def add_input(self, value):
        self.input.append(value)

    def take_output(self, length):
        for _ in range(length):
            yield self.read_output()

    def read_output(self):
        self.previous = self.current
        self.current = next(self.output_stream, None)
        return self.current

    def get_memory(self, address):
        if address >= len(self.memory):
            return 0
        return self.memory[address]

    def runner(self):
        pointer = 0
        relative_base = 0

        get_by_mode = [
            lambda x: self.get_memory(x),
            lambda x: x,
            lambda x: self.get_memory(relative_base+x),
        ]

        while True:
            opcode, *modes = Intcode.get_modes(self.get_memory(pointer))
            if opcode == 99:
                break
            values = [x for x in self.memory[pointer+1:pointer+1+len(modes)]]
            modded = [get_by_mode[m](v) for v, m in zip(values, modes)]
            assign_value = None
            if opcode == 1:
                assign_value = modded[0] + modded[1]
            elif opcode == 2:
                assign_value = modded[0] * modded[1]
            elif opcode == 3:
                assign_value, *self.input = self.input
            elif opcode == 4:
                yield modded[0]
            elif opcode == 5:
                if modded[0] != 0:
                    pointer = modded[1]
                    continue
            elif opcode == 6:
                if modded[0] == 0:
                    pointer = modded[1]
                    continue
            elif opcode == 7:
                assign_value = (modded[0] < modded[1]) * 1
            elif opcode == 8:
                assign_value = (modded[0] == modded[1]) * 1
            elif opcode == 9:
                relative_base += modded[0]
            else:
                raise Exception(f'opcode {opcode} not an accepted value')

            if assign_value != None:
                address = values[-1]
                if modes[-1] == 2:
                    address += relative_base
                needed_length = address + 1 - len(self.memory)
                if needed_length > 0:
                    self.memory += [0] * needed_length
                self.memory[address] = assign_value

            pointer += Intcode.param_count[opcode]
        self.halted = True
