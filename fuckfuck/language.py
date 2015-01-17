class BaseCommands(object):
    INCREMENT_POINTER = "fuck"
    DECREMENT_POINTER = "fuckers"
    INCREMENT_VALUE   = "fuckity"
    DECREMENT_VALUE   = "fucking"
    OUTPUT_VALUE      = "fucked"
    INPUT_VALUE       = "fuckable"
    LOOP_BEGIN        = "fuckster"
    LOOP_END          = "fuckups"

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
