# print a hello world on the screen
print('Hello')

# create a variable 
x = 5
name = "rayan"

# create a dictionary
country1 = {
    'name' :'Egypt',
    'population' : '107 million',
    'continent' : 'Africa',
    'capital_city' : 'Cairo',
    'biggest_cities' : ["Cairo","Alexandria","Giza"]
     }

# create classes and objects
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

Persons = [Person("John", 36), Person('tom', 23), Person('ali', 45)]
print(Persons[1].age)

# Using list comprehension, how can you extract from a list of fruits only those whose names contain the letter "a"?
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# How can you use unpacking in Python to assign the first two items of a tuple to individual variables, and store the remaining items in a list?
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# Write a function called add that takes two numbers and returns their sum.
def add(a, b):
    return a + b
result = add(5, 3)
print(result)  # Output: 8

# How do you write a while loop in Python that prints numbers from 1 to 9?
i = 1
while i < 10:
  print(i)
  i += 1

# You have a custom Python module named mymodule.py with the following content:
def greeting(name):
    print("Hello, " + name)
# How would you import this module and call the greeting function in another Python script?
import mymodule

mymodule.greeting("Alice")

# Given the string b = "Hello, World!", how can you print just the word "Hello" from the string?
b = "Hello, World!"
print(b[:5])

# How can you check if the value of a is not equal to b in Python?
a != b

