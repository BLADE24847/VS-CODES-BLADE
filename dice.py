import random 

random_number = random.randint(1,6)

user = input("if you want me to roll the dice just type 'roll' and I will roll the dice for you--")

if user == "roll":
    print(random_number)