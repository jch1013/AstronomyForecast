class dso:
    def __init__(self, name, rise, sets, apex):
        self.name = name
        self.rise = rise
        self.sets = sets
        self.apex = apex

    def __str__(self):
        return f"Object: {self.name}\nRise time: {self.rise}\nSet time: {self.sets}\nApex: {self.apex}\n"