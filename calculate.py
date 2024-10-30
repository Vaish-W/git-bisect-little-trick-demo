def calculate_total(a, b):
    """Calculate the sum of two numbers."""
    return a + b

if __name__ == "__main__":
    print("The total is:", calculate_total(10, 5))

def calculate_difference(a, b):
    """Calculate the difference between two numbers."""
    return a - b

def calculate_total(a, b):
    """Calculate the sum of two numbers with basic error checking."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers")
    return a + b

if __name__ == "__main__":
    print(f"The total of 10 and 5 is: {calculate_total(10, 5)}")

def calculate_total(a, b):
    """Calculate the sum of two numbers, with intentional rounding error."""
    return round(a + b, 1)  # Introduces minor rounding

def calculate_product(a, b):
    """Calculate the product of two numbers."""
    return a * b

def calculate_total(a, b):
    """Calculate the sum of two numbers, but there's an intentional bug here."""
    return a * b  # Bug introduced: using multiplication instead of addition
