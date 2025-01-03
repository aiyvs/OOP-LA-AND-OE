class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
        
    def introduce(self, func):
        def jn(*args, **kwargs):
            print("Introducing...")
            func(*args, **kwargs) 
            print("This character is amazing")
        return jn
        
anime = AnimeCharacter("Naruto", "Shadow Clone Jutsu")

@anime.introduce
def character_intro():
    print(f"I am {anime.name} and I can use {anime.ability}.")  
    
character_intro()
