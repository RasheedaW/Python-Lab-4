# Function to divide two numbers safely
def safe_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Test division with different numbers
for a, b in [(10, 2), (10, 0)]:
    try:
        result = safe_divide(a, b)
        print("Result:", result)

    except ValueError as error:
        print("Error:", error)

    finally:
        print("Division operation completed")

# Demonstrate catching a general exception
try:
    number = int("hello")

except Exception as error:
    print("General error:", error)