# Demonstrates else

try:
    x = int(input("What's x? "))
except ValueError:
    print("error found, x is not an integer")
else:
    print(f"x is {x}")
