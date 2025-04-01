#naming_conventions
user_name = "Alice"    #correct
total_amount = 100

def calculate_total(price, tax):
    return price + tax


userName = "Alice"      #wrong
TotalAmount = 100      
def CalculateTotal(price, tax):  # ❌ PascalCase for function (should be snake_case)
    return price + tax


PI = 3.14159          #correct
MAX_CONNECTIONS = 100


pi = 3.14159         # wrong
MaxConnections = 100  # ❌ PascalCase (Constants should be UPPER_CASE)


#indentation
def check_number(num):
    if num > 0:  # ✅ Correct indentation
        print("Positive number")


def check_number(num):
if num > 0:      #wrong
print("Positive number")


def greet(name):         #correct
    if name:
        print(f"Hello, {name}!")  # 4 spaces indentation
    else:
        print("Hello, Guest!")  # 4 spaces indentation


def greet(name):          #wrong
    if name:
        print(f"Hello, {name}!")  # 4 spaces
	  print("Welcome!")  # ❌ Tab used instead of spaces (ERROR)
