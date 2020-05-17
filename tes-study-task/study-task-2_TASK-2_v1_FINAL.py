#region Main "Title"
# coding=utf-8
"""Study Task 2 -Task 2
Author: Russell Dyson
Custom region folding: "Visual Studio Code Custom Folding Extension" (maptz)
"""
#endregion
#region Main "Setup Environment"
import os, random
os.system('cls')
class style:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
#endregion

#region Main "Docstring"
"""Task 2: Simulate 100 rolls of a die
Write a program to simulate 100 rolls of a die. Use the randint () function 
from the random module to generate random numbers between 1 and 6 inclusive,
and use a list to keep count of how many 1s, 2s, 3s etc. have been ‘rolled’.
Remember the first item in a list is index 0. To set the value of an item in
the list tally, you may find it helpful to use something like:
tally[score-1] = tally[score-1]+1
The program should output the results showing the table of frequencies for
each number.
"""
#endregion
#region Main "100 Dice Rolls"
scoreboard = [0,0,0,0,0,0]
def diceRolls(rolls):
    print(
    style.BOLD + style.UNDERLINE + 
    "100 Dice Rolls" + style.END
    )
    print(
        style.PURPLE + 
        "\nThis programme will randomly roll and dice 100\n" +
        "times and populate an array with the number of\n" +
        "rolls for each number (between 1 and 6)\n" +
        style.END
        )   
    minDice = int(0)
    maxDice = int(6)
    loop = True
    while loop == True:
        print("Do you want to roll (YES, yEs, yes, y)?")
        print("Any other response will quit!\n")
        loop = ("y" or "yes") in input().lower()
        if loop == True:
            for diceRoll in range(minDice,maxDice):
                print(
                    style.YELLOW + 
                    ("Dice Number:{0:^6} >>> Number Count:{1:^9}\n" \
                    .format(diceRoll + 1, rolls[diceRoll])) 
                    + style.END
                    )
        else:
            loop = False
            print(style.RED + "\nQuitting!\n" + style.END)

for maxRolls in range(100):
    minDiceRange = int(0)
    maxDiceRange = int(6)
    score = random.randint(minDiceRange,maxDiceRange)
    scoreboard[score - 1] = scoreboard[score - 1] + 1
#endregion

# Call all functions from within main()
#region Main
def main():
    diceRolls(scoreboard)
#endregion

# Call main() function
main()
