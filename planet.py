class Planet:
    def __init__(self, name, rise, set, apex):
        self.name = name
        self.rise = rise
        self.set = set
        self.apex = apex

    def __str__(self):
        return f"Planet: {self.name}\nRise time: {self.rise}\nSet time: {self.set}\nApex: {self.apex}"

