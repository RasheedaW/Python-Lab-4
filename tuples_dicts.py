# Create a tuple of months
months = ("January", "February", "March", "April",
          "May", "June", "July", "August",
          "September", "October", "November", "December")

# Print first and last month
print("First month:", months[0])
print("Last month:", months[-1])

# Try to change a tuple
try:
    months[0] = "NewMonth"
except TypeError as error:
    print("Tuples are immutable, error:", error)

# Create a dictionary of students and grades
students = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 78
}

# Add a new student
students["David"] = 92
print("After adding David:", students)

# Update a grade
students["Bob"] = 95
print("Updated Bob's grade:", students["Bob"])

# Print all students and grades
for name, grade in students.items():
    print(name + ":", grade)