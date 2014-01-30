from fuckfuck.language import Commands

class FFParser(object):
    _lines = None
    _tokens = []

    @classmethod
    def from_file(cls, path):
        with open(path, 'r') as f:
           content = f.read()
           cmd = []
           lines = content.split("uck\n")
           for line in lines:
                if "uck" in line:
                    cmds = line.split("uck")
                    cmd += cmds
                else:
                    cmd.append(line)

        return cls(cmd)

    def __init__(self, lines):
        self._lines = lines

    def get_tokens(self):
        for line in self._lines:
            line = line.strip()
            if "f"*len(line) == line.strip():
                if len(line) in Commands:
                    self._tokens.append(len(line.strip()))
            else:
                raise SyntaxError(line)

        return self._tokens

class SyntaxError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "Invalid syntax: " + str(self.value)
