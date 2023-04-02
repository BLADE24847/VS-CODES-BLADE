import random 

my_list = [1, 2 , 3]

computer_pick = random.choice(my_list)

player_pick = int(input("choose a number between 1,2 and 3 --"))


if computer_pick == player_pick:
    print("you win!")
else:
    print("you lose")
