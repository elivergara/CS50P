# Ask user for their name
name = input("What's your name? ").strip().title() #Input expects text

# name=name.strip() #Remove whitespace from str (Function assigned to variable, right to left)
# name=name.capitalize() #capitalize (only the first letter in the string)
# name=name.title() #capitalize (first letter of each word)
# name.strip().title()  # capitalize all words at once
# See top line for final line
# Say hello to user
print("Hello, " + name) #Needs to have a space after "Hello,"
print("Hello,", name, "How are you? ", end="")  #Does not need to have a space after "Hello,". Adds it automatically.
#end=\n is the default.
print(f"Hello, {name}", "What's up?", sep="*") #Format String. Default is a space " _"

print("Hello, \"Friend\"") # ESACAPING: using \

#Split user's name into first and last name
first, last = name.split(" ")
print(f"Hola, {first}")

# 1:00hr https://video.cs50.io/JP7ITIXGpHk

