
# Sets cannot contain duplicate elements

names_set = set()
groceries = {"milk", "bread", "eggs", "milk", "bread"}

print(groceries)

# Adding elements to a set
names_set.add("John")

print(names_set)

# Removing elements from a set
names_set.remove("John")

print(names_set)

# Creating a set from a list
fruits = ["apple", "banana", "cherry", "apple", "banana"]
fruits_set = set(fruits)
print(fruits_set)

