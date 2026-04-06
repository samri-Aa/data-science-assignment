def is_prime(n: int) -> bool:
    # Validate base cases per mathematical definition of primality
    if n < 2:
        return False
    # Iterate only up to the square root for optimal performance
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if name == "main":
    # Ensure clean input handling and clear user feedback
    try:
        num = int(input("Enter an integer: "))
        status = "prime" if is_prime(num) else "not prime"
        print(f"{num} is {status}.")
    except ValueError:
        print("Invalid input. Please provide a whole number.")
