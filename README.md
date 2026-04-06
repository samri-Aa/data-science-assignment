# data-science-assignment
This is a small Python program I wrote that takes a number from the user and tells them whether it's prime or not. It's straightforward, but there's a neat little optimization under the hood that makes it more efficient than the obvious approach.
What Even Is a Prime Number?
A prime number is any number greater than 1 that can't be divided evenly by anything other than 1 and itself. So 7 is prime, but 8 isn't — because 8 can be divided by 2 and 4.
Some examples: 2, 3, 5, 7, 11, 13, 17...
How the Code Works
The core of the program is the is_prime(n) function. Here's what it does step by step:
First, it immediately returns False for any number that's 1 or less — those are never prime by definition.
Then, instead of checking every number from 2 all the way up to n, it only checks up to the square root of n. This is the key optimization.
If it finds any number that divides evenly into n, it returns False — the number isn't prime.
If it gets through the whole loop without finding a divisor, it returns True — the number is prime.
Why the Square Root?
Here's the intuition: if a number n has a factor bigger than its square root, then it must also have a matching factor that's smaller than the square root. So by the time we've checked everything up to √n, we've already indirectly covered everything above it too. No need to keep going.
For large numbers, this makes a real difference in speed.
Running the Program
You just need Python 3. No installs, no dependencies — run it directly:
python prime number checker.py
It'll ask you to enter a number and give you an instant answer:
Enter a number: 17
17 is a prime number.
Enter a number: 10
10 is not a prime number.
The Code
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
Requirements
Python 3
No external libraries needed
Author
Samrawit Alemeshet
Python Foundations – Daily Assignment  Level 1"
