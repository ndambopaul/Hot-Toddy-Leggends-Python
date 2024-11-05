# Creating Lists
people = []
names = list()

vegetables = ["carrots", "kale", "spinach"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Indexing
first_element = vegetables[0]
last_element = vegetables[-1]
third_element = vegetables[2]


# Adding items into a list
# 1. Adding item to the end of the list
people.append("John")
people.append("Jane")

# 2. Adding item to the beginning of the list
people.insert(0, "Bob")

# 3. Adding item in the middle of the list
people.insert(2, "Joe")


# Removing items from a list
# 1. Removing item from the end of the list
people.pop()

# 2. Removing item from a specific index
people.pop(2)

# 3. Removing item from a list using the value
people.remove("Bob")
numbers.remove(7)


# Generating a list of numbers
# 1. Generating a list of numbers from 0 to 100
numbers_list = list(range(0, 101))

for x in range(0, 101):
    print(x)


# Converting a list into a string
# 1. Converting a list into a string
vegetables_string = ", ".join(vegetables)

students = ["John", "Jane", "Joe", "Bob", "Jane"]
names_string = "-".join(students)

print(vegetables_string)
print(names_string)