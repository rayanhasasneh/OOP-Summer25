class Animal:
    def __init__(self, name, group, number_of_legs, skills):
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills 
    def display_info(self):
        return (f"Name: {self.name}, Group: {self.group}, "
                f"Legs: {self.number_of_legs}, Skills: {', '.join(self.skills)}")
animals =  [Animal("Dog", "Mammal", 4, ["running", "barking"]),
    Animal("Eagle", "Bird", 2, ["flying", "hunting"]),
    Animal("Frog", "Amphibian", 4, ["jumping"]),
    Animal("Shark", "Fish", 0, ["swimming"]),
    Animal("Snake", "Reptile", 0, [ "biting"])]

for animal in animals:
    print(animal.display_info())