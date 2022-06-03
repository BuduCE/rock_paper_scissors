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
        print(pc)
        print(player)
        print("Tie")
    elif player == "r":
        if pc == "s":
            print(pc)
            print(player)
            print("You win")
        elif pc == "p":
            print(pc)
            print(player)
            print("You lose")
    elif player == "p":
        if pc == "s":
            print(pc)
            print(player)
            print("You lose")
        elif pc == "r":
            print(pc)
            print(player)
            print("You win")
    elif player == "s":
        if pc == "r":
            print(pc)
            print(player)
            print("You lose")
        elif pc == "p":
            print(pc)
            print(player)
            print("You win")

    play_again = input("Do you want to play again: (Yes/ No)? ").lower()

    if play_again != "yes":
        break
print("Bye")