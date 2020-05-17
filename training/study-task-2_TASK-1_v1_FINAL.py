#region Main "Title"
# coding=utf-8
"""Study Task 2 -Task 1
Author: Russell Dyson
Custom region folding: "Visual Studio Code Custom Folding Extension" (maptz)
"""
#endregion
#region Main "Setup Environment"
import os
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
"""Write a program that finds the largest number in a list of unsorted numbers.
For this exercise, create the list of numbers in your code (rather than asking
the user to enter the numbers). The program should check each number in the
list in turn and compare it to the largest number found so far (use a variable
to store this value whilst the program is running).
"""
#endregion
#region Main "Find Largest Number in List"
def startPoint():
    choice = input(
        style.YELLOW + 
        "Find using (1) 'list stepping' or (2) 'max()' method? " +
        style.END
        )
    choice = int(choice)
    if choice == 1:
        findWithoutMax()
    elif choice == 2:
        findWithMax()
    else:
        print(style.RED + "Invalid choice. Please try again.\n" + style.END)
        choice = input(
            "Press (1) for 'list stepping' method and (2) for 'max()' method:"
            )

def numList(numlist):    
    numlist =  \
        [888,628,604,837,517,226,431,208,681,791,832,957,581,881,738,173,754,
        728,710,650,609,894,392,244,595,583,321,36,979,81,689,988,365,759,574,
        276,23,295,803,822,915,602,194,856,725,867,704,369,560,368,462,535,585,
        993,800,197,127,447,684,419,350,446,82,790,243,518,428,834,972,41,353,
        852,46,192,320,736,827,329,942,10,236,530,451,147,526,339,641,414,691,
        250,143,294,3,19,113,635,27,980,683,995]
    return numlist

def findWithoutMax():
    print("\nThe list is:\n")
    print(numList(numList))
    highest_num = 0
    for i in numList(numList):
        if i > highest_num:
            highest_num = i
    print(
        style.BLUE + "\nThe highest number ['list stepping'] is:" + style.END,
        style.GREEN + str(max(numList(numList))) + style.END,
        "\n")

def findWithMax():
    print("\nThe list is:\n")
    print(numList(numList))
    print(
        style.BLUE + "\nThe highest number [using 'max()'] is:" + style.END,
        style.GREEN + str(max(numList(numList))) + style.END,
        "\n")
#endregion

# Call all functions from within main()
#region Main
def main():
    startPoint()
#endregion

# Call main() function
main()



