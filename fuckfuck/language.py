class BaseCommands(object):
    INCREMENT_POINTER = 1
    DECREMENT_POINTER = 2
    INCREMENT_VALUE   = 3
    DECREMENT_VALUE   = 4
    OUTPUT_VALUE      = 5
    INPUT_VALUE       = 6
    LOOP_BEGIN        = 7
    LOOP_END          = 8

    __commands = [
        INCREMENT_POINTER,
        DECREMENT_POINTER,
        INCREMENT_VALUE,
        DECREMENT_VALUE, 
        OUTPUT_VALUE, 
        INPUT_VALUE,
        LOOP_BEGIN,
        LOOP_END
    ]

    def __getattr__(self, command):
        if not command in self:
            raise AttributeError 
        return self.command

    def __iter__(self):
        return iter(self.__commands)

Commands = BaseCommands()
