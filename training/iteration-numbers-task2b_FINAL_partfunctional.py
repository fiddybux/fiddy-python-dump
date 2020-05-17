# Write a program that asks a user to enter a number between 1 and 59 inclusive.
# The program should give the user a message if a number is outside this range 
# and ask for another number until the number input is within range.
# Extend your program so that it asks a user for 6 numbers between 1 and 59
# inclusive. After 6 numbers have been entered the program should display a
# message listing the numbers chosen.

import time
import sys
ValidNumber = False
count = 0 # set empty counter
maxcount = 6 # set numver of iterations for range
i = 0 # set 'i in range' to 0
numlist = [] # create empty list
while not ValidNumber: # set not valid conditions
    for i in range(maxcount):
        num = int(input("Enter a number (1 - 59): "))
        if num <= 0 or num >= 60:
            print("Not a valid number! Please try again.")
            ValidNumber = False
            if count >= 1:
                count -= 1
            else:
                pass
            print("The 'i in range' value is:   ", i) # i check
            print("The 'count' value is:        ", count) # count check
        else:
            print("Valid number inputted. Thank you!")
            count += 1
            print("The 'i in range' value is:   ", i) # i check
            print("The 'count' value is:        ", count) # count check
            numlist.append(num) # append to list!
    ValidNumber = True # set valid conditions
print("The numbers entered are: ", numlist)
time.sleep(2)
