'''
    Rock paper and scissors game using if, elif, else, enum, random string methods
'''
import sys
import random
from enum import Enum

class RockPaperScissors(Enum):
    ROCK = 1
    PAPER= 2
    SCISSORS = 3

print("")
userChoice = input("Enter your choice...\n\n1.for ROCK, \n2. for PAPER, or \n3.for SCISSORS.\n\n")
playerChoice = int(userChoice)


if playerChoice < 1 or playerChoice > 3:
    sys.exit("You must enter 1, 2, or 3.")
    

computerChoice = random.choice("123")
compChoice = int(computerChoice)


print("")
print("User choice is " + str(RockPaperScissors(playerChoice)).replace("RockPaperScissors.", "") + ".")
print("Computer choice is " + str(RockPaperScissors(compChoice)).replace("RockPaperScissors.", "") + ".")
print("")


if(playerChoice == 1 and compChoice == 3):
    print("🎉 You win.")
elif(playerChoice == 2 and compChoice == 1):
    print("🎉 You win.")
elif(playerChoice == 3 and compChoice == 2):
    print("🎉 You win.")
elif(playerChoice == compChoice):
    print("😲 Its a tie.")
else:
    print("😏 Computer wins.")