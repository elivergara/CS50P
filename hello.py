# Ask user for their name
# name = input("What's your name? ").strip().title()  # Input expects text

# # name=name.strip() #Remove whitespace from str (Function assigned to variable, right to left)
# # name=name.capitalize() #capitalize (only the first letter in the string)
# # name=name.title() #capitalize (first letter of each word)
# # name.strip().title()  # capitalize all words at once
# # See top line for final line
# # Say hello to user


# def greeting():
#     print("Hello, " + name)  # Needs to have a space after "Hello,"
#     # Does not need to have a space after "Hello,". Adds it automatically.
#     print("Hello,", name, "How are you?", end="")
#     # end=\n is the default.
#     print(f"Hello, {name}", "What's up?", sep="*")  # Format String. Default is a space " _"
#     print("Hello, \"Friend\"")  # ESACAPING: using \
#     # Split user's name into first and last name
#     first, last = name.split(" ")
#     print(f"Hola, {first}")
# greeting()


# # Functions and returning
# def greet(take_input):
#     if "hello" in take_input:
#         return "Hello, there"
#     else:
#        return "I don't know what you mean."

# name = input("What's your name? ").strip().title()
# take_input = input("Greet the computer ").lower()
# greet2 = greet(take_input)
# print(greet2, name)

# Now using parameter defaults in a function
def hello(to="world"):
    print(f"Hello", to)

hello()
name = input("What's your name? ").strip().title()
hello(name)




