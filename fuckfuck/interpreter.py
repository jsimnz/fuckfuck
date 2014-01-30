from fuckfuck.language import Commands
from fuckfuck.utils import getch
from sys import stdout, exit

class FFInterpreter(object):
    _pointer = 0
    _pc = 0
    _memory = [0]
    _instructions = []
    _jumptable = {}

    def __init__(self):
        self._functions = {
            Commands.INCREMENT_POINTER: self.increment_pointer,
            Commands.DECREMENT_POINTER: self.decrement_pointer,
            Commands.INCREMENT_VALUE: self.increment_value,
            Commands.DECREMENT_VALUE: self.decrement_value,
            Commands.OUTPUT_VALUE: self.output_value,
            Commands.INPUT_VALUE: self.input_value,
            Commands.LOOP_BEGIN: self.loop_begin,
            Commands.LOOP_END: self.loop_end,
        } 

    def dump(self):
        return self._memory

    def execute(self, instructions=[]):
        self._instructions = instructions
        self._build_jumptable()

        while self._pc < len(self._instructions):
            self.step(self._instructions[self._pc])
            self._pc += 1

    def _build_jumptable(self):
        stack = []
        
        for i, opcode in enumerate(self._instructions):
            if opcode == Commands.LOOP_BEGIN:
                stack.append(i)
            elif opcode == Commands.LOOP_END:
                enter = stack.pop() 

                self._jumptable[enter] = i
                self._jumptable[i] = enter    
        
        try: 
            assert len(stack) == 0
        except AssertionError:
            print "The number of LOOP BEGIN commands is not equal to the number of LOOP END commands."
            exit(1)

    def step(self, opcode):
        if opcode in Commands:
            self._functions[opcode]()

    def increment_pointer(self):
        self._pointer += 1

        if self._pointer == len(self._memory):
            self._memory.append(0)
    
    def decrement_pointer(self):
        self._pointer = 0 if self._pointer <= 0 else self._pointer -1

    def increment_value(self):
        self._memory[self._pointer] += 1

    def decrement_value(self):
        self._memory[self._pointer] -= 1

    def output_value(self):
        stdout.write(chr(self._memory[self._pointer]))

    def input_value(self):
        self._memory[self._pointer] = ord(getch())

    def loop_begin(self):
        if self._memory[self._pointer] == 0:
            self._pc = self._jumptable[self._pc] - 1

    def loop_end(self):
        if self._memory[self._pointer] != 0:
            self._pc = self._jumptable[self._pc] - 1

