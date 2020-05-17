# coding=utf-8
"""
Random Number Guessing Game
"""

# Setup environment
import os
import random
import sys

#Clear screen (Windows)
os.system('cls')

#Define function
def randnumgame():

	# Setup begin state for variables
	success = False
	attempts = int(0)
	guesses = int(0)
	
	# Generate random integer number
	randnum = random.randint(1,100)
	
	# Iterative loop to encapsulate all
	while success == False:

            # Get user input
	    guesses = int(input("Enter a number to make your guess (1-100): "))
	    
	    # Increment guesses by 1 and print guess number
	    attempts += 1
	    print("Guess attempt:",attempts)

	    # Disqualify invalid guesses
	    if guesses <= 0 or guesses >= 101:
	        print("ERROR! Guesses must be between 0 and 100, please try again!")

	    # Check if random number matches user input
	    # If true, congratulate and declare number of turns
	    # Set winner variable to True and exit  
	    else:
	        if randnum == int(guesses):
	            print("You're a massive winner!")
	            print("You guessed ",attempts,"times before you guessed correctly.")
	            success == True
	            sys.exit()

	        # Otherwise, check user input too low / high
	        # Don't break loop
	        else:
	            if randnum < int(guesses):
	                print("The number",guesses,"is too high. Guess again!")
	            else:
	                print("That number",guesses,"is too low. Guess again!")

# Call user defined function
randnumgame()
