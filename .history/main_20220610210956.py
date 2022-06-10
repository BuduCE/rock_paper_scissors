#Rock_Paper_Scissors #Game #Zuri
#First import random module for the pc to select from the option randomly
import random

while True:
    options = ["r","p","s"]
    pc = random.choice(options)
    player = None

    #The .lower() is used to prevent error from inputting of uppercase of the options provided
    while player not in options:
        player = input("Select r for rock, p for paper, or s for scissors: ").lower()

    if player == pc:
        print("Computer chose: " + pc)
        print("Player chose: " + player)
        print("Tie")
    elif player == "r":
        if pc == "s":
            print("Computer chose: " + pc)
            print("Player chose: " + player)
            print("You win")
        elif pc == "p":
            print("Computer chose: " + pc)
            print("Player chose: " + player)
            print("You lose")
    elif player == "p":
        if pc == "s":
            print("Computer chose: " + pc)
            print("Player chose: " + player)
            print("You lose")
        elif pc == "r":
            print("Computer chose: " + pc)
            print("Player chose: " + player)
            print("You win")
    elif player == "s":
        if pc == "r":
            print("Computer chose: " + pc)
            print("Player chose: " + player)
            print("You lose")
        elif pc == "p":
            print("Computer chose: " + pc)
            print("Player chose: " + player)
            print(p"You win")

    replay = input("Do you want to play again: (Yes/ No)? ").lower()

    if replay != "yes":
        break
print("Bye")