#Rock_Paper_Scissors #Game #Zuri
#First import random module for the pc to select from the option randomly
import random

options = ["r","p","s"]
pc = random.choice(options)
#The .lower() is used to prevent error from inputting of uppercase of the options provided
player = input("Select r for rock, p for paper, or s for scissors: ").lower()

print(pc)
print(player)

if player == "r"