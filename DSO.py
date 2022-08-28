class DSO:
    def __init__(self, name, rise, set, apex, direction, type, magnitude):
        self.name = name
        self.rise = rise
        self.set = set
        self.apex = apex
        self.direction = direction
        self.type = type
        self.magnitude = magnitude

    def __str__(self):
        return f"Object: {self.name}\nType: {self.type}\nMagnitude: {self.magnitude}\nRise time: {self.rise}\nSet time: {self.set}\nApex: {self.apex}\nDirection: {self.direction}"