

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

    def get_modes(self, instruction):
        opcode = instruction % 100
        yield opcode
        instruction //= 100
        param_count = Intcode.param_count[opcode]
        for _ in range(1, param_count):
            yield instruction % 10
            if instruction:
                instruction //= 10

    def run(self, intcode, *, noun=None, verb=None, input_stream=None):
        if input_stream:
            input_gen = iter(input_stream)
        memory = [*intcode]
        pointer = 0
        if noun is not None:
            memory[1] = noun
        if verb is not None:
            memory[2] = verb
        output = []
        while True:
            opcode, *modes = self.get_modes(memory[pointer])
            if opcode == 99:
                break
            values = [x for x in memory[pointer+1:pointer+1+len(modes)]]
            modded = [x if modes[i] else memory[x]
                      for i, x in enumerate(values)]

            if opcode == 1:
                memory[values[2]] = modded[0] + modded[1]
            elif opcode == 2:
                memory[values[2]] = modded[0] * modded[1]
            elif opcode == 3:
                memory[values[0]] = next(input_gen)
            elif opcode == 4:
                output.append(modded[0])
            elif opcode == 5:
                if modded[0] != 0:
                    pointer = modded[1]
                    continue
            elif opcode == 6:
                if modded[0] == 0:
                    pointer = modded[1]
                    continue
            elif opcode == 7:
                memory[values[2]] = (modded[0] < modded[1]) * 1
            elif opcode == 8:
                memory[values[2]] = (modded[0] == modded[1]) * 1
            else:
                raise Exception(f'opcode {opcode} not an accepted value')
            pointer += Intcode.param_count[opcode]
        return (memory, output)

    def test(self):
        from test import test as test
        run = self.run
        # day 2 part 1 tests
        test([3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
             run([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])[0])
        test([2, 0, 0, 0, 99], run([1, 0, 0, 0, 99])[0])
        test([2, 3, 0, 6, 99], run([2, 3, 0, 3, 99])[0])
        test([2, 4, 4, 5, 99, 9801], run([2, 4, 4, 5, 99, 0])[0])
        test([30, 1, 1, 4, 2, 5, 6, 0, 99],
             run([1, 1, 1, 4, 99, 5, 6, 0, 99])[0])


__intcode__ = Intcode()
__intcode__.test()

run = __intcode__.run
