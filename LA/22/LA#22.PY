class bday:
    def __init__(self, theme, food):
        self.theme = theme
        self.food = food
    
    def foods(self):
        print("Foods: pansit,")
        self.__secretDish()
        
    def __secretDish(self):
        print(f" Coffee {self.food} a secret dish")
        
animeCostume = bday("Fried Chiken", "Wine")
newYear = bday("Graham", "Biko")
dinnerParty = bday("Cassava Cake", "Lechon")

animeCostume.foods()
newYear.foods()
dinnerParty.foods()