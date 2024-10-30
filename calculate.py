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
