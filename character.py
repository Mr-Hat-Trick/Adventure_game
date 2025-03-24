class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.fighting_stlye = 0

    def __str__(self):
        return f"{self.name}\t\t\tHealth: {self.health}"

    def add_to_health(self, amount):
        self.health += amount

    def remove_health(self, amount):
        self.health -= amount

    def add_f_style(self, fighting_style):
        self.fighting_style = fighting_style