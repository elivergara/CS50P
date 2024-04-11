# Learn the difference between a str and an int as an input
def get_guess():
    guess = int(input("Guess a number: "))
    if guess == 50:
        print("Correct!")
    else:
        print("Wrong!")
        return get_guess()

print(get_guess())
            