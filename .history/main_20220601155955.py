#Rock_Paper_Scissors #Game #Zuri
#First import random module for the pc to select from the option randomly
import random

options = ["r","p","s"]
pc = random.choice(options)
player = input("Select r for rock, p for paper or s for scissors: ")

print(pc)
