# FUnction Definition
def greetings():
    print("Hello World!!")
    
# Calling the function
#greetings()


def greet_person(name):
    message = f"Hello {name}"
    print(message)
    

#greet_person("James Smith")
#greet_person("John Doe")


def add_numbers(first_number, second_number):
    result = first_number + second_number
    print(result)
    
    
add_numbers(10, 20)


def calculate_tax(salary, tax_rate):
    tax = salary * tax_rate
    return tax


salary = 230000
tax_amount = calculate_tax(salary, 0.05)

take_home_amount = salary - tax_amount

def calculate_take_home(salary, tax_rate):
    tax_amount = calculate_tax(salary, tax_rate)
    
    take_home_amount = salary - tax_amount
    return take_home_amount


take_home = calculate_take_home(30000, 0.12)
print(take_home)