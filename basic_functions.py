# Function to greet a user
def greet_user(name=""):
    if name:
        print("Hello,", name + "! Welcome!")
    else:
        print("Hello! Welcome!")

# Function to add two numbers
def add_two_numbers(a, b):
    return a + b

# Function to check if a number is even
def is_even(num):
    return num % 2 == 0

# Call the functions
greet_user("Rasheeda")
greet_user()

total = add_two_numbers(5, 3)
print("Sum:", total)

print("4 is even:", is_even(4))
print("7 is even:", is_even(7))