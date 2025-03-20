animals = [
    {
        "name": "Dog", #str
        "group": "Mammal", #str
        "number_of_legs": 4, #int
        "skills": ["running", "barking"], #list
    },
    {
        "name": "Eagle",
        "group": "Bird",
        "number_of_legs": 2,
        "skills": ["flying", "hunting"]
    },
    {
        "name": "Frog",
        "group": "Amphibian",
        "number_of_legs": 4,
        "skills": ["jumping"]
    },
    {
        "name": "Shark",
        "group": "Fish",
        "number_of_legs": 0,
        "skills": ["swimming"]
    },
    {
        "name": "Snake",
        "group": "Reptile",
        "number_of_legs": 0,
        "skills": [ "biting"]
    }
]
for animal in animals:
    print(animal)