# Define arithmetic operations using lambda functions for brevity
OPS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else "Error: Division by zero"
}

print("CLI Calculator | Type 'exit' to quit")

while True:
    try:
        expr = input("Enter <num1> <op> <num2> > ").strip()
        
        if expr.lower() == "exit":
            print("Calculator closed.")
            break
        
        # Parse input and validate format
        n1, op, n2 = expr.split()
        n1, n2 = float(n1), float(n2)
        
        # Execute operation if operator is valid
        if op in OPS:
            result = OPS[op](n1, n2)
            print(f"Result: {result}\n")
        else:
            print("Error: Unsupported operator. Use +, -, *, /\n")
            
    except ValueError:
        print("Error: Invalid input. Use format: <number> <op> <number>\n")
