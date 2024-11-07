employees = [
    {"name": "John Doe", "salary": 50000},
    {"name": "Jane Doe", "salary": 60000},
    {"name": "Will Smith", "salary": 70000},
    {"name": "Mark Smith", "salary": 80000},
    {"name": "Tom Smith", "salary": 90000}
]

def calculate_tax(salary, tax_rate):
    tax = salary * tax_rate
    return tax

def take_home(salary, tax_rate):
    tax = calculate_tax(salary, tax_rate)

    take_home = salary - tax
    return take_home


tax_rate = 0.16

for employee in employees:
    name = employee["name"]
    salary = employee["salary"]
    
    salary_float = float(salary)
    
    take_home_amount = take_home(salary_float, tax_rate)
    
    message = f"Employee: {name}, Salary: {salary_float}, Take Home: {take_home_amount}"
    print(message)
