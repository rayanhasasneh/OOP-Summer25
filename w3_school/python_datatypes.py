#python_strings
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#python_Booleans
#True or False values
#Evaluate two variables:
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

#python_lists
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#The del keyword also removes the specified index  also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist
#Sort the list descending
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#python_Tuples
#To create a tuple with only one item, you have to add a comma after the item
thistuple = ("apple",)
print(type(thistuple))
#Change Tuple Values:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
# we are also allowed to extract the values back into variables. This is called "unpacking":
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#python_sets
#Set items are unordered, unchangeable, and do not allow duplicate values.
#You can use the | operator instead of the union() method, and you will get the same result.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#The update() method inserts all items from one set into another.
#The update() changes the original set, and does not return a new set.
#Keep ONLY the duplicates.The intersection() method will return a new set  & 
#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
#The values True and 1 are considered the same value. The same goes for False and 0.


