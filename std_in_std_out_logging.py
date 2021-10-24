import sys


class LoggerOut:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.filename = filename

    def write(self, message):
        self.terminal.write(message)
        with open(self.filename, "a") as file:
            print(message, file=file, flush=True, end='')

    def flush(self):
        pass


class LoggerIn:
    def __init__(self, filename):
        self.terminal = sys.stdin
        self.filename = filename

    def readline(self):
        entry = self.terminal.readline()
        with open(self.filename, "a") as file:
            print(entry.rstrip(), file=file, flush=True)
        return entry


default_log = 'default.txt'
sys.stdout = LoggerOut(default_log)
sys.stdin = LoggerIn(default_log)