name = "Paul"
age = 45

print("Hello " + name)

first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name # String concatenation
print(full_name)

message = "Hello, my name is " + full_name +" " + " and i am " + str(age) +" years old"
f_message = f"Hello, my name is {full_name} and i am {age} years old"
fmt_message = "Hello, my name is {} and i am {} years old".format(full_name, age)
print(message)