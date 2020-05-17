#coding=utf-8
"""
Item Cost & Change Calculator
"""

# Setup environment
import os
os.system('cls')

# Setup variables
poundsign = str("£") # Define currency symbol
rangeitemcount = int(0) # Create empty item count for range
itemlist = [] # Create empty shopping item list
itemprice = float() #Create empty item price

#Define cost calculator function
def costCalc():
    itemnumber = float(input("Enter total number of items: ")) # Get input for total number of items and populate variable
    print("Number of items chosen (to the nearest whole item):", int(itemnumber)) # Print the number of items for user feedback

    # Iterate over item numbers based on user selection
    for rangeitemcount in range(int(itemnumber)):
        print("\nCHOICE:",rangeitemcount +1) # The +1 here is more user-friendly (avoid list index 0)
        itemprice = float(input("Enter the item price in (£.p): ")) # Get user input for the price of each item
        itemlist.append(itemprice) # Append each item to a list array for later manipulation
        print("Item",rangeitemcount +1,"is:", poundsign, str(format(itemlist[rangeitemcount], '.2f'))) # Concatenate and format results and print each item price
    # print("\nPrice list stored in array:", itemlist) # PRINT ARRAY: COMMENT OUT AFTER TESTING

    # Define function to perform iterative addition on each list element 
    def listAddition(itemlist):
        total = float(0) # Define list addition variable and type
        for x in itemlist: # Iterate over each element in list array
            total += x # Add each pass onto itself, equivalent to 'total = total + x'
        return total # Return the total sum off iterations
    print("\nThe total cost of all items is:", poundsign, "{:.2f}".format(listAddition(itemlist))) # Format and concatenate results in print statement
    grandtotal = (listAddition(itemlist))

    # grandtotal = float(5.98) # ASSIGN TEMPORARY GRANDTOTAL: COMMENT OUT AFTER TESTING

    print("\nHow much are you giving the cashier?") # Ask customer to consider how much money to give
    amountpaid = float(input("Enter an amount higher than the total cost of the items (£.p): ")) # Get input as float
    changeamount = amountpaid - grandtotal # Calculate change
    pennies = round(changeamount * 100) # Convert to pennies and round float precision error
    print("\nYou have given the cashier", poundsign, "{:.2f}".format(amountpaid)) # Print change message in £.p

    # print("The change amount in pennies is", pennies,"pence") # PRINT PENNIES: COMMENT OUT AFTER TESTING

    # Create nice user-friendly formatted output and WHILE loop check for short change
    while amountpaid < grandtotal:
        enoughmoney = False
        print("You haven't given enough money. Please pay at least an extra", poundsign, "{:.2f}".format(changeamount)) # Request for extra money indicated
        print("\nHow much are you giving the cashier?") # Ask customer to consider how much money to give
        amountpaid = float(input("Enter an amount higher than the total cost of the items (£.p): ")) # Get input as float
        changeamount = amountpaid - grandtotal # Calculate change
        pennies = round(changeamount * 100) # Convert to pennies and round float precision error
        print("\nYou have given the cashier", poundsign, "{:.2f}".format(amountpaid)) # Print change message in £.p
    else:
        enoughmoney = True
        if enoughmoney == True:
            print("Total change from", poundsign, "{:.2f}".format(amountpaid), "from a goods total of", poundsign, "{:.2f}".format(grandtotal), "is", poundsign, "{:.2f}".format(changeamount))

            # Create denomination variables and do the maths
            twentypounds = int(pennies / 2000) # Create 20s variable and get division
            pennies = pennies % 2000 # Find remainder
            tenpounds = int(pennies / 1000) # Create 10s variable and get division
            pennies = pennies % 1000 # Find remainder
            fivepounds = int(pennies / 500) # Create 5s variable and get division
            pennies = pennies % 500 # Find remainder
            twopounds = int(pennies / 200) # Create 2s variable and get division
            pennies = pennies % 200 # Find remainder
            onepounds = int(pennies / 100) # Create 1s variable and get division
            pennies = pennies % 100 # Find remainder
            fiftypence = int(pennies / 50) # Create .5s variable and get division
            pennies = pennies % 50 # Find remainder
            twentypence = int(pennies / 20) # Create .2s variable and get division
            pennies = pennies % 20 # Find remainder
            tenpence = int(pennies / 10) # Create .1s variable and get division
            pennies = pennies % 10 # Find remainder
            fivepence = int(pennies / 5) # Create .05s variable and get division
            pennies = pennies % 5 # Find remainder
            twopence = int(pennies / 2) # Create .02s variable and get division
            pennies = pennies % 2 # Find remainder
            pennies = int(pennies) # Always last, lowest possible denomination

            # Print quantities of each denomination
            print("\nQUANTITY of each denomination are:\n")
            print("£20 :", twentypounds)
            print("£10 :", tenpounds)
            print("£5  :", fivepounds)
            print("£2  :", twopounds)
            print("£1  :", onepounds)
            print("50p :", fiftypence)
            print("20p :", twentypence)
            print("10p :", tenpence)
            print("5p  :", fivepence)
            print("2p  :", twopence)
            print("1p  :", pennies)

            # Manners cost nothing, but mean everything
            print("\nThank you for shopping.\n")
        else:
            pass

# Call cost calculator function
costCalc()
