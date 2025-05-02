class City:
    def __init__(self, name, country, population, landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks

myCity = City("Gdansk", "Poland", 477000, ["Kopernik", "Fontanna"])
print(vars(myCity))