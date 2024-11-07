first_name = "James"
last_name = "Smith"

students = ["James Smith", "John Doe", "Will Smith"]


message_1 = "Hello parent your child, " + first_name + " Will be sent home today"
message_2 = f"Hello parent your child, {first_name}, Will be sent home today"
message_3 = "Hello parent your child, {}, Will be sent home today".format(first_name)


for student in students:
    message = "Hello parent your child," + student + " Will be sent home today"
    print(message)