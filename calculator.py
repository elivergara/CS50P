# x = int(input("What's X "))
# y = input("What's Y ")

# z = x+int(y)

# print(z)


# # Improved
# x = int(input("What's X "))
# y = int(input("What's Y "))
# print(x+y)

# # Alternative though not necessarily improved
# print(int(input("What's X "))+int(input("What's Y ")))

# Using float
x = float(input("What's X "))
y = float(input("What's Y "))
# print(x+y)

# Rounding the result, and formatting it to use comma for the thousands
# print(f"{round(x+y):,}")

# Now try with division
z = round(x / y, 2)
print(z)
# or usinf f string:
z = x / y
print(f"{x / y:.2f}")


    
