names = ("John", "Corey", "Adam", "Steve", "Rick", "Thomas")

user_roles = ("Admin", "Instructor", "Student")

# Tuples are immutable

first_name = names[0]
last_name = names[-1]

first_3_elements = names[:3]
last_3_elements = names[-3:]


# Tuples can be unpacked
admin, instructor, student = user_roles
print(admin)

john, corey, *other_names = names
print(john)
print(corey)
print(other_names)

for name in names:
    print(name)
    
    
# Convert tuple to a list
names_list = list(names)
print(names_list)


# Convert list to a tuple
names_tuple = tuple(names_list)
print(names_tuple)