#Indentation
def my_function():
    if True:
        print("Use 4 spaces for indentation")     #correct

        #Use 2 blank lines before top-level definitions.
        #Use 1 blank line inside classes between methods.  
      
def top_level_function():
    pass


class MyClass:
    def method_one(self):
        pass

    def method_two(self):
        pass


# Naming Conventions
# GOOD
data_analysis.py

# BAD
DataAnalysis.py

# Good
user_name = "Alice"
total_count = 42

# Bad
UserName = "Alice"
totalCount = 42

# Good
def calculate_average():
    pass

# Bad
def CalculateAverage():
    pass

# Good
utils.py
math_tools.py

# Bad
MathUtils.py
MathTools.py

# OK for counters
for i in range(5):
    print(i)

# Not OK for important variables
d = {'a': 1}  # what does 'd' mean?


# Docstrings
def greet(name):              #Use triple quotes (""")
    """Return a greeting message for a given name."""
    return f"Hello, {name}!"


#Classes
class Dog:                    #Use CamelCase names.

    """A class representing a dog."""

    def __init__(self, name):
        self.name = name

    def bark(self):
        return "Woof!"

# Good
class BankAccount:
    pass

# Bad
class bank_account:
    pass


#Whitespace Rules
# Bad spacing
x=1
y =2
z= 3

# Good spacing
x = 1
y = 2
z = 3

# Bad
value=10*5+1

# Good
value = 10 * 5 + 1

# Good
if x == 10:
    print("x is ten")

# Bad
if (x == 10) :
    print("x is ten")
