class Pokemon:
    def __init__(self, entry, name, types, description, isCaught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.isCaught = isCaught
    
    def speak(self):
        for i in range(0, 2):
            print(f"{self.name}!")
    
    def displayDetails(self):
        print(f"Entry Number: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Type: {self.types}")
        print(f"Description: {self.description}")
        if self.isCaught == True:
            print(f"{self.name} has already been caught!\n")
        else:
            print(f"You have yet to catch {self.name}.\n")

pikachu = Pokemon(25, "Pikachu", "Electric", "When it is angered, it immediately discharges the energy stored in the pouches in its cheeks.", True)
rayquaza = Pokemon(384, "Rayquaza", ["Dragon, Flying"], "Rayquaza is said to have lived for hundreds of millions of years. Legends remain of how it put to rest the clash between Kyogre and Groudon.", False)
duosion = Pokemon(578, "Duosion", "Psychic", "Since they have two divided brains, at times they suddenly try to take two different actions at once.", True)

pikachu.speak()
pikachu.displayDetails()

rayquaza.speak()
rayquaza.displayDetails()

duosion.speak()
duosion.displayDetails()