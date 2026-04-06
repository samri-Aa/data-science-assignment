# Define modular arithmetic functions as instructed
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0: raise ValueError("Division by zero is undefined.")
    return a / b

# Map string operators to corresponding functions
OPS = {"+": add, "-": subtract, "*": multiply, "/": divide}

def main():
    print("CLI Calculator | Type 'exit' to quit")
    while True:
        try:
            # Parse user input into three distinct components
            expr = input("Enter <num1> <operator> <num2> > ").strip()
            if expr.lower() == "exit":
                print("Calculator closed.")
                break
                
            n1_str, op, n2_str = expr.split()
            n1, n2 = float(n1_str), float(n2_str)
            
            # Execute operation and display formatted result
            print(f"Result: {OPS[op](n1, n2)}\n")
        except (ValueError, KeyError):
            # Handle malformed input or unsupported operators cleanly
            print("Error: Use format '<number> <+/−/*/> <number>'\n")

if name == "main":
    main()
