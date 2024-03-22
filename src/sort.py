class Digit:

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value
