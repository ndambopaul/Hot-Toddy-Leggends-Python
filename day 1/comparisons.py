student_age = 23
teacher_age = 56

# Comparison operators
print(student_age > teacher_age)
print(student_age < teacher_age)
print(student_age == teacher_age)
print(student_age != teacher_age)
print(student_age >= teacher_age)
print(student_age <= teacher_age)


# Logical operators and, or, not
# TT => True
print(student_age < teacher_age and teacher_age > student_age)

# FF => False
print(student_age > teacher_age and teacher_age < student_age)
# TF => False
print(student_age < teacher_age and teacher_age < student_age)
# FT => False

print(4 < 6 or 6 > 3)
print(6 < 4 or 6 > 3)

# Not is used for negation

print(not 4 < 6)
print(not 6 < 4)
