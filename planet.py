class Planet:
    def __init__(self, name, rise, set, apex, direction):
        self.name = name
        self.rise = rise
        self.set = set
        self.apex = apex
        self.direction = direction

    def __str__(self):
        return f"Planet: {self.name} \n Rise time: {self.rise} \n Set time: {self.set} \n Apex: {self.apex} \n Direction: {self.direction}"

