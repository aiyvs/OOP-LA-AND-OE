class Hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        
    def display_hero(self):
        return f"{self.name} is a {self.role} hero."

hero1 = Hero("Layla", "marksman")
print(hero1.display_hero())