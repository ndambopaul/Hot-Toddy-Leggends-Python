is_logged_in = True

if is_logged_in == True:
    print("You are logged in")
else:
    print("You are not logged in")
    
first_number = input("Enter first number: ")
math_operator = input("Enter math operator: ")
second_number = input("Enter second number: ")

int_first_number = int(first_number)
int_second_number = int(second_number)

result = 0

if math_operator == "+":
    result = int_first_number + int_second_number

elif math_operator == "-":
    result = int_first_number - int_second_number

elif math_operator == "*":
    result = int_first_number * int_second_number

elif math_operator == "/":
    result = int_first_number / int_second_number
else:
    print("Invalid operator")
    
print(result)