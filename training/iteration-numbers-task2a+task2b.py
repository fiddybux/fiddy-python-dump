# Write a program that asks a user to enter a number between 1 and 59 inclusive.
# The program should give the user a message if a number is outside this range 
# and ask for another number until the number input is within range.
# Extend your program so that it asks a user for 6 numbers between 1 and 59
# inclusive. After 6 numbers have been entered the program should display a
# message listing the numbers chosen.

import time
import sys

# get number
# invalidnum = True # bool loop control
ValidNumber = False
count = 0 # set empty counter
maxcount = 6
# runningcount = 6
i = 0
a = "0 0 0 0 0 0"
numlist = [] # create empty list
# while invalidnum:
while not ValidNumber:
    # for i in range(runningcount): #for count in range(counterything)????
        #Add 1 to count range for bad count?
        # for count in range(badcountadd1) or newcount or something???
        # IT'S STILL COUNTING FOR A MAX OF 6, AND OMITING BAD NUMBERS
        # CAN WE GET IT TO ADD AN EXTRA GO SO BAD NUMBERS DONT USE UP A GO?
        while i < len(a):
            num = int(input("Enter a number (1 - 59): "))
            # give the user a message if number is outside range
            # ask for another number until input is within range
            if num <= 0 or num >= 60:
                print("Badness!")
                # runningcount = maxcount + 1
                # invalidnum = True
                ValidNumber = False
                if count >= 1:
                    count -= 1
                else:
                    pass
                print("The 'i in range' value is:   ", i)
                print("The 'count' value is:        ", count)
                # print("The 'maxcount' value is:     ", maxcount)
                # print("The 'runningcount' value is: ", runningcount)
            else:
                print("Thank you!")
                count += 1
                print("The 'i in range' value is:   ", i)
                print("The 'count' value is:        ", count)
                # print("The 'maxcount' value is:     ", maxcount)
                # print("The 'runningcount' value is: ", runningcount)
                numlist.append(num) # append to list!
            # invalidnum = False
            ValidNumber = True
        else:
            i += 1
print("The numbers entered are: ", numlist)
time.sleep(2)



# for i in range(6):
    # input("number: ")