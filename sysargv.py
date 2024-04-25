import sys
from statistics import mean

if len(sys.argv) < 3:
    print("Usage: python calc.py <number1> <number2>")
    sys.exit(1)  # Exit the script with a non-zero value indicating error

# Convert arguments to integers
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

# Perform addition
result = mean([num1, num2])
print(f"The mean between {num1} and {num2} is {result}")
