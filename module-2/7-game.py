#/usr/bin/python3
import random



def get_choice():
    Player_choice = input("Enter a choice (rock,paper, scissors):")
    options = ["rock", "paper", "Scissors"]
    computer_choice = random.choice(options)
    choices = {"player": Player_choice, "computer": computer_choice}
    return choices

def check_win (player, computer):
    print(f"you choose {player}, computer choose{computer}")
    if player == ("computer"):
        return "it is a tie!"
    elif player == "rock":
     if computer == ("scissors"):
        return " Rock smashes scissors!you win!:"
    else:
     return "paper covers rock!you lose."
    if player == "paper":
        if computer =="rock":
            return "paper covers rock!you win!"
        else:
            return "scissors cuts paper!you lose."
    elif player == "scissors":
        if computer == "paper":
            return "scissors cuts paper! you win!"
        else:
            return "Rock smashes scissors! you lose."
        
choices = get_choice()
result = check_win(choices ["player"], choices["computer"])
print(result)





