nums = [1, 2, 3, 4, 5, 6]

names = ["John", "Paul", "George", "Ringo", "Stuart", "Keith"]

for number in nums:
    print(f"The number is {number}")
    

for name in names:
    print(f"The name is {name}")
    
    
for number in range(10):
    print(f"The number is {number}")
    
    
even_numbers = []
for number in nums:
    if number % 2 == 0:
        even_numbers.append(number)
        
print(even_numbers)


odd_numbers = []
for number in nums:
    if number % 2 == 1:
        odd_numbers.append(number)
        
print(odd_numbers)


squares = []
for number in nums:
    squares.append(number*number)
    
print(squares)