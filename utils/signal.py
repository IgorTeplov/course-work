from collections import deque

class Signal:
    def __init__(self, func, time_line, impulces=[0]):
        self.func = func
        self.impulces = impulces

        self.base_time_line = time_line
        self.base_signal_line = [self.func(t) for t in self.base_time_line]

    def strategy(self, x, y):
        if y == 0:
            return x
        if x == y:
            return x
        return x + y

    def create_signal_line(self):
        signal_line = [0 for x in range(len(self.base_signal_line))]
        signal_pull = []
        for x in self.impulces:
            temp = deque(self.base_signal_line)
            temp.rotate(x)
            signal_pull.append(list(temp))

        for x in range(len(signal_pull)):
            for k in range(len(signal_pull[x])):

                signal_line[k] = self.strategy(signal_pull[x][k], signal_line[k])

        return signal_line

    # просто попробуйте это) это забавно)
    def signal_line_so_smesh(self, smesh):
        return [self.func(t-smesh)/2 for t in self.base_time_line]