# Python Foundations: Daily Assignment

This repository contains my solutions for today's Python Foundations assignment. I selected one task from each difficulty level and focused on writing clean, functional code that adheres to standard Python practices.

## Implementation Details

### Level 1: Prime Number Checker (level_1_prime.py)
This script evaluates whether a given integer is prime. It uses a straightforward trial division method that only checks factors up to the square root of the input number, which keeps the computation efficient. The code includes basic input validation to handle non-integer entries gracefully.

### Level 2: Fibonacci Sequence Generator (level_2_fibonacci.py)
This program generates a Fibonacci sequence based on a user-specified term count. I opted for an iterative approach rather than recursion to avoid stack overflow issues with larger inputs and to maintain predictable memory usage. It safely handles edge cases like zero or negative term requests.

### Level 3: CLI Calculator (level_3_calculator.py)
A simple command-line calculator that performs basic arithmetic operations. Each operation is handled by a dedicated function, which promotes modularity and makes the code easier to test and extend. The calculator runs in a continuous loop, parses user input dynamically, and includes explicit error handling for malformed expressions and division by zero.

## How to Run
Ensure you have Python 3.6 or higher installed. You can run each script independently from the terminal:
python level_1_prime.py
python level_2_fibonacci.py
python level_3_calculator.py
## Video Demonstration
I have recorded a brief walkthrough demonstrating how each script functions, including standard usage and edge-case handling. You can view the recording here: [Insert Loom Link]

Thank you for reviewing my submission. Please let me know if you require any adjustments or additional documentation.
