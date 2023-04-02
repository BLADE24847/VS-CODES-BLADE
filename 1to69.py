import random 

list_game = ["rock","paper","scissors"]

computer_choice = random.choice(list_game)

player_choice = input("pick any between rock paper and scissors - ")

if computer_choice == player_choice:
    print("Its a tie")
elif player_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif player_choice == "scissors" and computer_choice == "paper":
    print("You win!")
elif player_choice == "paper" and computer_choice == "rock":
    print("You win!")
else:
    print("You lose!")
