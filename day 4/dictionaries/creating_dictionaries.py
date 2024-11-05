# Creating an empty dictionary
empty_dict = {}

student = {
    "first_name": "John",
    "last_name": "Smith",
    "gender": "Male",
    "course": "Bsc. Computer Science"
}

# Getting the value of a key
student["gender"]
student["first_name"]

student.get("gender") # Get the value if it exists, else returns None
student.get("phone_number")

student.get("specialization", "N/A") # Get the value if it exists, else returns the default value

# Adding a new key-value pair
student["phone_number"] = "0745491093"
student["address"] = "123 Main Street"
print(student)

# Removing a key-value pair
del student["phone_number"]

# Updating a key-value pair
student["address"] = "00100 Nairobi, Kenya"
student["phone_number"] = "0746740960"


# Checking if a key exists
"first_name" in student
"phone_number" in student

# Iterating over a dictionary
# 1. Getting all the keys
for key in student.keys():
    print(f"Key is: {key}")
    
keys = list(student.keys())
print(keys)

# 2. Getting all the values
for value in student.values():
    print(f"Value is: {value}")
    
values = list(student.values())
print(values)

# 3. Getting all the key-value pairs
for key, value in student.items():
    print(f"Key is: {key} and value is: {value}")
    