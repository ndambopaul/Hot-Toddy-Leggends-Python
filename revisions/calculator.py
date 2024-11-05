# we want users to perform: addition, subtraction, multiplication, and division

num_1 = input("Enter the first number: ")
operator = input("Enter an operator (+, -, *, /): ")
num_2 = input("Enter the second number: ")

int_num_1 = int(num_1)
int_num_2 = int(num_2)

result = 0
if operator == "+":
    result = int_num_1 + int_num_2

elif operator == "-":
    result = int_num_1 - int_num_2

elif operator == "*":
    result = int_num_1 * int_num_2

elif operator == "/":
    result = int_num_1 / int_num_2
    
else:
    print("Invalid operator")

print(result)