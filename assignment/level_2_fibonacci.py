def generate_fibonacci(terms):
    """
    Function to generate a Fibonacci sequence.
    Returns a list of numbers based on the term count.
    """
    if terms <= 0:
        return []
    elif terms == 1:
        return [0]
    
    sequence = [0, 1]
    # Generate remaining terms
    for _ in range(2, terms):
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    
    return sequence

# Main program execution
try:
    count = int(input("Enter number of terms: "))
    result = generate_fibonacci(count)
    print(f"Fibonacci sequence: {result}")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
