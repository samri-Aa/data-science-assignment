def generate_fibonacci(terms: int) -> list[int]:
    # Handle edge cases gracefully
    if terms <= 0:
        return []
    if terms == 1:
        return [0]
    
    # Initialize sequence and build iteratively for memory efficiency
    sequence = [0, 1]
    for _ in range(2, terms):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

if name == "main":
    # Prompt user, generate sequence, and display result
    try:
        count = int(input("Enter number of terms: "))
        print(f"Fibonacci sequence: {generate_fibonacci(count)}")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
