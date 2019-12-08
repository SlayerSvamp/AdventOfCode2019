

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

    def read_output(self):
        self.previous = self.current
        self.current = next(self.output_stream, None)
        return self.current

    def runner(self):
        pointer = 0
        while True:
            opcode, *modes = Intcode.get_modes(self.memory[pointer])
            if opcode == 99:
                break
            values = [
                x for x in self.memory[pointer+1:pointer+1+len(modes)]]
            modded = [x if modes[i] else self.memory[x]
                      for i, x in enumerate(values)]

            if opcode == 1:
                self.memory[values[2]] = modded[0] + modded[1]
            elif opcode == 2:
                self.memory[values[2]] = modded[0] * modded[1]
            elif opcode == 3:
                self.memory[values[0]], *self.input = self.input
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
                self.memory[values[2]] = (modded[0] < modded[1]) * 1
            elif opcode == 8:
                self.memory[values[2]] = (modded[0] == modded[1]) * 1
            else:
                raise Exception(f'opcode {opcode} not an accepted value')
            pointer += Intcode.param_count[opcode]
        self.halted = True
