import random 

my_list = ["rock", "paper", "scissors"]
computer = random.choice(my_list)

player_choice = input("pick any between rock, paper and scissors:")

if player_choice == computer:
    print("its a tie")


if player_choice == "rock" and computer == "scissors":
    print("you win!") 
elif player_choice == "scissors" and computer == "paper":
    print("you win!")
elif player_choice == "paper" and computer == "rock":
    print("you win!")
else:
    print("you lose")

