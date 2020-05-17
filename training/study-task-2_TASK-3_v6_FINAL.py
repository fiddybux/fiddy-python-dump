#region Main "Title"
# coding=utf-8
"""Study Task 2 -Task 3
Author: Russell Dyson
Custom region folding: "Visual Studio Code Custom Folding Extension" (maptz)
"""
#endregion
#region Main "Setup Environment"
import os
import random
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
"""Task 3: Last one loses game
The game ‘Last one loses’ is played by two players and uses a pile of n
counters. Players take turns at removing 1, 2 or 3 counters from the pile.
The game continues until there are no counters left. The loser is the person
who takes the last counter and the winner is the one who leaves only one
counter so that their opponent has to take the last counter.

Using functions, write a program to play the game so that a player can play
against the computer. The program should allow the user to specify the value
for n in the range 10 - 50 inclusive. The program acts as one player, playing
at random, and reports the number of counters left after each player’s turn.
It should prompt the user to enter the number of counters that the user wants
to remove (checking that it is a valid number of counters) and tell the user
how many counters it removes for its turn. At the end, it should state which
player has won.
"""
#endregion
#region Main "Last One Loses Game"
def totalCounters():
    print(
        style.BOLD + style.UNDERLINE + 
        "Last One Loses - The Game" + style.END
        )
    print(
        style.PURPLE + 
        "\nThe game ‘Last One Loses’ is played by two players and uses a\n" \
        "pile of counters between 10 and 50.\n\n" \
        "Players take turns at removing 1, 2 or 3 counters from the pile.\n" \
        "The game continues until there are no counters left.\n" \
        "The loser is the person who takes the last counter.\n" \
        "The winner is the one who leaves only one counter, forcing their\n" \
        "opponent to take the last counter." 
        + style.END
        )
    total_counters = input("\nHow many counters to play with (10 - 50)?: ")
    total_counters = int(total_counters)
    while True:
        if 10 <= total_counters <= 50:
            print("The number of counters selected for the game is",total_counters)
            break
        else:
            print("Invalid input! Please try again.")
            total_counters = input("How many counters to play with (10 - 50)?: ")
            total_counters = int(total_counters)
    playerDecide(total_counters)

def playerDecide(total_counters):
    whose_go = input("\nWho is going to go first? (1) Human, or (2) CPU?: ")
    whose_go = int(whose_go)
    while True:
        if whose_go == 1:
            humanTurn(total_counters)
        elif whose_go == 2:
            cpuTurn(total_counters)
        else:
            print("\nInvalid input! Choose wisely.")
            whose_go = input("Who is going to go first? (1) Human, or (2) CPU?: ")
            whose_go = int(whose_go)

def humanTurn(total_counters):
    # Print total_counters - CHECK!
    print("There are",total_counters,"counter(s) remaining")
    # Check FIRST to see how many counters are left BEFORE making choice
    # Calling function will return back to origin function when complete
    counterCheck(total_counters)
    # Puny human gets to choose how many counters
    human_counter_choice = input("\nPuny human! Choose your number of counters! (1 - 3): ")
    human_counter_choice = int(human_counter_choice)

    # Test is there are enough counters, catch errors
    while True:
        if human_counter_choice < total_counters:
            while True:
                if human_counter_choice >= 1 and human_counter_choice <= 3:
                    print("HUMAN chose",human_counter_choice,"counter(s)")
                    doTheMathHuman(total_counters,human_counter_choice)
                    break
                else:
                    print("HUMAN chose",human_counter_choice,"counter(s)")
                    print("The pathetic human chose invalid input!")
                    human_counter_choice = input("CHOOSE AGAIN! Human filth! (1 - 3): ")
                    human_counter_choice = int(human_counter_choice)
        else:
            print("\nNot enough counters left! You MUST leave 1 counter.")
            human_counter_choice = input("Foolish human! CHOOSE AGAIN!: ")
            human_counter_choice = int(human_counter_choice)
    cpuTurn(total_counters)

def cpuTurn(total_counters):
    # Print total_counters - CHECK!
    print("There are",total_counters,"counter(s) remaining")
    # Check FIRST to see how many counters are left BEFORE making choice
    # Calling function will return back to origin function when complete
    counterCheck(total_counters)
    # CPU could normally just choose randomly from valid range with randint(1,3)
    # For fun this could be changed to a higher number to taunt the human
    # Allow the conditional loop to prevent invalid choices
    cpu_counter_choice = random.randint(1,6) # Will make deliberate invalid choices
    print("\nThe CPU is making its choice, and has chosen:",cpu_counter_choice) 
    # Test is there are enough counters, catch errors
    while True:
        if cpu_counter_choice < total_counters:
            while True:
                if cpu_counter_choice >= 1 and cpu_counter_choice <= 3:
                    print("CPU chose",cpu_counter_choice,"counter(s)")
                    doTheMathCpu(total_counters,cpu_counter_choice)
                    break
                else:
                    print("The CPU deliberately chose",cpu_counter_choice,"counter(s)")
                    print("Taunting puny human! Mwhaha! Going again.")
                    cpu_counter_choice = random.randint(1,6)
        else:
            print("Not enough counters left! You MUST leave 1 counter.")
            print("The CPU is mocking you, adding insult to injury! Going again!")
            cpu_counter_choice = random.randint(1,1) # Force a valid CPU choice
    humanTurn(total_counters)

def doTheMathHuman(total_counters,human_counter_choice):
    # Do the math for human turn
    total_counters = total_counters - human_counter_choice
    cpuTurn(total_counters)

def doTheMathCpu(total_counters,cpu_counter_choice):
    # Do the math for CPU turn
    total_counters = total_counters - cpu_counter_choice
    humanTurn(total_counters)

def counterCheck(total_counters):
    # Catch exceptions, if counters left is less than choice, do not allow
    if 2 <= total_counters <= 10:
        print("Game ends at 1 counter remaining!",total_counters,"counter(s) to go!")
    elif total_counters <= 1:
        print(style.BOLD + "\nGame over!" + style.END)
        # No idea how to express the winner (programmatically), although it is implied.
        print("The player leaving only 1 counter is the winner!\n")
        exit()
#endregion

#region Main "Call all functions from within main()"
def main():
    totalCounters()
#endregion

# region Main "Call main() function"
main()
#endregion