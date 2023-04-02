import random

random_number = random.randint(1,3)

user_input = int(input("guess the number right between 1 to 100"))

if user_input == random_number:
    print("You got it right!")
else:
    print("Guess was incorrect")
