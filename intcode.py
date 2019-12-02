

class Intcode:
    def run(self, intcode, noun, verb):
        memory = [*intcode]
        pointer = 0
        if noun is not None:
            memory[1] = noun
        if verb is not None:
            memory[2] = verb

        while True:
            if memory[pointer] == 99:
                break
            opcode, p1, p2, p3, *_ = memory[pointer:]
            if opcode == 1:
                memory[p3] = memory[p1] + memory[p2]
            elif opcode == 2:
                memory[p3] = memory[p1] * memory[p2]
            else:
                raise Exception(f'opcode {opcode} not an accepted value')
            pointer += 4
        return memory

    def test(self):
        from test import test as test

        def run(intcode):
            return self.run(intcode, intcode[1], intcode[2])
        # day 2 part 1 tests
        test([3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
             run([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]))
        test([2, 0, 0, 0, 99], run([1, 0, 0, 0, 99]))
        test([2, 3, 0, 6, 99], run([2, 3, 0, 3, 99]))
        test([2, 4, 4, 5, 99, 9801], run([2, 4, 4, 5, 99, 0]))
        test([30, 1, 1, 4, 2, 5, 6, 0, 99],
             run([1, 1, 1, 4, 99, 5, 6, 0, 99]))


__intcode__ = Intcode()
__intcode__.test()

run = __intcode__.run
