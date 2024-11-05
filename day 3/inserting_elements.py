# Inserting Elements in a List
numbers = [1, 4, 5, 6]
# Add an element to the end of the list
numbers.append(7)
numbers.append(8)

print(numbers)

# Adding an element at a specific index
numbers.insert(1, 2)
numbers.insert(2, 3)


even_numbers = []

for number in range(1, 11):
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)