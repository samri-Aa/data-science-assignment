def is_prime(n):
    """
    Function to check if a number is prime.
    A prime number is only divisible by 1 and itself.
    """
    if n <= 1:
        return False
    
    # Check divisors from 2 up to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

# Main program execution
try:
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter a whole number.")
